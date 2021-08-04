from django import forms
from .models import Post

class TextForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('first_name', 'first_name_kana', 'last_name', 'last_name_kana',
                  'call_num', 'address', 'memo')
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder': '姓'}),
            'first_name_kana':forms.TextInput(attrs={'placeholder': '姓(フリガナ)'}),
            'last_name':forms.TextInput(attrs={'placeholder': '名'}),
            'last_name_kana':forms.TextInput(attrs={'placeholder': '名(フリガナ)'}),
            'call_num':forms.TextInput(attrs={'placeholder': '携帯番号'}),
            'address':forms.TextInput(attrs={'placeholder': 'メールアドレス'}),
            'memo':forms.TextInput(attrs={'placeholder': 'メモ'}),
        }

class updateform(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('first_name', 'first_name_kana', 'last_name', 'last_name_kana',
                  'call_num', 'address', 'memo')
        widgets = {
            'first_name':forms.TextInput(),
            'first_name_kana':forms.TextInput(),
            'last_name':forms.TextInput(),
            'last_name_kana':forms.TextInput(),
            'call_num':forms.TextInput(),
            'address':forms.TextInput(),
            'memo':forms.TextInput(),
        }