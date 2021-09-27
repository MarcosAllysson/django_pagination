from django.views.generic import ListView
from .models import Produto


# Create your views here.
class IndexListView(ListView):
    model = Produto
    paginate_by = 3  # número de elementos por página
    ordering = 'id'  # ordenado pelo atributo do banco
    template_name = 'index.html'
