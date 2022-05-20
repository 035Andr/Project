import graphene
from graphene_django import DjangoObjectType
from todos.models import Todo, Project
from users.models import User


# несколько моделей
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todos = graphene.List(TodoType)
    all_projects = graphene.List(ProjectType)
    todo_by_user_name = graphene.List(TodoType, first_name=graphene.String(
        required=False))

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_todo_by_user_name(self, info, first_name=None):
        todo = Todo.objects.all()
        if first_name:
            todo = todo.filter(user__first_name=first_name)
        return todo


schema = graphene.Schema(query=Query)


"""
class UserType(DjangoObjectType):     #  одна модель
    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()
"""
