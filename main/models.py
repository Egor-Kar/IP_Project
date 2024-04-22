from datetime import datetime, timedelta

import psycopg2
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from main.managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin

from main.profle import Profile


class MyUser(AbstractUser):
    username = models.CharField(
        'Никнейм', max_length=20, unique=True, null=True, blank=True
    )
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    score = models.IntegerField(name="score", default=0, blank=True)
    count_play = models.IntegerField('count_play', default=0, blank=True, null=True)
    hit1 = models.IntegerField('1_try', default=0, blank=True)
    hit2 = models.IntegerField('2_try', default=0, blank=True)
    hit3 = models.IntegerField('3_try', default=0, blank=True)
    hit4 = models.IntegerField('4_try', default=0, blank=True)
    hit5 = models.IntegerField('5_try', default=0, blank=True)
    hit6 = models.IntegerField('6_try', default=0, blank=True)
    hit7 = models.IntegerField('7_try', default=0, blank=True)
    hit8 = models.IntegerField('8_try', default=0, blank=True)
    hit9 = models.IntegerField('9_try', default=0, blank=True)
    hit10 = models.IntegerField('10_try', default=0, blank=True)
    hit11 = models.IntegerField('11_try', default=0, blank=True)
    hit12 = models.IntegerField('12_try', default=0, blank=True)
    hit13 = models.IntegerField('13_try', default=0, blank=True)
    hit14 = models.IntegerField('14_try', default=0, blank=True)
    hit15 = models.IntegerField('15_try', default=0, blank=True)
    hit16 = models.IntegerField('16_try', default=0, blank=True)
    hit17 = models.IntegerField('17_try', default=0, blank=True)
    hit18 = models.IntegerField('18_try', default=0, blank=True)
    hit19 = models.IntegerField('19_try', default=0, blank=True)
    hit20 = models.IntegerField('20_try', default=0, blank=True)
    try_1 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_2 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_3 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_4 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_5 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_6 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_7 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_8 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_9 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_10 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_11 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_12 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_13 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_14 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_15 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_16 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_17 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_18 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_19 = models.CharField(max_length=50, null=True, blank=True, default="")
    try_20 = models.CharField(max_length=50, null=True, blank=True, default="")
    last_score = models.IntegerField(default=0, blank=True)
    last_hit = models.IntegerField(default=0, blank=True)
    last_number = models.IntegerField(default=0, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
