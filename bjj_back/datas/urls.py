from django.urls import path
from . import views

app_name = 'datas'

urlpatterns = [
    path('get/<str:query>', views.get_video),
    path('list', views.send_video_list),

    path('<int:video_pk>/comments', views.create_comment)
]
