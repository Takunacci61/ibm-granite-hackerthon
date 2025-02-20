from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectTasksAPIView

# Create a router for automatic URL mapping
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # This will create /api/projects/ endpoints
    path('api/project/<int:project_id>/tasks/', ProjectTasksAPIView.as_view(), name='get_project_tasks'),
]
