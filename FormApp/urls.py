from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_form_link, name='generate_form_link'),
    path('<slug:form_slug>/', views.open_form, name='open_form'),
    path('confirm/<slug:form_slug>/', views.confirm_form, name='confirm_form'),
]