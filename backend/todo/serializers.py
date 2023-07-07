from rest_framework import serializers


from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """ Cette classe permet de convertir les données au format JSON et inversement."""
    class Meta:
        model = Todo
        fields = '__all__'