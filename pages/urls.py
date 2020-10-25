from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView

urlpatterns = [
    path('base/', BasePageView.as_view(), name='base'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),

]
