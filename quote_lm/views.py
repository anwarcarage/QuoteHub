from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import QuoteLm, CalcHour, CalcPrice, SearchQuote
from .forms import QuoteForm, HoursForm, PriceForm, SearchForm
from django.shortcuts import render
from .DBWork import hours_calculate
from django.shortcuts import HttpResponse

# calls new quote page
def quote_new(request):

    form = QuoteForm

    context = {'form': form}

    return render(request, 'createquote.html', context)


# called with the calculate button to fill in hours and dollars table
def calculate(request):
    form = QuoteForm(request.POST or None)
    hours = HoursForm
    price = PriceForm
    if form.is_valid():
        test = form.save()
        track_id = test.id
        hours_calculate(track_id)
        hours = CalcHour.objects.get(quote_id_id=track_id)
        price = CalcPrice.objects.get(quote_id_id=track_id)
        context = {'form': form, 'hours': hours, 'price': price}
        return render(request, 'createquote.html', context)
    else:
        return render(request, 'createquote.html', {'form': form, 'hours': hours, 'price': price})


# calls main page with six most recent entries by date (initial load)
def mainpage(request):
    form = SearchForm
    recent = QuoteLm.objects.order_by('-date')[:6]

    context = {'form': form, 'recent': recent}

    return render(request, 'mainpage.html', context)


def search_quotes(request):
    form = SearchForm
    if form.is_valid():
        quote_id = form.cleaned_data['quote_id']
        customer = form.cleaned_data['customer_id']
        date = form.cleaned_data['data']
        form = QuoteLm.objects.filter(quote_id=quote_id)
        context = {'form': form}

        return render(request, 'mainpage.html', context)


class MainPageView(TemplateView):
    model = SearchQuote
    template_name = 'mainpage.html'
    fields = [
        'quote_id',
        'customer_id',
        'date'
    ]


class CreateQuoteView(CreateView):
    model = QuoteLm
    template_name = 'createquote.html'
    fields = [
        'quote_id',
        'customer_id',
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
        # 'image',
    ]


class TestBaseView(TemplateView):
    template_name = 'base.html'




