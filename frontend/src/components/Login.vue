<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6  mt-5">
                <div class="card">
                    <div class="card-header bg-info">
                        <h2 class="text-muted">Connexion</h2>
                    </div>
                    <div class="card-body">
                        <div class="row justify-content-center">
                            <div class="col-md-10">
                                <form @submit.prevent="submitForm">
                                    <div v-if="errors.wrong_credentials" class="form-group my-3 text-start">
                                        <small class="text-danger ">{{ errors.wrong_credentials}}</small>
                                    </div>
                                    <div class="form-group my-3 text-start"> 
                                        <input type="text" name="username" id="username" placeholder="Nom d'utilisateur" class="form-control" v-model="username">
                                        <small v-if="errors.username" class="text-danger ">{{ errors.username }}</small>
                                    </div>
                                    <div class="form-group my-3 text-start"> 
                                        <input type="password" name="password" id="password" placeholder="Mot de passe" class="form-control" v-model="password">
                                        <small v-if="errors.password" class="text-danger">{{ errors.password }}</small>
                                    </div>
                        
                                    <div class="form-group my-3"> 
                                        <button type="submit" class="btn btn-info text-muted w-50">Se connecter</button>
                                    </div>

                                    <div class="form-group my-3 text-start"> 
                                        <p>Je n'ai pas de compte. <router-link class="text-decoration-none text-info" to="/signup">Créer un compte</router-link></p>
                                    </div>
                                </form>
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
    name: 'Login',
    data(){
        return {
            username: "",
            password: "",
            errors: {
                username: "",
                password: "",
                wrong_credentials: ""
            }
        }
    },
    methods: {
        // On verifie si le nom d'utilisateur et le mode passe ne sont pas vide
        isValidForm(){
            let valid = true
            if(!this.username){
                this.errors.username = "Ce champ ne doit pas être vide";
            }else{
                this.errors.username = "";
            }

            if(!this.password){
                this.errors.password = "Ce champ ne doit pas être vide.";
            }else{
                this.errors.password = "";
            }
            if(this.errors.username || this.errors.password){
                valid = false;
            }
            return valid;
        },

        submitForm(){
            // Cette methode permet à l'utilisateur de se connecter
            if(this.isValidForm()){ // On verifie si les champs ne sont pas vide
                const url = "/login/";
                axios.post(url, {username: this.username, password: this.password})
                .then(response => {
                    this.$store.commit('setToken', response.data);
                    this.username = "";
                    this.password = "";
                    this.$router.push('/todo')
                })
                .catch(error => {
                    if(error.response.data.non_field_errors){
                        this.errors.wrong_credentials = "Nom d'utilisateur ou mot de passe incorrect";
                    }else{
                        this.errors.wrong_credentials = "";
                    }
                })
            }
            
        }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped lang="scss">
  </style>
  