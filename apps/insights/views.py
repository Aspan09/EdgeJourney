from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import (Reviews, Feedback, BlogNews, CustomUser, Task, SubRole, Role, Group, GroupMember, TestResult)
from .serializers import (ReviewsSerializers, FeedbackSerializers, BlogNewsSerializer, RegistrationSerializer,
                          LoginSerializer, TaskSerializer, SubRoleSerializers, RoleSerializers, GroupSerializers,
                          GroupMemberSerializers, TestResultSerializers)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = RegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubRoleView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        sub_role = SubRole.objects.all()
        serializers = SubRoleSerializers(sub_role, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = SubRoleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        sub_role = SubRole.objects.get(pk=pk)
        serializer = SubRoleSerializers(sub_role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sub_role = SubRole.objects.get(pk=pk)
        sub_role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializers(role, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        role = Role.objects.get(pk=pk)
        serializer = RoleSerializers(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status)

    def delete(self, request, pk):
        role = Role.objects.get(pk=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        group = Group.objects.all()
        serializer = GroupSerializers(group, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GroupSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializers(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupMemberView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        group_member = GroupMember.objects.all()
        serializer = GroupMemberSerializers(group_member, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GroupMemberSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        group_member = GroupMember.objects.get(pk=pk)
        serializer = GroupMemberSerializers(group_member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        group_member = GroupMember.objects.get(pk=pk)
        group_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TestResultView(APIView):
    permission_classes = [IsAuthenticated]  # Проверка на аутентификацию

    def get(self, request, pk=None):
        # Получение одного или всех результатов
        if pk:
            test_result = get_object_or_404(TestResult, pk=pk)
            serializer = TestResultSerializers(test_result)
            return Response(serializer.data)
        else:
            test_results = TestResult.objects.all()
            serializer = TestResultSerializers(test_results, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Создание нового тестового результата
        serializer = TestResultSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(submitted_by=request.user)  # Устанавливаем `submitted_by` автоматически
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Обновление существующего результата
        test_result = get_object_or_404(TestResult, pk=pk)
        if test_result.submitted_by != request.user:
            return Response({'error': 'You do not have permission to edit this result.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = TestResultSerializers(test_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        # Удаление результата
        test_result = get_object_or_404(TestResult, pk=pk)
        if test_result.submitted_by != request.user:
            return Response({'error': 'You do not have permission to delete this result.'},
                            status=status.HTTP_403_FORBIDDEN)

        test_result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        # Вернуть только данные без метаданных пагинации
        return Response(data)


class ReviewsView(APIView):
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            review = get_object_or_404(Reviews, pk=pk)
            serializer = ReviewsSerializers(review)
            return Response(serializer.data)
        else:
            reviews = Reviews.objects.all()
            paginator = self.pagination_class()
            paginated_reviews = paginator.paginate_queryset(reviews, request)
            serializer = ReviewsSerializers(paginated_reviews, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ReviewsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        review = get_object_or_404(Reviews, pk=pk)
        serializer = ReviewsSerializers(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackView(APIView):
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            feedback = get_object_or_404(Feedback, pk=pk)
            serializer = FeedbackSerializers(feedback)
            return Response(serializer.data)
        else:
            feedback = Feedback.objects.all()
            paginator = self.pagination_class()
            paginated_feedback = paginator.paginate_queryset(feedback, request)
            serializer = FeedbackSerializers(paginated_feedback, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        feedback = get_object_or_404(Feedback, pk=pk)
        serializer = FeedbackSerializers(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogNewsView(APIView):
    pagination_class = CustomPagination

    def get(self, request):
        blog_news = BlogNews.objects.all().order_by('-date')
        paginator = self.pagination_class()
        paginated_blog_news = paginator.paginate_queryset(blog_news, request)
        serializer = BlogNewsSerializer(paginated_blog_news, many=True)
        return paginator.get_paginated_response(serializer.data)

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

