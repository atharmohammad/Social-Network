from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='index.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'

class TestView(TemplateView):
    template_name = 'test.html'