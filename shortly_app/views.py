#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from .models import Shortly
from .forms import ShortlyForm


class ShortlyList(ListView):
    model = Shortly
    template_name = "shortly_app/list.html"
    context_object_name = "all_el"


class TopShortlyList(ListView):
    model = Shortly
    template_name = "shortly_app/list.html"
    context_object_name = "all_el"
    queryset = Shortly.objects.filter(
        click_count__gte=5).order_by('-click_count')


class ShortlyCreate(CreateView):
    model = Shortly
    template_name = "shortly_app/new_url.html"
    form_class = ShortlyForm

    def get_success_url(self):
        link_url = reverse(
            'shortly-detail',
            args=[self.object.pk]
        )
        return link_url


class ShortlyDetail(DetailView):
    model = Shortly
    template_name = "shortly_app/detail.html"
    context_object_name = "link"


class ShortlyCounterRedirectView(RedirectView):
    permanent = False
    query_string = True
    model = Shortly

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Shortly, pk=kwargs['pk'])
        link.click_count += 1
        link.save(update_fields=['click_count'])
        return link.url_target
