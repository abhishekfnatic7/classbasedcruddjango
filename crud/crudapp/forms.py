from .models import Student
from django import forms


class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields="__all__"
        widgets = {
            'sname': forms.TextInput(attrs={'class':'form-control',}),
            'sage': forms.TextInput(attrs={'class':'form-control'}),
            'sgender': forms.Select(attrs={'class':'form-control'},choices=[(1, 'Mac'), (2, 'PC')]),
            'semail': forms.TextInput(attrs={'class':'form-control'}),
            'sphone': forms.TextInput(attrs={'class':'form-control'}),
            'saddress': forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'5'}),
            'simage': forms.FileInput(attrs={'class':'form-control'}),
        }
        error_messages={
            'sname':{'required':"Student Name is required"},
            'sage':{'required':"Student Age is required"},
            'sgender':{'required':"Student Gender is required"},
            'semail':{'required':"Student Email is required"},
            'sphone':{'required':"Student Phone is required"},
            'saddress':{'required':"Student Address is required"},
            'simage':{'required':"Student Image is required"},
        }
        labels={
            'sname':"Student Name",
            'sage':"Student Age",
            'sgender':"Student Gender",
            'semail':"Student Email",
            'sphone':"Student Phone",
            'saddress':"Student Address",
            'simage':"Student Image",
        }
       
    def clean_sphone(self):
        sphone=self.cleaned_data['sphone']
        if len(sphone) < 10:
            raise forms.ValidationError("Phone number is invalid")
        return sphone

       
    
