from django import forms
from users.models import UserData, User


class call_analyse(forms.Form):
    date_start = forms.DateField(label="Начало", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'text-field'}))
    date_end = forms.DateField(label="Конец", required=False, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': 'text-field'}))
    excel_file = forms.FileField(label="Excel-файл", required=True, widget=forms.widgets.FileInput(attrs={'accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel'}))
    range_cells_start = forms.CharField(label='Начало', required=True, widget=forms.TextInput(attrs={'placeholder':'Например, W4','class': 'text-field','size':'11'}))
    range_cells_end = forms.CharField(label='Конец', required=True, widget=forms.TextInput(attrs={'placeholder':'         W37','class': 'text-field','size':'11'}))
    uniq_num = forms.ChoiceField(required=True, widget=forms.RadioSelect(
        attrs={'class': 'Radio', 'default':'uniq'}), choices=(('uniq', 'Уникальные номера телефонов'), ('nouniq', 'Повторяющиеся номера телефонов'),))