from django.urls import path
from .views import CreateTaskView, AssignTaskView

urlpatterns = [
    path('create', CreateTaskView.as_view(), name='task view'),
    path('assign/<int:id>', AssignTaskView.as_view(), name='assign task')

]