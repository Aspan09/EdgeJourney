from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(email, username=username, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class SubRole(models.Model):
    sub_role_name = models.CharField(verbose_name='Название Суб-роли')

    def __str__(self):
        return self.sub_role_name

    class Meta:
        verbose_name = 'Суб роль'
        verbose_name_plural = 'Суб роли'


class Role(models.Model):
    role_name = models.CharField(max_length=255, verbose_name='Название роли', choices=[
        ('Student', 'Студент'),
        ('Teacher', 'Преподаватель'),
        ('Parents', 'Родитель'),
        ('Director', 'Директор'),
        ('Staff', 'Сотрудники')
    ], default='new')
    sub_role = models.ForeignKey(SubRole, on_delete=models.CASCADE, blank=True, null=True)
    privileges = models.JSONField(verbose_name='Привилегии', default=dict, blank=True, null=True)  # Поле для хранения привилегий

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=255, verbose_name='Имя пользователя', blank=True, null=True)
    about_me = models.TextField(verbose_name="Краткая информация о пользователе", blank=True, null=True)
    avatar = models.ImageField(verbose_name="Картинка", upload_to='resource', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, default=None)

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


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи", blank=True, null=True)
    priority = models.IntegerField(verbose_name="Приоритет", default=0)
    status = models.CharField(max_length=50, verbose_name="Статус", choices=[
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
        ('deferred', 'Отложена')
    ], default='new')
    assigned_by = models.ForeignKey(CustomUser, verbose_name='Было сделано кем то',
                                    related_name='tasks_assigned_by', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, verbose_name='Принято кем то',
                                    related_name='tasks_assigned_to', on_delete=models.CASCADE,
                                    null=True, blank=True)
    group_assigned_to = models.ForeignKey(SubRole, verbose_name="Группа назначения",
                                          related_name='tasks_group_assigned_to',
                                          on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Group(models.Model):
    group_name = models.CharField(max_length=255, verbose_name="Название группы")
    curator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Куратор")

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Ученик")

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = "Член группы"
        verbose_name_plural = "Члены группы"
        unique_together = ('group', 'student')


class TestResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Ученик")
    test_date = models.DateTimeField(verbose_name="Дата теста")
    score = models.JSONField(verbose_name="Результаты теста")
    remarks = models.TextField(verbose_name="Комментарии", null=True, blank=True)
    submitted_by = models.ForeignKey(CustomUser, verbose_name='Отправлено кем-то',
                                     related_name='submitted_results', on_delete=models.CASCADE)

    def __str__(self):
        return self.student

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"


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
        return self.title_ru

    class Meta:
        verbose_name = "Блог и новости"
        verbose_name_plural = "Блог и новости"
        ordering = ['-date']  # Сортировка по дате от новых к старым

