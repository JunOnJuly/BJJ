from django.urls import path
from . import views

app_name = 'datas'

urlpatterns = [
    path('video/<str:query>', views.get_video),
    path('list', views.send_video_list),
]
