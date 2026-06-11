from django.urls import path
from .views import LibraryListView, LibraryDetailView, LibraryCreateView, LibraryUpdateView, LibraryDeleteView
from . import views

urlpatterns = [
    path('', LibraryListView.as_view(), name = 'library-home'),
    path('<int:pk>/', LibraryDetailView.as_view(), name = 'library-detail'),
    path('/new/', LibraryCreateView.as_view(), name = 'library-create'),
    path('<int:pk>/update/', LibraryUpdateView.as_view(), name = 'library-update'),
    path('<int:pk>/delete/', LibraryDeleteView.as_view(), name = 'library-delete'),  
]