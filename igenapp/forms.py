from django import forms


class IssueForm(forms.Form):

    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=500)
