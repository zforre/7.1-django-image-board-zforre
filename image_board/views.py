from django.shortcuts import render
from .models import Image

# Create your views here.
class ImageBoard(TemplateView):
    template_name = 'index.html' #class based view

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            'images': images
        }

        return context