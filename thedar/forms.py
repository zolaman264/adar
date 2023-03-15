from django import forms
from .models import Post



class DateInput(forms.DateInput):
        input_type='time'
        


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('checkin','checkout','position','author','details','report','report_image')
        widgets={
            'checkin': DateInput(attrs={'class':'form-control' }),
            'checkout':DateInput(attrs={'class':'form-control'}),
            'position':forms.Select(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'zola','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'details':forms.Textarea(attrs={'class':'form-control'}),
             'report':forms.Textarea(attrs={'class':'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('checkin','checkout','position','author','details','report')
        widgets={
           'checkin':forms.TimeInput(attrs={'class':'form-control'}),
            'checkout':forms.TimeInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control ','value':'','id':'zola','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'details':forms.Textarea(attrs={'class':'form-control'}),
             'report':forms.Textarea(attrs={'class':'form-control'}),

        }