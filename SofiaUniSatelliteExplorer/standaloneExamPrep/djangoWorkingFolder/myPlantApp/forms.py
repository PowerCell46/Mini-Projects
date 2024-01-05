from django import forms

from djangoWorkingFolder.myPlantApp.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    ...


class PlantEditForm(PlantBaseForm):
    ...


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


