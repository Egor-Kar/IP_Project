from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('game/', views.game, name='game'),
    path('secret_game/', views.game_secret, name='sec_game'),
    path('data_form_secret/', views.data_form_secret, name='data_sec'),
    path('data_form/', views.data_form, name='data'),
    path('profile/', views.profile, name='profile'),
    path('rules/', views.rules, name='rules'),
    path('statistica/', views.statistika, name='statistica'),
    path('table_stat/', views.stat_table, name='table'),
]
