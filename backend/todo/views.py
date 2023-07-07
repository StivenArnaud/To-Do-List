from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.
from .models import Todo
from .serializers import TodoSerializer


# Notre vue login
class Login(ObtainAuthToken): 
    def post(self, request, *args, **kwargs):
        """ Cette méthode permet à l'utilisateur de s'authentifier"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        #On retourne l'id de l'utilisateur et le Token de connexion
        return Response({'token': token.key, 'user_id': user.id})


class ListCreateTodo(generics.ListCreateAPIView):
    """ Cette classe permet de récupérer tous les Todo et d'ajouter les Todo dans notre base de données. """

    permission_classes = [permissions.IsAuthenticated,] # restreindre l'accès aux données à un utilisateur non authentifier
    serializer_class = TodoSerializer # récupérer les données au format JSON et inversement

    def get_queryset(self):
        #récupère les todo d'utilisateur
        return Todo.objects.filter(user=self.request.user)
    

class RetrieveUpdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    """ Cette permet de Modifier et Supprimer un Todo"""
    permission_classes = [permissions.IsAuthenticated,] # restreindre l'accès aux données à un utilisateur non authentifier
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



