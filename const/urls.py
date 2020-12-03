from django.urls import path
from.views import HomePageView , contactView, successView, HomePage



urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', HomePage, name='home'),
    #path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]
