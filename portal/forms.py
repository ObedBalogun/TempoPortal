from django import forms
from .models import Staff
from datetime import datetime
STAFF_LIST=[[i.pk,i.staff_name] for i in Staff.objects.all()]
VISIT_TYPE=(('', 'Select Visit Type'),('Personal','Personal'),
('Official/Business','Official/Business'))


#Here you create the form input fields etc
class VisitorsForm(forms.Form):
    visitor_name=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visitor Name'}), label="")
    staff = forms.ChoiceField( choices=STAFF_LIST,required=True,widget=forms.Select(attrs={'class': 'btn btn-success dropdown-toggle'}),label="")
    visit_type=forms.ChoiceField(choices=VISIT_TYPE,required=True,widget=forms.Select(attrs={'class': 'btn btn-primary dropdown-toggle'}),label="")
    comment=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comment'}), label="")
    time_in=forms.DateTimeField