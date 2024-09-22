from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Reviews, Feedback, BlogNews
from .serializers import ReviewsSerializers, FeedbackSerializers, BlogNewsSerializer


class ReviewsView(APIView):

    # GET запрос для получения всех отзывов или одного отзыва по id
    def get(self, request, pk=None):
        if pk:
            review = get_object_or_404(Reviews, pk=pk)
            serializer = ReviewsSerializers(review)
        else:
            reviews = Reviews.objects.all()
            serializer = ReviewsSerializers(reviews, many=True)
        return Response(serializer.data)

    # POST запрос для создания нового отзыва
    def post(self, request):
        serializer = ReviewsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT запрос для обновления отзыва по id
    def put(self, request, pk=None):
        review = get_object_or_404(Reviews, pk=pk)
        serializer = ReviewsSerializers(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(APIView):
    # GET запрос для получения всех записей обратной связи или одной записи по id
    def get(self, request, pk=None):
        if pk:
            feedback = get_object_or_404(Feedback, pk=pk)
            serializer = FeedbackSerializers(feedback)
        else:
            feedback = Feedback.objects.all()
            serializer = FeedbackSerializers(feedback, many=True)
        return Response(serializer.data)

    # POST запрос для создания новой записи обратной связи
    def post(self, request):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT запрос для обновления записи обратной связи по id
    def put(self, request, pk=None):
        feedback = get_object_or_404(Feedback, pk=pk)
        serializer = FeedbackSerializers(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogNewsView(APIView):

    def get(self, request):
        blog_news = BlogNews.objects.all().order_by('-date')  # Сначала новые
        serializer = BlogNewsSerializer(blog_news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogNewsDetailView(APIView):

    def put(self, request, pk):
        blog_news = get_object_or_404(BlogNews, pk=pk)
        serializer = BlogNewsSerializer(blog_news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
# from .models import Reviews, News, Feedback, BlogNews
# from .serializers import ReviewsSerializers, NewsSerializers, FeedbackSerializers, BlogNewsSerializer
#
#
# class ReviewsView(APIView):
#
#     def get(self, request, pk=None):
#         if pk:
#             review = get_object_or_404(Reviews, pk=pk)
#             serializer = ReviewsSerializers(review)
#             return Response(serializer.data)
#         else:
#             reviews = Reviews.objects.all()
#             # Преобразуем список в словарь
#             review_data = {review.id: ReviewsSerializers(review).data for review in reviews}
#             return Response(review_data)
#
#     def post(self, request):
#         serializer = ReviewsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         review = get_object_or_404(Reviews, pk=pk)
#         serializer = ReviewsSerializers(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class FeedbackView(APIView):
#
#     def get(self, request, pk=None):
#         if pk:
#             feedback = get_object_or_404(Feedback, pk=pk)
#             serializer = FeedbackSerializers(feedback)
#             return Response(serializer.data)
#         else:
#             feedback = Feedback.objects.all()
#             # Преобразуем список в словарь
#             feedback_data = {item.id: FeedbackSerializers(item).data for item in feedback}
#             return Response(feedback_data)
#
#     def post(self, request):
#         serializer = FeedbackSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         feedback = get_object_or_404(Feedback, pk=pk)
#         serializer = FeedbackSerializers(feedback, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BlogNewsView(APIView):
#
#     def get(self, request):
#         blog_news = BlogNews.objects.all().order_by('-date')
#         # Преобразуем список в словарь
#         blog_news_data = {item.id: BlogNewsSerializer(item).data for item in blog_news}
#         return Response(blog_news_data)
#
#     def post(self, request):
#         serializer = BlogNewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BlogNewsDetailView(APIView):
#
#     def put(self, request, pk):
#         blog_news = get_object_or_404(BlogNews, pk=pk)
#         serializer = BlogNewsSerializer(blog_news, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
