<template>
    <nav class="navbar sticky-top bg-menu">
      <div class="container-fluid">
        <h1 class="navbar-brand fw-bold fs-2 text-light">ToDoList</h1>
        <div>
          <button class="btn btn-danger" @click="logOut"><i class="bi bi-box-arrow-right"></i> Deconnexion</button>
        </div>
      </div>
    </nav>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-12  mt-3">
                <div class="row justify-content-center">
                    <div class="col-md-7 mx-3">
                        <h2 v-if="numberTodoList" class="text-center mt-5">Pas de tache disponible</h2>
                        <!-- Affichage des taches  -->
                        <div v-else class="card border-0">
                            <div class="card-header bg-marron">
                                <h4 class="text-light">Ma liste des taches à faire</h4>
                            </div>
                            <div class="card-body">
                                <div class="">
                                    <table class="table text-start">
                                        <tbody>
                                            <tr v-for="todo in filteredTodos" v-bind:key="todo.id" class="bg-tr">
                                                <td>
                                                    <p v-if="todo.completed" class="titre"><del>{{ todo.title }}</del></p>
                                                    <p v-else id="titre">{{ todo.title }}</p>
                                                    <small class="text-muted">{{ todo.description }}</small>
                                                </td>
                                                <td>
                                                    <div v-if="todo.completed" class="form-check">
                                                        <input type="checkbox" class="form-check-input" checked :id="todo.id" @change="changeStatus(todo)">
                                                    </div>
                                                    <div v-else class="form-check">
                                                        <input type="checkbox" class="form-check-input" :id="todo.id" @change="changeStatus(todo)">
                                                    </div>
                                                </td>
                                                <td>
                                                    <i @click="edit(todo)" class="bi bi-pencil-square text-primary"></i>
                                                    <i @click="removeTodo(todo.id)" class="bi bi-trash-fill text-danger"></i>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="card-footer border-0 d-flex bg-footer">
                                <span class="p-2 text-muted"><strong>{{numberOfTodo}}</strong> taches à faire</span>
                                <ul class="nav">
                                    <li class="nav-item"><a class="nav-link text-muted" :class="{selected: filter === 'all'}" @click.prevent="filter = 'all'" href="#">Toutes</a></li>
                                    <li class="nav-item"><a class="nav-link text-muted" :class="{selected: filter === 'todo'}" @click.prevent="filter = 'todo'" href="#">À faire</a></li>
                                    <li class="nav-item"><a class="nav-link text-muted" :class="{selected: filter === 'done'}" @click.prevent="filter = 'done'" href="#">Complètes</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <!-- Ajouter une tache -->
                        <div v-if="!editing.status" class="card">
                            <div class="card-header bg-footer">
                                <h4 class="fw-bold">Ajouter d'une tache</h4>
                            </div>
                            <div class="card-body">
                                <div class="">
                                    <div class="row">
                                        <div class="col-md-12">
                                            <form @submit.prevent="addNew" action="" method="post">
                                                <div class="form-group mb-3 text-start">
                                                    <label for="title" class="form-label">Titre <span class="text-danger">*</span></label>
                                                    <input type="text" class="form-control" id="title" name="title" v-model="newItem.title" required>
                                                    <small v-if="errors.title" class="text-danger ">{{ errors.title }}</small>
                                                </div>
                                                <div class="mb-3 text-start">
                                                    <label for="description" class="form-label">Description</label>
                                                    <textarea class="form-control" id="description" name="description" rows="3" v-model="newItem.description"></textarea>
                                                </div>
                                                <div class="text-start">
                                                    <button type="submit" class="btn btn-add">Ajouter</button>
                                                </div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-else class="card">
                            <!-- Modifier une tache -->
                            <div class="card-header bg-warning">
                                <h4>Modifier la tache</h4>
                            </div>
                            <div class="card-body">
                                <div class="">
                                    <div class="row">
                                        <div class="col-md-12">
                                            <form @submit.prevent="update" action="" method="post">
                                                <div class="mb-3 text-start">
                                                    <label for="title" class="form-label">Titre</label>
                                                    <input type="text" class="form-control" id="title" name="title" v-model="editing.todo.title">
                                                </div>
                                                <div class="mb-3 text-start">
                                                    <label for="description" class="form-label">Description</label>
                                                    <textarea class="form-control" id="description" name="description" rows="3" v-model="editing.todo.description"></textarea>
                                                </div>
                                                <div class="text-start">
                                                    <button type="submit" class="btn btn-warning">Modifier</button>
                                                </div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
  <script>
    import axios from "axios";
  export default {
    name: 'Todolist',
    data(){
        return {
            todos: [],
            newItem: {
                title: "",
                description: "",
                completed: false,
                user: this.$store.state.user_id
            },
            errors: {
                title: ""
            },
            editing:{
                status: false,
                todo: {}
            },
            filter: 'all',
        }
    },
    methods: {
        fetchTodoList(){
            // La requête GET via le backend pour récupérer les tache disponible
            axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
            const url = '/list-create-todo/';
            axios.get(url)
            .then(response => {
                this.todos = response.data;
            })
            .catch(error => {
                console.log(error);
            })
        },

        formIsValid(){
            // On vérifie si le champ titre n'est pas pour l'ajout d'une tache
            let valid = true
            if(!this.title){
                this.errors.title = "Ce champ ne doit pas être vide."
                valid = false
            }else{
                this.errors.title = ""
                valid = true
            }

            return valid
        },

        addNew(){
            // La requête POST via le backend pour ajouter une nouvelle tache
            if(this.formIsValid()){
                axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
                const url = '/list-create-todo/'
                axios.post(url, this.newItem)
                .then(response => {
                    this.todos.unshift(response.data);
                    this.newItem = {title:"", description: "", completed: false, user: this.$store.state.user_id};
                    //this.fetchTodoList()
                })
                .catch(errror => {
                    console.log(errror);
                })
            }
        },

        edit(todo){
            this.editing.status = true
            this.editing.todo = todo
        },

        changeStatus(todo){
            // On modifie le status de la tache Complète ou Pas
            this.editing.todo = todo;
            this.editing.todo.completed = !todo.completed;
            this.update();
        },

        update(){
            // La requête PUT via le backend pour modifier une tache
            axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
            const url = '/update-todo/' + this.editing.todo.id + '/'
            axios.put(url, this.editing.todo)
            .then(response => {
                this.editing.status = false
                this.editing.todo = {}
                this.fetchTodoList()
            })
            .catch(errror => {
                console.log(errror);
            })

        },

        removeTodo(id){
            // La requête DELETE via le backend pour supprimer une tache
            axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
            const url = '/update-todo/' + id + '/'
            axios.delete(url)
            .then(response => {
                this.fetchTodoList()
            })
            .catch(errror => {
                console.log(errror);
            })
        },

        logOut(){
            this.$store.commit('removeToken');
            this.$router.push('/');
        }
    },
    mounted(){
        this.fetchTodoList() // Actualise l'affichage de la liste des taches
    },

    computed: {
        numberTodoList(){
            // Nombre de taches
            return this.todos.length === 0
        },
        numberOfTodo (){
            // Nombre de taches à faire 
            return this.todos.filter(todo => !todo.completed).length
        },
        donetodos(){
            // Nombre de taches complètes
            return this.todos.filter(todo => todo.completed).length
        },

        filteredTodos(){
            // les filtres
            if(this.filter === 'todo'){
                return this.todos.filter(todo => !todo.completed)
            }else if(this.filter === 'done'){
                return this.todos.filter(todo => todo.completed)
            }
            return this.todos
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
    #titre{
        padding: 0;
        margin: 0;
        font-weight: 600;
    }

    .titre{
        padding: 0;
        margin: 0;
        color: #999;
    }
    .bi{
        font-size: 20px;
        cursor: pointer;
        
    }
    .bi-trash-fill{
        margin-left: 12px;
    }

    .bg-menu{
        background-color: #999;
    }
    .selected{
        background-color: #999;
        font-weight: 600;
        border-radius: 5px;
    }
    .bg-marron, .btn-add:hover{
        background-color: #bf8c8c;
    }
    .bg-tr{
        background-color: #fff;
        color: #333;
    }
    .bg-footer, .btn-add{
        background-color: #ece5e5;
    }

  </style>
  