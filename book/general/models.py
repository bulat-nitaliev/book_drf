from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    ROLE_CHOICES = (
        ('librarian', 'Librarian'),
        ('reader', 'Reader'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')
    employee_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
    )

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    using_the_book = models.BooleanField(default=False)

    def __str__(self):
        return self.title
