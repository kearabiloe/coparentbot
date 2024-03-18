# coparentbot/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import ParentingPlan, Visitation, ChangeRequest, Conversation

class ParentingPlanForm(forms.ModelForm):
    class Meta:
        model = ParentingPlan
        fields = ['parent1', 'parent2', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'parent1',
            'parent2',
            'start_date',
            'end_date',
            Submit('submit', 'Save')
        )

class VisitationForm(forms.ModelForm):
    class Meta:
        model = Visitation
        fields = ['parenting_plan', 'parent', 'start_datetime', 'end_datetime', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'parenting_plan',
            'parent',
            'start_datetime',
            'end_datetime',
            'notes',
            Submit('submit', 'Save')
        )

class ChangeRequestForm(forms.ModelForm):
    class Meta:
        model = ChangeRequest
        fields = ['parenting_plan', 'requesting_parent', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'parenting_plan',
            'requesting_parent',
            'description',
            Submit('submit', 'Save')
        )

class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['parenting_plan', 'parent', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'parenting_plan',
            'parent',
            'message',
            Submit('submit', 'Save')
        )



class ParentMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
        'message',
        Submit('submit', 'Send')
        )

