from django.views.generic import TemplateView

from django.views import View
from django.shortcuts import render

class ReactAppView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')  # Adjust the template if necessary

