from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import QuoteLm


class CreateQuoteView(CreateView):
    models = QuoteLm
    template_name = 'createquote.html'
    fields = [
        'quote_id',
        # 'customer_name',
        # 'date',
        # 'length',
        # 'width',
        # 'height',
        # 'material',
        # 'surface_finish',
        # 'h_headers',
        # 'v_headers',
        # 'bubs_num',
        # 'drill_bar_num',
        # 'image'
    ]

class MainPageView(TemplateView):
    template_name = 'mainpage.html'
    fields = [
        'quote_id',
        'customer_name',
        'date'
    ]

class TestBaseView(TemplateView):
    template_name = 'base.html'



