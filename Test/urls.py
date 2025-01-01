"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from API import api_view as aview
from API import views 
from ajax import urls

from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns


# route = routers.DefaultRouter()
# route.register(r'users', aview.UserView)
# route.register(r'groups', aview.GroupView)

snippet_list= views.SnippetViewSet.as_view({
    'get': 'list',
    'pos': 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = aview.UserViewSet.as_view({'get':'list'})
user_detail= aview.UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('route/', include(route.urls)),
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),
    path('snippet/', snippet_list, name='snippet-list'),
    path('snippet/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippet/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path("users/<int:pk>", user_detail, name='user-detail'),

    path('ajax/', include('ajax.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)