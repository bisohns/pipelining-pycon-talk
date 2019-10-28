from django.shortcuts import render
from django.views.generic import TemplateView


class PyconView(TemplateView):
    template_name = "pycon.html"
