from django import forms

class CreateNewList(forms.Form): #inherit class automaticly checks the fields u defined to make sure they has valid input
    name = forms.CharField(label='Name', max_length=200)
    check = forms.BooleanField(required=False)


