from django import forms
from .models import Portfolio, Portfolio_image
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PortfolioForm(forms.ModelForm):
    portfolio = '[포트폴리오]'
    CATEGORY_CHOICES = [
        (portfolio, '포트폴리오'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'title_input',
                'placeholder':'제목',
            }
        )
    )

    content = forms.CharField(
        widget=CKEditorUploadingWidget())
        

    class Meta:
        model = Portfolio
        exclude = [('author'),]

class Portfolio_imageForm(forms.ModelForm):

    class Meta:
        model = Portfolio_image
        exclude = [('portfolio'),]