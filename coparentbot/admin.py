from django.contrib import admin
from .models import ParentingPlan, Visitation, ChangeRequest, Conversation, Parent

@admin.register(ParentingPlan)
class ParentingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent1', 'parent2', 'start_date', 'end_date')
    search_fields = ('parent1', 'parent2')
    list_filter = ('start_date', 'end_date')

@admin.register(Visitation)
class VisitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'parenting_plan', 'parent', 'start_datetime', 'end_datetime')
    search_fields = ('parent',)
    list_filter = ('parenting_plan', 'start_datetime', 'end_datetime')

@admin.register(ChangeRequest)
class ChangeRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'parenting_plan', 'requesting_parent', 'status')
    search_fields = ('requesting_parent',)
    list_filter = ('parenting_plan', 'status')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'parenting_plan', 'parent', 'timestamp')
    search_fields = ('parent', 'message')
    list_filter = ('parenting_plan', 'timestamp')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)