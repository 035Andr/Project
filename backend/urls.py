"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views
#from rest_framework_simplejwt.views import TokenObtainPairView, \
 #   TokenRefreshView, TokenVerifyView

from users.views import UserModelViewSet
from todos.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls')),   # log in
    path('api-auth-token/', views.obtain_auth_token),

]






#  Тестовое занятие
 #   path('jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('jwt-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 #   path('jwt-token-verify/', TokenVerifyView.as_view(), name='token_verify'),

#  jwt-token/  авторизация
#  jwt-token-refresh/  обновление
#  jwt-token-verify/ проверка подписи

