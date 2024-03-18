from django.urls import path
from . import views

app_name = 'coparentbot'

urlpatterns = [
    path('', views.whatsapp_demo, name='whatsapp_demo'),
    path('parenting-plan/', views.parenting_plan, name='parenting_plan'),
    path('visitation/', views.visitation, name='visitation'),
    path('change-request/', views.change_request, name='change_request'),
    path('conversation/', views.conversation, name='conversation'),
]