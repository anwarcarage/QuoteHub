from django.contrib import admin
from django.urls import path
from .views import MainPageView, CreateQuoteView, TestBaseView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main_page'),
    path('createquote/', CreateQuoteView.as_view(), name='create_quote'),
    path('testbase/', TestBaseView.as_view(), name='test_base'),
    path('quoteform/', views.quote_new, name='quote_form'),
    path('quoteform/calculate', views.calculate, name='calculate')
]