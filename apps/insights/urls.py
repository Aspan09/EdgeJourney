from django.urls import path
from .views import ReviewsView, FeedbackView, BlogNewsView, BlogNewsDetailView

urlpatterns = [

    # Reviews URLs
    path('api/v1/reviews/', ReviewsView.as_view(), name='reviews-list'),  # GET all reviews, POST a new review
    path('api/v1/reviews/<int:pk>/', ReviewsView.as_view(), name='reviews-detail'),  # GET, PUT a review by id

    # Feedback URLs
    path('api/v2/feedback/', FeedbackView.as_view(), name='feedback-list'),  # GET all feedback, POST a new feedback
    path('api/v2/feedback/<int:pk>/', FeedbackView.as_view(), name='feedback-detail'),  # GET, PUT feedback by id

    # BlockNews URLs
    path('api/v3/blog-news/', BlogNewsView.as_view(), name='blog-news-list'),
    path('api/v3/blog-news/<int:pk>/', BlogNewsDetailView.as_view(), name='blog-news-detail'),
]
