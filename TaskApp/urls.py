from django.urls import path, include
from .views import TaskView, AssignTaskView, AssigneeTaskView
from rest_framework.routers import DefaultRouter

# router for simpler CRUD for tasks
router = DefaultRouter()
router.register(r'tasks', TaskView, basename='task')  

urlpatterns = [
    path('', include(router.urls)),
    path('assign/<int:id>', AssignTaskView.as_view(), name='assign task'),
    path('by_assignee/<int:id>', AssigneeTaskView.as_view(), name='view task'),
]