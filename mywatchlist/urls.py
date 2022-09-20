from django.urls import path
from mywatchlist.views import show_xml, show_json,show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_html, name='show_html'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
]

