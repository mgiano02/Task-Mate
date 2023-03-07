from django.urls import path
from projects.views import show_project_list, project_details, create_project

urlpatterns = [
    path("", show_project_list, name="list_projects"),
    path("<int:id>/", project_details, name="show_project"),
    path("create/", create_project, name="create_project"),
]
