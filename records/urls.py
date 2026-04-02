from django.urls import path
from .views import RecordListCreateView, RecordDetailView

urlpatterns = [
    path('records/', RecordListCreateView.as_view()),
    path('records/<int:pk>/', RecordDetailView.as_view()),
]