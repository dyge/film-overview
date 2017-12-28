from django.views.generic import ListView
from verwaltung.models import Film

class HomePage(ListView):
    queryset = Film.objects.all()
    context_object_name = 'films'
    # paginate_by = 3
    template_name = "index.html"
