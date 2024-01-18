from django import forms
from users.models import UserData, User


class call_analyse(forms.Form):
    date_start = forms.DateField(label="Начало", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'text-field'}))
    date_end = forms.DateField(label="Конец", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'text-field'}))
    excel_file = forms.FileField(label="Excel-файл", required=True, widget=forms.widgets.FileInput(attrs={'accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel'}))
