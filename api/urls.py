from django.urls import path
from .views import extract_pdfs

urlpatterns = [
    path('extract/', extract_pdfs),
]
