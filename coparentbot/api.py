from tastypie.resources import ModelResource
from .models import ParentingPlan, Visitation, ChangeRequest, Conversation, ConflictScore, DemeritPoint

class ParentingPlanResource(ModelResource):
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
    class Meta:
        queryset = Conversation.objects.all()
        resource_name = 'conversation'

class ConflictScoreResource(ModelResource):
    class Meta:
        queryset = ConflictScore.objects.all()
        resource_name = 'conflict_score'

class DemeritPointResource(ModelResource):
    class Meta:
        queryset = DemeritPoint.objects.all()
        resource_name = 'demerit_point'