from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message, Profile
from dotenv import load_dotenv

import requests
import os

# Create your views here.
load_dotenv()

def help_page(request):
    return render(request, "chat/help.html")

@login_required     # Solo puede entrar alguien autenticado
def home(request):
    # Con esto vamos a coger solo la conversacion del usuario autenticado
    conversations = Conversation.objects.filter(user = request.user)
    return render(
        request,
        'chat/home.html',
        {'conversations': conversations}
    )

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method=="POST":
        profile.alias=request.POST["alias"]
        profile.theme=request.POST["theme"]
        profile.save()
        return redirect("home")

    return render(request, "chat/profile.html", {"profile":profile})

@login_required
def create_conversation(request):
    conversation = Conversation.objects.create(user=request.user, title='Nueva conversación')
    return redirect('conversation_detail', conversation_id=conversation.id)

@login_required
def conversation_detail(request, conversation_id):
    conversation = Conversation.objects.get(
        id=conversation_id,
        user=request.user
    )

    if request.method=='POST':
        content = request.POST.get('content')
        if content:
            # Poner nombre a la nueva conversacion
            if conversation.title=='Nueva conversación':
                conversation.title=content[:30]
                conversation.save()

            # MENSAJE USUARIO
            Message.objects.create(conversation=conversation, role='user', content=content)
            assistant_response = ask_llm(content)   # Llama a la IA
            # MENSAJE IA
            Message.objects.create(conversation=conversation, role='assistant', content=assistant_response)
    messages = Message.objects.filter(conversation=conversation).order_by('created_at')

    if request.headers.get('HX-Request'):
        return render(request, 'chat/messages.html', {'messages':messages})
    return render(
        request,
        'chat/conversation_detail.html',
        {'conversation': conversation, 'messages': messages}
    )

def ask_llm(prompt):
    api_key = os.getenv('OPENROUTER_API_KEY')

    response = requests.post(url='https://openrouter.ai/api/v1/chat/completions',
                           headers={
                               'Authorization':f'Bearer {api_key}',
                               'Content-Type':'application/json'},
                           json={
                               'model':'openrouter/free',
                               'messages':[{
                                     'role': 'user',
                                     'content': prompt
                                 }]
                           })

    try:
        data = response.json()
        return data['choices'][0]['message']['content']
    except:
        return "Error al contactar con la IA"

@login_required
def rename_conversation(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id, user=request.user)
    if request.method == 'POST':
        new_title = request.POST.get('title')

        if new_title:
            conversation.title = new_title
            conversation.save()
        return redirect('/')

    return render(request, 'chat/rename_conversation.html', {'conversation': conversation})

@login_required
def delete_conversation(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id, user=request.user)
    conversation.delete()
    return redirect('/')