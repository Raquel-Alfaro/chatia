from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conversation(models.Model):   # Representa un chat completo
    # Tiene usuario, titulo y fecha
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title


class Message(models.Model):    # Representa un mensaje individual
    # Cada mensaje pertenece a una conversacion
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE
    )
    # Tiene un rol (usuario, ia), contenido y fecha
    role = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content[:30]}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50, blank=True)
    theme = models.CharField(max_length=20, default="rosa")

    def __str__(self):
        return self.user.username
