from rest_framework import serializers
from .models import (Reviews, Feedback, BlogNews, CustomUser, Task, Group, GroupMember, TestResult,
                     SubRole, Role)
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username', ''),
            password=validated_data['password']
        )
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = CustomUser.objects.filter(email=data['email']).first()
        if user and user.check_password(data['password']):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        raise serializers.ValidationError("Invalid credentials")


class SubRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubRole
        fields = ['id', 'sub_role_name']


class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role_name', 'sub_role', 'privileges']


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'curator']


class GroupMemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ['id', 'group', 'student']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TestResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = ['id', 'student', 'test_date', 'score', 'remarks', 'submitted_by']
        read_only_fields = ['submitted_by']  # Автоматически установить `submitted_by` в представлении


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
