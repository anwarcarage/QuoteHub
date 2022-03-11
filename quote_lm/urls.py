from django.urls import path
from .views import MainPageView, CreateQuoteView, TestBaseView


urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('createquote/', CreateQuoteView.as_view(), name='createquote'),
    path('testbase/', TestBaseView.as_view(), name='testbase')
]