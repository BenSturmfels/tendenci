from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import CustomMetaForm, CustomMetaConfirmDeletion
from .models import CustomMeta


@user_passes_test(lambda u: u.is_superuser)
@login_required
def show_custom_meta_data(request):
    if request.method == 'GET':
        all_top_level_page_data = []
        for each in CustomMeta.objects.all():
            all_top_level_page_data.append({"id": each.pk, "title": each.title, "keywords": each.keywords,
                                            "canonical_url": each.canonical_url,
                                            "description": each.description, "page_path": each.page_path})
        return render(request, 'meta/custom-meta-show.html',
                      context={"top_level_page_data": all_top_level_page_data})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_custom_meta_data(request):
    if request.method == 'POST':
        the_form = CustomMetaForm(request.POST)
        if the_form.is_valid():
            the_form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added new metadata.')
            return HttpResponseRedirect(reverse('show_custom_meta_data'))
        else:
            return render(request, 'meta/custom-meta-add.html', context={"form": the_form})
    if request.method == 'GET':
        the_form = CustomMetaForm()
        return render(request, 'meta/custom-meta-add.html', context={"form": the_form})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def edit_custom_meta_data(request, metadata_id):
    try:
        metadata_object = CustomMeta.objects.get(pk=int(metadata_id))
    except:
        messages.add_message(request, messages.ERROR, 'The object does not exist.')
        return HttpResponseRedirect(reverse('show_custom_meta_data'))
    if request.method == 'POST':
        the_form = CustomMetaForm(request.POST, instance=metadata_object)
        if the_form.is_valid():
            try:
                metadata_object.title = the_form.cleaned_data['title']
                metadata_object.keywords = the_form.cleaned_data['keywords']
                metadata_object.description = the_form.cleaned_data['description']
                metadata_object.canonical_url = the_form.cleaned_data['canonical_url']
                metadata_object.page_path = the_form.cleaned_data['page_path']
                metadata_object.save()
                messages.add_message(request, messages.SUCCESS, 'Successfully added new metadata.')
                return HttpResponseRedirect(reverse('show_custom_meta_data'))
            except:
                messages.add_message(request, messages.ERROR, 'Failed to save metadata.')
                return render(request, 'meta/custom-meta-edit.html',
                              context={"form": the_form})
        else:
            return render(request, 'meta/custom-meta-edit.html', context={"form": the_form})
    if request.method == 'GET':
        the_form = CustomMetaForm(initial={"title": metadata_object.title, "keywords": metadata_object.keywords,
                                             "description": metadata_object.description,
                                             "canonical_url": metadata_object.canonical_url,
                                             "page_path": metadata_object.page_path})
        return render(request, 'meta/custom-meta-edit.html', context={"form": the_form})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_custom_meta_data(request, metadata_id):
    try:
        metadata_object = CustomMeta.objects.get(pk=int(metadata_id))
    except:
        messages.add_message(request, messages.ERROR, 'The object does not exist.')
        return HttpResponseRedirect(reverse('show_custom_meta_data'))
    if request.method == 'POST':
        the_form = CustomMetaConfirmDeletion(request.POST)
        if the_form.is_valid():
            try:
                metadata_object.delete()
                messages.add_message(request, messages.SUCCESS, 'Successfully deleted metadata.')
                return HttpResponseRedirect(reverse('show_custom_meta_data'))
            except:
                messages.add_message(request, messages.ERROR, 'Failed to delete metadata.')
                return HttpResponseRedirect(reverse('show_custom_meta_data'))
        else:
            return render(request, 'meta/custom-meta-delete.html', context={"form": the_form})
    if request.method == 'GET':
        the_form = CustomMetaConfirmDeletion()
        return render(request, 'meta/custom-meta-delete.html', context={"form": the_form})
