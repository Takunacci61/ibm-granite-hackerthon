from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating, retrieving, updating, and deleting projects.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        """
        Associates the created project with the logged-in user.
        """
        serializer.save(user=self.request.user)


class ProjectTasksAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access
    """
    API endpoint to retrieve project details along with its assigned tasks.
    """

    def get(self, request, project_id):
        """
        Handles GET request to fetch project details and tasks.

        Args:
            request: HTTP request object.
            project_id (int): The ID of the project.

        Returns:
            Response: JSON response containing project details and assigned tasks.
        """
        # Fetch the project or return 404 if not found
        project = get_object_or_404(Project, id=project_id)

        # Retrieve all tasks assigned to the project
        tasks = project.assignments.all().values(
            'id', 'task', 'team_member_number', 'start_date_time',
            'end_date_time', 'description', 'created_at'
        )

        # Construct the response data
        project_details = {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "team_size": project.team_size,
            "start_date": project.start_date,
            "end_date": project.end_date,
            "country": project.country,
            "budget": project.budget,
            "created_at": project.created_at,
            "tasks": list(tasks)  # Convert queryset to a list of dictionaries
        }

        return Response(project_details, status=status.HTTP_200_OK)
