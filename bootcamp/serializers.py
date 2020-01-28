from rest_framework import serializers
from .models import Instructor, Post

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    instructor_url = serializers.ModelSerializer.serializer_url_field(
        view_name='instructor_detail'
    )
    class Meta:
        model = Instructor
        fields = ('instructor_url', 'name', 'photo_url', 'immersive', 'school', 'campus', 'posts')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    instructors = serializers.HyperlinkedRelatedField(
        view_name='instructor_detail',
        many=True,
        read_only=True
    )
    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail'
    )
    class Meta:
        model = Post
        fields = ('post_url', 'instructor', 'post', 'date', 'instructors')