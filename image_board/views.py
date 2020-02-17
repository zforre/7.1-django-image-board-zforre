from django.views.generic import TemplateView
from .models import Image

# Create your views here.

class ImageBoard(TemplateView):
    template_name = 'imageboard.html' #class based view

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            'images': images
        }

        return context