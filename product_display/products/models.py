from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    discounted_price = models.CharField(max_length=50)
    actual_price = models.CharField(max_length=50)
    description = models.TextField(default="Description manquante")
    image_url = models.URLField()
    product_url = models.URLField()

    def __str__(self):
        return self.name



class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    adresse = models.TextField()
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"



class Conversation(models.Model):
    user_id = models.CharField(max_length=255)  # Identifiant unique pour l'utilisateur
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=10, choices=[("user", "User"), ("bot", "Bot")])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)