from django.urls import path
from .views import MainPageView, CreateQuoteView


urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('newquote/', CreateQuoteView.as_view(), name='newquote')
]