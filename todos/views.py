from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer

"""
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
"""


class ProjectModelViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                          UpdateModelMixin, DestroyModelMixin,
                          GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


#    pagination_class = ProjectLimitOffsetPagination


class TodoModelViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                       UpdateModelMixin, DestroyModelMixin,
                       GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


#    pagination_class = TodoLimitOffsetPagination


def perform_destoy(instance):
    instance.is_deleted = True
    instance.save()
