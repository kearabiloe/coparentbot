from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import MultiAuthentication,SessionAuthentication, Authentication, BasicAuthentication,ApiKeyAuthentication
from tastypie.authorization import Authorization,DjangoAuthorization
from tastypie.serializers import Serializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from .models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password']

class ParentResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', null=True, full=True)
    class Meta:
        queryset = Parent.objects.all()
        resource_name = 'parent'

class ParentingPlanResource(ModelResource):
    parent1 = fields.ForeignKey(ParentResource, 'parent1',null=True, full=True)
    parent2 = fields.ForeignKey(ParentResource, 'parent2',null=True, full=True)
    class Meta:
        queryset = ParentingPlan.objects.all()
        resource_name = 'parenting_plan'

class VisitationResource(ModelResource):
    class Meta:
        queryset = Visitation.objects.all()
        resource_name = 'visitation'

class ChangeRequestResource(ModelResource):
    class Meta:
        queryset = ChangeRequest.objects.all()
        resource_name = 'change_request'

class ConversationResource(ModelResource):
    parenting_plan = fields.ForeignKey(ParentingPlanResource, 'parenting_plan',null=True, full=False)
    parent = fields.ForeignKey(ParentResource, 'parent',null=True, full=False)
    intended_parent = fields.ForeignKey(ParentResource, 'intended_parent',null=True, full=False)

    class Meta:
        queryset = Conversation.objects.all()
        resource_name = 'conversation'
        allowed_methods = ['get','post','patch','put']
        authentication = MultiAuthentication(ApiKeyAuthentication(),BasicAuthentication())
        authorization = Authorization()        
        always_return_data=True

class ConflictScoreResource(ModelResource):
    class Meta:
        queryset = ConflictScore.objects.all()
        resource_name = 'conflict_score'

class DemeritPointResource(ModelResource):
    class Meta:
        queryset = DemeritPoint.objects.all()
        resource_name = 'demerit_point'