from django.contrib import admin
from .models import Reviews, Feedback, BlogNews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'city', 'message_ru', 'grade', 'created_at')
    search_fields = ('user_name', 'city')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'created_at')
    search_fields = ('user_name', 'phone_number')


@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'description_ru', 'date')
    search_fields = ('title_ru', 'date')
