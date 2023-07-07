from django.db import models
from django.conf import settings

# Create your models here.


class Todo(models.Model):
    """ Cette classe represente le modèle de notre base de données """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_todo')
    title = models.CharField(max_length=255, verbose_name="Titre ")
    description = models.TextField(blank=True, max_length=2000)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self) -> str:
        return self.title
