from django import forms
from .models import SurveillanceRecord

class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget(),
            'plant_parts': forms.CheckboxSelectMultiple()
        }
