from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(verbose_name="Дата создания аккаунта", auto_now_add=True)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Reviews(models.Model):
    user_name = models.CharField(verbose_name='Имя пользователя', max_length=255)
    city = models.CharField(verbose_name='Город', max_length=255)
    message_ru = models.TextField(verbose_name='Сообщение на рус', blank=True, null=True)
    message_kz = models.TextField(verbose_name='Сообщение на каз', blank=True, null=True)
    message_en = models.TextField(verbose_name='Сообщение на англ', blank=True, null=True)
    user_avatar = models.ImageField(verbose_name='Аватарка пользователя', upload_to='resource', blank=True, null=True)
    grade = models.IntegerField(verbose_name='Оценка(звезды)')
    created_at = models.DateTimeField(verbose_name="Дата создания сообщения", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Feedback(models.Model):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20)
    user_name = models.CharField(verbose_name='Имя', max_length=255)
    question = models.TextField(verbose_name='Вопрос')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"


class BlogNews(models.Model):
    title_ru = models.CharField(max_length=255, verbose_name="Заголовок на рус", blank=True, null=True)
    title_kz = models.CharField(max_length=255, verbose_name="Заголовок на каз", blank=True, null=True)
    title_en = models.CharField(max_length=255, verbose_name="Заголовок на англ", blank=True, null=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='resource', blank=True, null=True)
    description_ru = models.TextField(verbose_name='Описание на рус', blank=True, null=True)
    description_kz = models.TextField(verbose_name='Описание на каз', blank=True, null=True)
    description_en = models.TextField(verbose_name='Описание на англ', blank=True, null=True)

    date = models.DateTimeField(verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог и новости"
        verbose_name_plural = "Блог и новости"
        ordering = ['-date']  # Сортировка по дате от новых к старым

