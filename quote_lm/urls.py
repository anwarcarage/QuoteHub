from django.contrib import admin
from django.urls import path
from .views import MainPageView, CreateQuoteView, TestBaseView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.mainpage, name='main_page'),
    path('home/search', views.search_quotes, name='search'),
    path('createquote/', CreateQuoteView.as_view(), name='create_quote'),
    path('testbase/', TestBaseView.as_view(), name='test_base'),
    path('quoteform/', views.quote_new, name='quote_form'),
    path('quoteform/calculate', views.calculate, name='calculate'),
    path('quoteform/edit', views.edit_quote, name='edit'),
    path('home/delete', views.delete_quote, name='delete'),
]