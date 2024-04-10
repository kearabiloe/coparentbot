"""coparentbot_web URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from tastypie.api import Api
from coparentbot.api import ParentingPlanResource, VisitationResource, ChangeRequestResource, ConversationResource, ParentResource

v1_api = Api(api_name='v1')
v1_api.register(ParentingPlanResource())
v1_api.register(ParentResource())
v1_api.register(VisitationResource())
v1_api.register(ChangeRequestResource())
v1_api.register(ConversationResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include(v1_api.urls)),
    path('', include('coparentbot.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

