from rest_framework import serializers
from .models import Video, VideoComment

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('black',)

class VideoCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoComment
        fields = '__all__'