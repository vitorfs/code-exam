# coding: utf-8
from datetime import time
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView

class Homepage(TemplateView):
    template_name = 'index.html'