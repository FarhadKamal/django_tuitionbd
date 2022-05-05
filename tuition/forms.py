from tkinter import Widget
from django import forms
from .models import Contact,Post

class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=100, label='Your name')
    # hobby = forms.CharField(max_length=20 , label='Your hobby')
    class Meta:
        model = Contact
        fields='__all__' 
        
        widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':'who the are yoy?'})}
    def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].label='My Name'
            self.fields['name'].initial='My Name'
    def clean_name(self):
        value = self.cleaned_data["name"]
        num_of_word= value.split(' ')
        print(num_of_word)
        if len(num_of_word)>3 :
            self.add_error('name','sabdhane no! more 3 word!')
        else: return value
class ContactFormtwo(forms.ModelForm):
    # name = forms.CharField(max_length=100, label='Your name')
    # hobby = forms.CharField(max_length=20 , label='Your hobby')
    class Meta:
        model = Contact
        fields='__all__'         
      
class PostForm(forms.ModelForm):
    # name = forms.CharField(max_length=100, label='Your name')
    # hobby = forms.CharField(max_length=20 , label='Your hobby')
    class Meta:
        model = Post
        exclude = ['user','id','created_at','slug']   
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True}),
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True}),   

        }     
