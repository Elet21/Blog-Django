from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .forms import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, requests, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(requests, self.template, context={self.model.__name__.lower():obj, 'admin_object': obj, 'detail': True})


class ObjectsCreateMixin:
    form_model = None
    template = None

    def get(self, requests):
        form = self.form_model()
        return render(requests, self.template, context={'form': form})

    def post(self, requests):
        bound_form = self.form_model(requests.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(requests, self.template, context={'form': bound_form})


class ObjectsUpdateMixin:
    model = None
    form_model = None
    template = None


    def get(self, requests, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return render(requests, self.template, context={'form': bound_form, self.model.__name__.lower():obj})

    def post(self, requests, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(requests.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(requests, self.template, context={'form': bound_form, self.model.__name__.lower():obj})


class ObjectDeleteMixin:
    model = None
    template = None
    url = None


    def get(self, requests, slug):
        new_obj = self.model.objects.get(slug__iexact=slug)
        return render(requests, self.template, context={self.model.__name__.lower(): new_obj})

    def post(self, requests, slug):
        new_obj = self.model.objects.get(slug__iexact=slug)
        new_obj.delete()
        return redirect(reverse(self.url))
