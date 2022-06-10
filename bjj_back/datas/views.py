from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Video
from .serializers import VideoSerializer, VideoCommentSerializer

skills = [
    'armbar', '암바',
    'triangle choke', 'triangleChoke', '트라이앵글',
    'choke', '초크',
    'loop choke', 'loopchoke', '루프',
    'knee bar', 'kneebar', '니바',
    'choi bar', 'choibar', '초이바',
    'omoplata', '오모플라타',
    'berimbolo', '베림보로', '베림볼로',
    ]

guards = [
    'lasso', '라쏘',
    'half', '하프',
    'xguard', 'x guard', '엑스',
    'single x', 'singlex', '싱글 엑스', '싱글엑스',
    'closed', '클로즈', '클로즈드',
    'butter fly', 'butterfly', '버터플라이',
    'spider', '스파이더',
    'delariva', 'de la riva', '데라히바',
    'rubber', '러버',
    'turtle', '터틀',
    'lapel', '라펠',
    'worm', '웜',
]

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
        
        inskill = []
        inguard = []

        for skill in skills:
            if skill in datas[idx]['snippet']['title'].lower() or skill in datas[idx]['snippet']['description'].lower():
                inskill.append(skill)
        
        for guard in guards:
            if guard in datas[idx]['snippet']['title'].lower() or guard in datas[idx]['snippet']['description'].lower():
                inguard.append(guard)

        video.objects.create(
            title = datas[idx]['snippet']['title'],
            url = 'https://www.youtube.com/watch?v=' + datas[idx]['id']['videoId'],
            thumbnail = datas[idx]['snippet']['thumbnails']['high']['url'],
            description = datas[idx]['snippet']['description'],
            channel = datas[idx]['snippet']['channelTitle'],
        )

        if inskill:
            video_update = video.objects.get(title=datas[idx]['snippet']['title'])
            video_update.skill_name = ' '.join(inskill)
            video_update.save()

        if inguard:
            video_update = video.objects.get(title=datas[idx]['snippet']['title'])
            video_update.guard_name = ' '.join(inguard)
            video_update.save()
        

    return Response({'status': 'success'})

@api_view(['GET'])
def send_video_list(request):
    video = Video.objects.filter(black = 0)
    serializer = VideoSerializer(video, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, video_pk):
    video = get_object_or_404(Video, pk=video_pk)
    serializer = VideoCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(video=video)
        comments = video.videocomments.all()
        serializer = VideoCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)