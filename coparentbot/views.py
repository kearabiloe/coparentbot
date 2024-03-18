from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ParentingPlan, Visitation, ChangeRequest, Conversation, Parent
from .forms import ParentingPlanForm, VisitationForm, ChangeRequestForm, ConversationForm,ParentMessageForm
from anthropic import Anthropic


anthropic = Anthropic()

def parenting_plan(request):
    if request.method == 'POST':
        form = ParentingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coparentbot:parenting_plan')
    else:
        form = ParentingPlanForm()
    
    parenting_plans = ParentingPlan.objects.all()
    return render(request, 'coparentbot/parenting_plan.html', {'form': form, 'parenting_plans': parenting_plans})

def visitation(request):
    if request.method == 'POST':
        form = VisitationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coparentbot:visitation')
    else:
        form = VisitationForm()
    
    visitations = Visitation.objects.all()
    return render(request, 'coparentbot/visitation.html', {'form': form, 'visitations': visitations})

def change_request(request):
    if request.method == 'POST':
        form = ChangeRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coparentbot:change_request')
    else:
        form = ChangeRequestForm()
    
    change_requests = ChangeRequest.objects.all()
    return render(request, 'coparentbot/change_request.html', {'form': form, 'change_requests': change_requests})

def conversation(request):
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coparentbot:conversation')
    else:
        form = ConversationForm()
    
    conversations = Conversation.objects.all()
    return render(request, 'coparentbot/conversation.html', {'form': form, 'conversations': conversations})

@login_required
def whatsapp_demo(request):
    parent_a_form = ParentMessageForm(prefix='parent_a')
    parent_b_form = ParentMessageForm(prefix='parent_b')
    parenting_plan_form = ParentingPlanForm()
    parenting_plans = ParentingPlan.objects.all()

    selected_plan_id = request.GET.get('plan_id')
    if selected_plan_id:
        selected_plan = ParentingPlan.objects.get(id=selected_plan_id)
        conversation = Conversation.objects.filter(parenting_plan=selected_plan).order_by('timestamp')
    else:
        selected_plan = None
        conversation = []

    if request.method == 'POST':
        if 'parent_a_message' in request.POST:
            parent_a_form = ParentMessageForm(request.POST, prefix='parent_a')
            if parent_a_form.is_valid() and selected_plan:
                message = parent_a_form.cleaned_data['message']
                Conversation.objects.create(parenting_plan=selected_plan, parent=selected_plan.parent1, message=message)
        elif 'parent_b_message' in request.POST:
            parent_b_form = ParentMessageForm(request.POST, prefix='parent_b')
            if parent_b_form.is_valid() and selected_plan:
                message = parent_b_form.cleaned_data['message']
                Conversation.objects.create(parenting_plan=selected_plan, parent=selected_plan.parent2, message=message)
        elif 'parenting_plan_form' in request.POST:
            parenting_plan_form = ParentingPlanForm(request.POST)
            if parenting_plan_form.is_valid():
                parenting_plan_form.save()

        if selected_plan:
            conversation = Conversation.objects.filter(parenting_plan=selected_plan).order_by('timestamp')
            moderated_response = moderate_conversation(conversation)
            if moderated_response:
                intended_parent = moderated_response['intended_parent']
                moderator_message = moderated_response['message']
                Conversation.objects.create(
                    parenting_plan=selected_plan,
                    parent=None,
                    message=moderator_message,
                    moderator_response=moderator_message,
                    intended_parent=intended_parent
                )

    context = {
        'parent_a_form': parent_a_form,
        'parent_b_form': parent_b_form,
        'parenting_plan_form': parenting_plan_form,
        'parenting_plans': parenting_plans,
        'selected_plan': selected_plan,
        'conversation': conversation,
    }
    return render(request, 'coparentbot/whatsapp_demo.html', context)

def moderate_conversation(conversation):
    conversation_history = [
        f"{message.parent.user.username if message.parent else 'Moderator'}: {message.message}" for message in conversation
    ]
    system_prompt = "You are a conversation moderator for co-parenting. Analyze the conversation and provide a response to help the parents communicate effectively."
    human_prompt = "\n\nHuman: " + "\n".join(conversation_history)
    prompt = system_prompt + human_prompt + "\n\nAssistant:"
    response = anthropic.completions.create(
        prompt=prompt,
        max_tokens_to_sample=150,
        model='claude-v1',
    )
    moderated_response = response.completion.strip()
    # Extract the intended parent from the moderated response
    intended_parent = None
    if 'Parent A' in moderated_response:
        intended_parent = conversation[0].parenting_plan.parent1
    elif 'Parent B' in moderated_response:
        intended_parent = conversation[0].parenting_plan.parent2
    return {'message': moderated_response, 'intended_parent': intended_parent}