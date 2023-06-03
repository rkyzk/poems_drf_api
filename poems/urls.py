from django.urls import path
from poems import views

urlpatterns = [
    path('poems/', views.PoemList.as_view()),
    path('poems/<int:pk>', views.PoemDetail.as_view()),
]