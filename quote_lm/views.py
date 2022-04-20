from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import QuoteLm, CalcHour, CalcPrice, SearchQuote
from .forms import QuoteForm, HoursForm, PriceForm, SearchForm
from django.shortcuts import render
from .DBWork import hours_calculate, update_calculate
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
    display = QuoteLm.objects.order_by('-date')[:6]

    context = {'form': form, 'display': display}

    return render(request, 'mainpage.html', context)


# search for quote and/or customer
def search_quotes(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query1 = form.cleaned_data.get('quote_id')
        query2 = form.cleaned_data.get('customer_id')
        if query1 and query2:
            display = QuoteLm.objects.filter(quote_id__contains=query1).filter(customer_id=query2)
            context = {'form': form, 'display': display}
            return render(request, 'mainpage.html', context)
        if query1:
            display = QuoteLm.objects.filter(quote_id__contains=query1)
            context = {'form': form, 'display': display}
            return render(request, 'mainpage.html', context)
        if query2:
            display = QuoteLm.objects.filter(customer_id=query2)
            context = {'form': form, 'display': display}
            return render(request, 'mainpage.html', context)


def edit_quote(request):
    query = request.GET.get('id', False)                    # gets quote_lm.id value from card
    if request.method == 'GET':
        quote = QuoteLm.objects.get(id=query)
        form = QuoteForm(instance=quote)
        hours = CalcHour.objects.get(quote_id_id=query)
        price = CalcPrice.objects.get(quote_id_id=query)
        context = {'form': form, 'hours': hours, 'price': price}
        return render(request, 'updatequote.html', context)
    if request.method == 'POST':
        quote = QuoteLm.objects.get(id=query)
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            update_calculate(track_id=query)
            hours = CalcHour.objects.get(quote_id_id=query)
            price = CalcPrice.objects.get(quote_id_id=query)
            context = {'form': form, 'hours': hours, 'price': price}
            return render(request, 'updatequote.html', context)
        else:
            return HttpResponse(form.errors)


def delete_quote(request):
    query = request.GET.get('id', False)                    # gets quote_lm.id value from card
    quote = QuoteLm.objects.get(id=query)
    hours = CalcHour.objects.get(quote_id_id=query)
    price = CalcPrice.objects.get(quote_id_id=query)
    quote.delete()
    hours.delete()
    price.delete()
    return mainpage(request)


class MainPageView(TemplateView):
    model = SearchQuote
    template_name = 'mainpage.html'
    fields = [
        'quote_id',
        'customer_id',
        'date',
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




