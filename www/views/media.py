from django.shortcuts import render_to_response, get_object_or_404
from www.models import DlnaSettings, Collection
from www.forms.media import DlnaSettingsForm, CollectionForm


def settings(request):
    settings = DlnaSettings.objects.order_by('-version')[0]
    settings_form = DlnaSettingsForm(instance=settings)
    return render_to_response('manage/dlna.html', {
        'form': settings_form
    })


def collection(request, collection_id=None):
    if request.POST:
        collection_form = CollectionForm(request.POST)
        # Validate etc
    else:
        if collection_id:
            collection = get_object_or_404(Collection, id=collection_id)
            collection_form = CollectionForm(instance=collection)
        else:
            collection_form = CollectionForm()

    return render_to_response('manage/collections/create.html', {
        'collection_form': collection_form,
        'is_edit': (collection_id is not None),
    })


def manage_media(request):
    return render_to_response('manage/media.html')
