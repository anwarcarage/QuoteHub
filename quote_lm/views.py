from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import QuoteLm
from .forms import QuoteForm
from django.shortcuts import render, redirect


def quote_new(request):

    form = QuoteForm

    return render(request, 'createquote.html', {'form': form})

# called with the calculate button
def calculate(request):
    # if request.method == 'POST':
    #     quote_info = QuoteForm(request.POST)
    #     if quote_info.is_valid():
    #         quote_info.save()
    #     else:
    #         return render(request, 'createquote.html', {'form':quote_info})

    form = QuoteForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'createquote.html', context)

    # if request.method == 'POST':
    #     form = QuoteForm(request.POST)
    #     if form.is_valid():
    #         data = form.save(commit=False)
    #         data.quote_id = request.quote_id
    #         data.save()
    #     return render(request, 'createquote.html', {'form': form})

class MainPageView(TemplateView):
    template_name = 'mainpage.html'
    fields = [
        'quote_id',
        'customer_name',
        'date'
    ]

class CreateQuoteView(CreateView):
    model = QuoteLm
    template_name = 'createquote.html'
    fields = [
        'quote_id',
        'customer_name',
        'date',
        'length',
        'width',
        'height',
        'material',
        'surface_finish',
        'h_headers',
        'v_headers',
        'bubs_num',
        'drill_bar_num',
        # 'image'
    ]

class TestBaseView(TemplateView):
    template_name = 'base.html'




