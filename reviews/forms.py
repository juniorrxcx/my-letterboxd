from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Sua Nota',
            'comment': 'Comentário (opcional)'
        }
        widgets = {
            'rating': forms.Select(choices=[(1, '1 Estrela'), (2, '2 Estrelas'), (3, '3 Estrelas'), (4, '4 Estrelas'), (5, '5 Estrelas')]),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'O que você achou do filme?'}),
        }