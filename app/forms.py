from django import forms

class CompanyForm(forms.Form):

    company_id = forms.CharField(max_length = 255) 
    gst = forms.CharField(max_length = 255)
