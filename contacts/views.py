from contacts.models import Contact
from rest_framework import generics
from rest_framework.parsers import JSONParser


from .serializer import ContactSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
         return Contact.objects.all()
        
    def perform_create(self, serializer):
        serializer.save()