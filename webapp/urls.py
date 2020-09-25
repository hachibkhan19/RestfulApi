from django.urls import path
from . import views
from django.conf.urls import url
from .api import QuoteApi, CategoryApi, QuoteDetail

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('quote/', views.QuotesView.as_view(), name='quote'),
    url(r'^api/quotes/$', QuoteApi.as_view(), name='quotes'),
    url(r'^api/quotes/(?P<id>\d+)/$', QuoteDetail.as_view(), name='quotes'),
    url(r'^api/category/$', CategoryApi.as_view(), name='category'),
]
