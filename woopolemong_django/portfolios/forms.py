from django import forms
from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    portfolio = '[포트폴리오]'
    CATEGORY_CHOICES = [
        (portfolio, '포트폴리오'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Portfolio
        exclude = [('author'),]
