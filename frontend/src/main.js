import { createApp } from 'vue'

import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import './scss/main.scss';

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)

app.mount('#app')
