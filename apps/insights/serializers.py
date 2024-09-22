from rest_framework import serializers
from .models import Reviews, Feedback, BlogNews


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'user_name', 'city', 'message_ru', 'message_kz', 'message_en',
                  'user_avatar', 'grade', 'created_at', 'updated_at']


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'phone_number', 'user_name', 'question', 'created_at', 'updated_at']


class BlogNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogNews
        fields = ['id', 'title_ru', 'title_kz', 'title_en', 'image',
                  'description_ru', 'description_kz', 'description_en', 'date']
