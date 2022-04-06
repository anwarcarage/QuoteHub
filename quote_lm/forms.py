from django.forms import ModelForm
from quote_lm.models import QuoteLm, CalcHour, CalcPrice, SearchQuote
from crispy_forms.helper import FormHelper


class QuoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['customer_id'].widget.attrs.update({'class': 'form-select'})
        self.fields['material'].widget.attrs.update({'class': 'form-select'})
        self.fields['surface_finish'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = QuoteLm
        fields = [
            'id',
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
        ]


class HoursForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CalcHour
        fields = [
            'weld_hours',
            'fit_hours',
            'program_hours',
            'machine_hours',
            'bench_hours',
            'assembly_hours',
            'shipping_hours',
            'laser_hours',
            'inspect_hours',
            'total_hours',
        ]


class PriceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CalcPrice
        fields = [
            'weld_price',
            'fit_price',
            'program_price',
            'machine_price',
            'bench_price',
            'assembly_price',
            'shipping_price',
            'laser_price',
            'inspect_price',
            'total_price',
        ]


class SearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['customer_id'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = SearchQuote
        fields = [
            'quote_id',
            'customer_id',
            'date',
        ]
