from django import forms
from .models import Review, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CustomSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.help_text = ''

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        labels = {'avatar': 'Sua Foto de Perfil'}