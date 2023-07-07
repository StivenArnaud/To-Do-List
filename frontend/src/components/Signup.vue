<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6  mt-5">
                <div class="card">
                    <div class="card-header bg-info">
                        <h2 class="text-muted">Création de compte</h2>
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
                                    <div class="form-group my-3 text-start"> 
                                        <input type="password" name="password2" id="password2" placeholder="confirmez le mot de passe" class="form-control" v-model="password2">
                                        <small v-if="errors.password2" class="text-danger">{{ errors.password2 }}</small>
                                    </div>
                        
                                    <div class="form-group my-3"> 
                                        <button type="submit" class="btn btn-info text-muted w-50">Créer mon compte</button>
                                    </div>

                                    <div class="form-group my-3 text-start"> 
                                        <p>J'ai un compte. <router-link class="text-decoration-none text-info" to="/">Se connecter</router-link></p>
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
    name: 'Signup',
    data(){
        return {
            username: "",
            password: "",
            password2: "",
            errors: {
                username: "",
                password: "",
                password2: "",
            }
        }
    },
    methods: {
        isValidForm(){
            // On verifie si le nom d'utilisateur et le mode passe ne sont pas vide
            let valid = true
            //Verification du username
            if(!this.username){
                this.errors.username = "Ce champ ne doit pas être vide";
            }else{
                this.errors.username = "";
            }
            // Verification du password
            if(!this.password){
                this.errors.password = "Ce champ ne doit pas être vide.";
            }else{
                this.errors.password = "";
            }
            // Verification de la confirmation de mot de passe
            if(this.password && this.password2 && this.password != this.password2){
                this.errors.password2 = "Les mots de passe ne sont pas identiques";
            }else{
                this.errors.password2 = "";
            }
            // on verifie s'il y a eu des erreurs
            if(this.errors.username || this.errors.password || this.errors.password2){
                valid = false;
            }
            return valid;
        },

        submitForm(){
            // Cette methode permet de créer le compte d'un utilisateur
            if(this.isValidForm()){ // On verifie si les champs ne sont pas vide
                const url = "/auth/users/"
                axios.post(url, {username: this.username, password: this.password})
                .then(response => {
                    this.$router.push('/');
                    this.username = "";
                    this.password = "";
                    this.password2 = "";
                })
                .catch(error => {
                    if(error.response.data.username){// Verifie si le nom d'utilisateur existe deja
                        this.errors.username = "Nom d'utilisation non valide."
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
  