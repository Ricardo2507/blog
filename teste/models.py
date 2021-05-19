from django.conf import settings
from django.db import models
from django.utils import timezone

# Post é o nome do nosso modelo. Nós podemos dar
#  um nome diferente (mas precisamos evitar caracteres
#  especiais e espaços em branco). Sempre inicie o 
# nome de uma classe com uma letra em maiúsculo.
# models.Model significa que o Post é um modelo de Django,
#  então o Django sabe que ele deve ser salvo no banco de dados.
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
