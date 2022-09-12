from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_Katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_Katalog,
    'nama': 'Dave Matthew Peter Lumban Tobing',
    'NPM' : '2106700870'
    }
    return render(request, "katalog.html", context)

