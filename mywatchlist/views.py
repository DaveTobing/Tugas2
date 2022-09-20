from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
    'list_movie': data_watchlist,
    'nama': 'Dave Matthew Peter Lumban Tobing',
    'NPM' : '2106700870'
    }
    return render(request, "mywatchlist.html", context)


def show_start(request):
    context = {
    'nama': 'Dave Matthew Peter Lumban Tobing',
    'NPM' : '2106700870'
    }
    return render(request, "start.html", context)