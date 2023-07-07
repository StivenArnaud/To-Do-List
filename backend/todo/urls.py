from django.urls import path


from . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name="login"), # Url pour s'authentifier
    path('list-create-todo/', views.ListCreateTodo.as_view(), name="list_create_todo"), # Récupérer et Créer un todo
    path('update-todo/<int:pk>/', views.RetrieveUpdateDestroyTodo.as_view(), name="retrieve_update_destroy"), # Modifier et Supprimer un todo 
]
