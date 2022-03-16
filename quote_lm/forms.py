from django.forms import ModelForm
from quote_lm.models import QuoteLm
from crispy_forms.helper import FormHelper


class QuoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['customer_id'].widget.attrs.update({'class':'form-select'})
        self.fields['material'].widget.attrs.update({'class':'form-select'})
        self.fields['surface_finish'].widget.attrs.update({'class':'form-select'})

    class Meta:
        model = QuoteLm
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
        ]

