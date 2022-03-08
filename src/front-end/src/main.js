import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { Quasar } from 'quasar';
import quasarUserOptions from './quasar-user-options';
import './styles/app.css';
import { i18n } from '@/i18n';

createApp(App)
	.use(Quasar, quasarUserOptions)
	.use(store)
	.use(router)
	.use(i18n)
	.mount('#app');
