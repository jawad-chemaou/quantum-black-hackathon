from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from .forms import ClientForm
from products.api.fonctions import *

def product_list(request):
    products = Product.objects.all()[0:10]
    return render(request, 'products/product_list.html', {'products': products})




def inscription_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige vers une page de succès
    else:
        form = ClientForm()
    return render(request, 'products/inscription.html', {'form': form})



def page_success(request):
    return render(request, 'products/success.html')


def log_button_view(request):
    return render(request, 'log_button.html')


def chatbot_view(request):
    return render(request, 'products/chatbot.html')


import os
from django.http import JsonResponse
from mistralai import Mistral

# Configurez votre modèle et clé API
api_key = os.environ.get("MISTRAL_API_KEY")  # Ou remplacez par settings.MISTRAL_API_KEY
model = "mistral-large-latest"
client = Mistral(api_key=api_key)

def mistral_chat(request):
    if request.method == "POST":
        # Récupérez le message utilisateur depuis la requête POST
        user_message = request.POST.get("message", "")
        print(f"Message reçu : {user_message}")  # Log dans le terminal
        
        if not user_message:
            return JsonResponse({"error": "Message utilisateur manquant"}, status=400)

        chunks = generate_chunks(user_message)

        for chunk in chunks:
            print(chunk)
            print("_____________________")


        if "conversation" not in request.session:
            request.session["conversation"] = []

        conversation = request.session["conversation"]
        conversation.append({"role": "user", "content": user_message})

        discussion = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
        # Effectuer une requête à l'API Mistral
        prompt = f"""Context information is below.
                ---------------------
                {[preprocess_text(chunk[0][0]) for chunk in chunks]}
                ---------------------
                Prior discussion is below.
                ---------------------
                {discussion}
                ---------------------
                Given the context information and the prior discussion, answer the query.
                Query: {user_message}
                Answer:"""
        try:
            print("J'essaie de répondre....")
            chat_response = client.agents.complete(
                agent_id="ag:68495cb5:20241123:egsj:6803ad09",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )
            print(chat_response.choices[0].message.content)
            # Extraire la réponse du bot
            bot_response = chat_response.choices[0].message.content
            conversation.append({"role": "bot", "content": bot_response})
            request.session["conversation"] = conversation
            request.session.modified = True
            return JsonResponse({"response": bot_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)




