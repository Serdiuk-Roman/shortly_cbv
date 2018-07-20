#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms

from .models import Shortly


class ShortlyForm(forms.ModelForm):
    class Meta:
        model = Shortly
        fields = ('url_target',)
