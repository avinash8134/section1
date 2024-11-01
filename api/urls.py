from django.urls import path
from task.views import listview


urlpatterns = [
    path('listview/',listview,name="list"),
]
