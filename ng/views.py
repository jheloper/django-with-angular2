from django.shortcuts import render
from django.views.generic import TemplateView


class NgTestView(TemplateView):
    template_name = 'ng/index.html'
