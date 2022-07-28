from django.urls import path
from .views import query_big_lotto_by_day, query_big_lotto_by_latest_number, query_two_color_balls_by_latest_number, query_two_color_balls_by_day


app_name = 'data'
urlpatterns = [
    path('big-lotto/<str:day>', query_big_lotto_by_day, name='query_big_lotto_by_day'),
    path('big_lotto/latest/<int:number>', query_big_lotto_by_latest_number, name='query_big_lotto_by_latest_number'),
    path('two_color_balls/<str:day>', query_two_color_balls_by_day, name='query_two_color_balls_by_day'),
    path('two_color_balls/latest/<int:number>', query_two_color_balls_by_latest_number, name='query_two_color_balls_by_latest_number')
]