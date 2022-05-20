from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet
from .serializers import UserModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, \
    IsAuthenticatedOrReadOnly, BasePermission, DjangoModelPermissions
from .models import User
from rest_framework.viewsets import ModelViewSet


class UserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]  # обязателен
    queryset = User.objects.all()  # обязателен
    serializer_class = UserModelSerializer  # обязателен
 #   permission_classes = IsAuthenticated   # только у авторизованных
#   authentication_classes = TokenAuthentication
#   данные по записи можно получать только при авторизации по токенам


# permission_classes = DjangoModelPermissions


#    Simple JWT
#   pagination_class = UserLimitOffsetPagination


#
# class ModelViewSet(mixins.CreateModelMixin,       создать
#                    mixins.RetrieveModelMixin,     забрать
#                    mixins.UpdateModelMixin,       изменить
#                    mixins.DestroyModelMixin,      удалить
#                    mixins.ListModelMixin,         смотреть
#                    GenericViewSet):
