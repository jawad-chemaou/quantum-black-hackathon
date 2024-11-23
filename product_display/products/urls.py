from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Associe la vue à la racine de l'application
    path('inscription/', views.inscription_client, name='inscription'),
    path('success/', views.page_success, name='success'),  # Une page de succès temporaire
    path('log-button/', views.log_button_view, name='log_button'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('mistral-chat/', views.mistral_chat, name='mistral_chat'),
    
]

