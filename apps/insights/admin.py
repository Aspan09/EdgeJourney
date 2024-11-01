from django.contrib import admin
from .models import (Reviews, Feedback, BlogNews, CustomUser, SubRole, Role, Task, Group, GroupMember, TestResult)


@admin.register(SubRole)
class SubRoleAdmin(admin.ModelAdmin):
    list_display = ('sub_role_name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'sub_role', 'privileges')
    search_fields = ('role_name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'status', 'assigned_by', 'assigned_to', 'group_assigned_to',
                    'created_at', 'updated_at')
    search_fields = ('status', 'assigned_by', 'created_at')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'curator')


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('group', 'student')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test_date', 'score', 'remarks', 'submitted_by')
    search_fields = ('test_date', 'score')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'about_me', 'role', 'created_at', 'is_staff',)
    search_fields = ('created_at', 'is_staff', 'role')


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
