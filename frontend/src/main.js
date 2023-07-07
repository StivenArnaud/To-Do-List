import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.min.css"
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000"; // L'adresse de base pour se connecter au backend

createApp(App).use(store).use(router, axios).mount('#app')
