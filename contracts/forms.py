from django import forms
from .models import Contracts, Review, Document


class DateInput(forms.DateInput):
    input_type = 'date'


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts

        fields = ['contract_type', 'contract_status', 'tag_type', 'title', 'company_name', 'contract_number',
                  'office', 'division', 'short_description', 'effective_date',
                  'expiration_date', 'renewal_date', 'prime', 'prime_pm', 'sub', 'sub_pm', 'current_year',
                  'total_funding', 'current_funding', 'funded', 'city', 'state', 'zipcode', 'contact_email',
                  'contract_award', 'main_logo', 'created_date']

        widgets = {
            'effective_date': DateInput(),
            'expiration_date': DateInput(),
            'renewal_date': DateInput(),
            'created_date': forms.TextInput(
                attrs={'class': 'form-control', 'readonly': 'readonly'}
            )
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ['text', 'atRisk']

        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
            'atRisk': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'title': 'At Risk'}
            )
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = ['document_type', 'title', 'tag', 'attach_file']
