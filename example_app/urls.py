from xml.etree.ElementInclude import include
from django.urls import path, include
from example_app.views import index

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('katalog/', include('katalog.urls')),
]