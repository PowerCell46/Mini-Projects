from django import forms

from djangoWorkingFolder.sofiauniproject.models import SatelliteImage


class SatelliteCreateForm(forms.ModelForm):
    class Meta:
        model = SatelliteImage
        fields =\
            ['territory', 'sourceUrl', 'dataSource', 'trueColourImage', 'falseColourImage', 'NDVIimage', 'imageDate']
        labels = {
            'territory': '',
            'sourceUrl': '',
            'dataSource': 'Data Source',
            'trueColourImage': 'True Colour Image',
            'falseColourImage': 'False Colour Image',
            'NDVIimage': 'NDVI Image',
            'imageDate': '',
        }
        widgets = {
            'territory': forms.TextInput(attrs={'placeholder': 'Territory'}),
            'sourceUrl': forms.TextInput(attrs={'placeholder': 'Source URL'}),
            'trueColourImage': forms.FileInput(attrs={'class': 'file-upload'}),
            'falseColourImage': forms.FileInput(attrs={'class': 'file-upload'}),
            'NDVIimage': forms.FileInput(attrs={'class': 'file-upload'}),
            'imageDate': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(SatelliteCreateForm, self).__init__(*args, **kwargs)
        self.fields['imageDate'].initial = '2023-07-22'

        default_data_source = 'S-2'
        self.fields['dataSource'].initial = default_data_source
