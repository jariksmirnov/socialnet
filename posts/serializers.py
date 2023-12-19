from . models import Post
from rest_framework import serializers
from votes.serializers import VoteSerializer


class PostSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'post_image',
                  'created_at', 'votes']
