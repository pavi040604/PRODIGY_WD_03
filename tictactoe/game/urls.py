from django.urls import path
from .views import index, two_player, ai, get_ai_move

urlpatterns = [
    path('', index, name='index'),
    path('two_player/', two_player, name='two_player'),
    path('ai/', ai, name='ai'),
    path('get_ai_move/', get_ai_move, name='get_ai_move'),
]

