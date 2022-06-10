from re import A
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Video
from .serializers import VideoSerializer

@api_view(['GET'])
def get_video(request, query):
    video = Video

    api_key = 'AIzaSyDr2zDTj9xwb8LtUJXOtMsC4NbwzL5YiJo'
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&maxResults=100'

    response = requests.get(url).json()
    datas = response['items']

    for idx in range(len(datas)):

        if video.objects.filter(url = 'https://www.youtube.com/watch?v=' + datas[idx]['id']['videoId']).exists():
            continue

        video.objects.create(
        title =  datas[idx]['snippet']['title'],
        url = 'https://www.youtube.com/watch?v=' + datas[idx]['id']['videoId'],
        thumbnail = datas[idx]['snippet']['thumbnails']['high']['url'],
        description = datas[idx]['snippet']['description'],
        channel = datas[idx]['snippet']['channelTitle'],
        )

    return Response({'status': 'success'})

@api_view(['GET'])
def send_video_list(request):
    video = Video.objects.filter(black = 0)
    serializer = VideoSerializer(video, many=True)

    return Response(serializer.data)