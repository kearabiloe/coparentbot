from django.db import models
from django.contrib.auth.models import User


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class ParentingPlan(models.Model):
    parent1 = models.ForeignKey(Parent, blank=True, null=True, on_delete=models.CASCADE, related_name='parent1_plans')
    parent2 = models.ForeignKey(Parent, blank=True, null=True, on_delete=models.CASCADE, related_name='parent2_plans')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s and %s" %(self.parent1, self.parent2)

class Visitation(models.Model):
    parenting_plan = models.ForeignKey(ParentingPlan, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    notes = models.TextField(blank=True)

class ChangeRequest(models.Model):
    parenting_plan = models.ForeignKey(ParentingPlan, on_delete=models.CASCADE, blank=True, null=True)
    requesting_parent = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending')


class ConflictScore(models.Model):
    parenting_plan = models.ForeignKey(ParentingPlan, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

class DemeritPoint(models.Model):
    parenting_plan = models.ForeignKey(ParentingPlan, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_points', blank=True, null=True)
    points = models.IntegerField(default=0)
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    parenting_plan = models.ForeignKey(ParentingPlan, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    moderator_response = models.TextField(blank=True)
    intended_parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='intended_messages', blank=True, null=True)

def signals_import():
    """ A note on signals.
    The signals need to be imported early on so that they get registered
    by the application. Putting the signals here makes sure of this since
    the models package gets imported on the application startup.
    """
    from tastypie.models import create_api_key

    models.signals.post_save.connect(create_api_key, sender=User)
     
signals_import()