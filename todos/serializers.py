from todos.models import Project, Todo
from rest_framework.serializers import ModelSerializer


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
