from django.urls import path
from .views import (ReviewsView, FeedbackView, BlogNewsView, BlogNewsDetailView, RegisterView, LoginView, TaskView,
                    SubRoleView, RoleView, GroupView, GroupMemberView, TestResultView)


urlpatterns = [
    # Маршруты для отзывов (Reviews)
    path('api/v1/reviews/', ReviewsView.as_view(), name='reviews-list-create'),
    path('api/v1/reviews/<int:pk>/', ReviewsView.as_view(), name='reviews-detail'),

    # Маршруты для обратной связи (Feedback)
    path('api/v2/feedback/', FeedbackView.as_view(), name='feedback-list-create'),
    path('api/v2/feedback/<int:pk>/', FeedbackView.as_view(), name='feedback-detail'),

    # Маршруты для блога и новостей (BlogNews)
    path('api/v3/blognews/', BlogNewsView.as_view(), name='blognews-list-create'),
    path('api/v3/blognews/<int:pk>/', BlogNewsDetailView.as_view(), name='blognews-detail'),

    # Авторизация и регистрация пользователей
    path('api/v4/register/', RegisterView.as_view(), name='register'),
    path('api/v4/login/', LoginView.as_view(), name='login'),

    # Маршруты для задач
    path('api/v5/tasks/', TaskView.as_view(), name='tasks'),
    path('api/v5/tasks/<int:pk>/', TaskView.as_view(), name='task-detail'),

    # Маршрут для Суб ролей
    path('api/v5/sub_role/', SubRoleView.as_view(), name='sub_role'),
    path('api/v5/sub_role/<int:pk>/', SubRoleView.as_view(), name='sub_role-detail'),

    # Маршрут для Ролей
    path('api/v5/role/', RoleView.as_view(), name='role'),
    path('api/v5/role/<int:pk>/', RoleView.as_view(), name='role-detail'),

    # Мрашрут для Group
    path('api/v5/group/', GroupView.as_view(), name='group'),
    path('api/v5/group/<int:pk>', GroupView.as_view(), name='group-detail'),

    # Маршрут для GroupMember
    path('api/v5/group_member/', GroupMemberView.as_view(), name='group_member'),
    path('api/v5/group_member/<int:pk>/', GroupMemberView.as_view(), name='group_member-detail'),

    # Маршрут для результатов теста TestResultView
    path('api/v5/test_result/', TestResultView.as_view(), name='test_result'),
    path('api/v5/test_result/<int:pk>/', TestResultView.as_view(), name='test_result-detail')

]

