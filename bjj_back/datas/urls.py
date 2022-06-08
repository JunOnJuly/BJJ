from django.urls import path
from . import views

app_name = 'datas'

urlpatterns = [
    path('<str:query>', views.get_video),
]
