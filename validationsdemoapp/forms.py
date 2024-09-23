
from django import forms 
from django.forms import DateInput, EmailInput, PasswordInput,RadioSelect, Select, URLInput 
from validationsdemoapp.models import UserRegistration
import re 

class UserRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = UserRegistration 
        fields = '__all__'
        
        genders=[{"male","Male"},{"female","Female"}]
        
        countries=[("select","Please Choose Country"),
                   ("India","India"),
                   ("Australia", "Australia"),
                   ("American","America"),
                   ("Pakistani","Pakistan")
                   ]
        
        widgets = {
            'password':PasswordInput(),
            'confirm_password': PasswordInput(),
            'gender':RadioSelect(choices=genders),
            'country':Select(choices=countries),
            'date_of_birth':DateInput(attrs={'type':'date'}),
            'email' : EmailInput(),
            'website_url':URLInput()
            
            
        }
        # feild level validations
        
        def clean_phone_number(self):
            iphonenumber = self.cleaned_data.get("phonenumber")
            if iphonenumber:
                pattern =re.compile(r"(0|91)?[6-9][0-9]{9}")
                if not re.fullmatck(pattern, iphonenumber):
                    raise forms.ValidationError("Invalid Phone Number! Example :+9111234657891.")
                return iphonenumber
            
            
        def clean(self):
            cleaned_data = super().clean()
            ipassword = cleaned_data.get("password")
            iconfirm_password = cleaned_data.get("confirm_password")
            
            if ipassword and iconfirm_password:
                if ipassword != iconfirm_password:
                    raise forms.ValidationError("Password do not match.")
                
            iusername = cleaned_data.get("username")
            ipassword = cleaned_data.get("password")
            
            if ipassword and iusername:
                if ipassword == iusername:
                    raise forms.ValidationError("User Name and password should not be Same...")
            
            country = cleaned_data.get('country')
            if country == 'select':
                raise forms.ValidationError('Please choose a country.')
            
            terms_conditions = cleaned_data.get('terms_conditions')
            
            if not terms_conditions:
                raise forms.ValidationError('Please agree to terms and conditions!..')
            
            
            return cleaned_data
            
            
        
        
        