#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('', views.TopShortlyList.as_view()),
    path('all/', views.ShortlyList.as_view()),
    path('new/', views.ShortlyCreate.as_view()),
    path(
        'detail/<int:pk>/',
        views.ShortlyDetail.as_view(),
        name='shortly-detail'
    ),
    path('follow/<int:pk>/', views.ShortlyCounterRedirectView.as_view()),
]
