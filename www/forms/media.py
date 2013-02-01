from django.forms import ModelForm
from www.models import DlnaSettings, Collection


class DlnaSettingsForm(ModelForm):
    class Meta:
        model = DlnaSettings
        exclude = ('hash_id', 'version', 'created')


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        exclude = ('created', 'edited')
