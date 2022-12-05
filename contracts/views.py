import datetime
from datetime import datetime

from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from django.views import View

import send
from .common.utils.process import html_to_pdf
from .common.utils.send_task import send_task_notification
from .forms import ContractForm, ReviewForm, DocumentForm
from .models import Contracts, Review, Document
from .filters import ContractFilter


# home index page here
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('contracts/index.html')
    user_name = request.user.username
    # my_index_contracts = Contracts.objects.order_by('-created_date')
    # if user_name == "admin" or user_name == "contractsadmin":
    #    my_index_contracts = Contracts.objects.order_by('-created_date')
    # else:
    # my_index_contracts = request.user.objects.order_by('-created_date')
    my_index_contracts = Contracts.objects.order_by('-created_date')

    context = {"my_index_contracts": my_index_contracts}
    context.update(dict(Contracts.total_info()))
    context['best_month'] = Contracts.best_month()
    context['contracts_month_report'], context['contracts_month_report_labels'] = Contracts.contracts_month_report()

    return HttpResponse(html_template.render(context, request))


# create all_contracts
def all_contracts(request):
    all_contracts = Contracts.objects.order_by('-created_date')

    my_Filter = ContractFilter(request.GET, queryset=all_contracts)
    all_contracts = my_Filter.qs

    context = {"all_contracts": all_contracts, "my_Filter": my_Filter}
    return render(request, 'contracts/all_contracts.html', context)


# create new_contract
def new_contract(request):
    if request.method != 'POST':
        form = ContractForm()
    else:
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # send notification
            send_task_notification(request)
            return redirect('contracts:all_contracts')

    context = {'form': form}
    return render(request, 'contracts/new_contract.html', context)


# create detail_contract
def detail_contract(request, detail_id):
    detail_contract = Contracts.objects.get(id=detail_id)

    reviews = Review.objects.filter(contract=detail_contract)

    documents = Document.objects.filter(contract=detail_contract)

    context = {'detail_contract': detail_contract, 'reviews': reviews, 'documents': documents}
    return render(request, 'contracts/detail_contract.html', context)


# create my_contracts
def my_contracts(request):
    # my_contracts = Contracts.objects.order_by('-created_date')
    my_contracts = request.user.contracts_set.order_by('-created_date')

    context = {"my_contracts": my_contracts}
    return render(request, 'contracts/my_contracts.html', context)


# create my_contracts_explorer
def my_contracts_explorer(request):
    # my_contracts = Contracts.objects.order_by('-created_date')
    my_contracts_explorers = request.user.contracts_set.order_by('-created_date')

    context = {"my_contracts_explorers": my_contracts_explorers}
    return render(request, 'contracts/my_contracts_explorer.html', context)


# create edit_contract
def edit_contract(request, edit_id):
    contract = Contracts.objects.get(id=edit_id)

    if request.method != 'POST':
        form = ContractForm(instance=contract)
    else:
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contracts:my_contracts')

    context = {'contract': contract, 'form': form}
    return render(request, 'contracts/edit_contract.html', context)


# create delete_contract
def delete_contract(request, delete_id):
    contract = Contracts.objects.get(id=delete_id)

    if request.method != 'POST':
        contract.delete()
        return redirect('contracts:my_contracts')

    context = {'contract': contract}
    return render(request, 'contracts/delete_contract.html', context)


def create_review(request, contract_id):
    contract = get_object_or_404(Contracts, pk=contract_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = ReviewForm()
    else:
        # POST data submitted, process data.
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new entry and assign to contract.
            newReview = form.save(commit=False)
            # Set the new contract attribute to the current user.
            newReview.user = request.user
            # Save to database now the object has all the required data.
            newReview.contract = contract

            newReview.save()

            return redirect('contracts:detail_contract', newReview.contract.id)

    context = {"form": form, 'contract': contract}
    return render(request, 'contracts/new_review.html', context)


def update_review(request, review_id):
    # review = Review.objects.get(id=review_id)
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method != 'POST':
        form = ReviewForm(instance=review)
    else:
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('contracts:detail_contract', review.contract.id)

    context = {"review": review, 'form': form}
    return render(request, 'contracts/update_review.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    review.delete()

    return redirect('contracts:detail_contract', review.contract.id)


def create_document(request, contract_id):
    contract = get_object_or_404(Contracts, pk=contract_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = DocumentForm()
    else:
        # POST data submitted, process data.
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new entry and assign to contract.
            newDocument = form.save(commit=False)
            # Set the new contract attribute to the current user.
            newDocument.user = request.user
            # Save to database now the object has all the required data.
            newDocument.contract = contract

            newDocument.save()
            # send email

            return redirect('contracts:detail_contract', newDocument.contract.id)

    context = {"form": form, 'contract': contract}
    return render(request, 'contracts/new_document.html', context)


def update_document(request, document_id):
    # review = Review.objects.get(id=review_id)
    document = get_object_or_404(Document, pk=document_id, user=request.user)

    if request.method != 'POST':
        form = DocumentForm(instance=document)
    else:
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('contracts:detail_contract', document.contract.id)

    context = {"document": document, 'form': form}
    return render(request, 'contracts/update_document.html', context)


def delete_document(request, document_id):
    document = get_object_or_404(Review, pk=document_id, user=request.user)

    document.delete()

    return redirect('contracts:detail_contract', document.contract.id)


# Creating a class based view
class GeneratePdf(View):
    def get(self, request, detail_id, *args, **kwargs):
        # report_data = Contracts.objects.all()
        report_data = Contracts.objects.get(id=detail_id)

        context = {"report_data": report_data}
        # invoice
        reports = html_to_pdf('reports/invoice-details.html', context)
        # getting the template
        # reports = html_to_pdf('reports/results.html', context)
        # All Reports
        # reports = html_to_pdf('reports/results-all.html', context)

        # rendering the template
        return HttpResponse(reports, content_type='application/pdf')
