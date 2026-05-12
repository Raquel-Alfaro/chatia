from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conversation/new/', views.create_conversation, name='create_conversation'),
    path('chat/<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
    path('rename/<int:conversation_id>/', views.rename_conversation, name='rename_conversation'),
    path('delete/<int:conversation_id>/', views.delete_conversation, name='delete_conversation'),
    path('profile/', views.profile, name='profile'),
    path('help/', views.help_page, name='help'),
]