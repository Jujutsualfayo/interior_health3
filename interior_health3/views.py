from django.views.generic import TemplateView

class ReactAppView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except TemplateDoesNotExist:
            return HttpResponseNotFound('<h1>React App not built yet.</h1>')
