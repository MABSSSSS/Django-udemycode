from django import forms 

from PayRollApp.models import Employee

from django.forms import modelform_factory 
from PayRollApp.models import PartTimeEmployee 


class EmployeeForm(forms.ModelForm):
    class Meta:
        model =Employee 
        fields="__all__"
        
        widgets = {
            'BirthDate' : forms.widgets.DateInput(attrs={'type': 'date'}),
            'HireDate' : forms.widgets.DateInput(attrs={'type':'date'}),
        }
        
PartTimeEmployeeForm = modelform_factory(PartTimeEmployee, fields=['FirstName','LastName','TitleName'])

class DynamicPartTimeEmployeeForm(PartTimeEmployeeForm):
    def __init__(self, *args, **kwargs):
        super(DynamicPartTimeEmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop("required", None)
        
        
class NewPartTimeEmployeeForm(forms.ModelForm):
    class Meta:
        model=PartTimeEmployee
        fields="__all__"
        
PartTimeEmployeeFormSet = forms.modelformset_factory(PartTimeEmployee, form=NewPartTimeEmployeeForm, extra=10)

    
    
