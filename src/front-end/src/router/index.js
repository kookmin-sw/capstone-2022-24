import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: () =>
      import(/* webpackChunkName: "about" */ '@/views/About.vue'),
  },
  {
    path: '/join',
    name: 'Join',
    component: () => import(/* webpackChunkName: "Join" */ '@/views/Join.vue'),
  },
  {
    path: '/discontinue',
    name: 'Discontinue',
    component: () =>
      import(/* webpackChunkName: "Discontinue" */ '@/views/Discontinue.vue'),
  },
  {
    path: '/details',
    name: 'Details',
    component: () =>
      import(/* webpackChunkName: "Details" */ '@/views/Details.vue'),
  },
  {
    path: '/introduction',
    name: 'Introduction',
    component: () =>
      import(
        /* webpackChunkName: "Introduction" */ '@/views/footer/Introduction.vue'
      ),
  },
  {
    path: '/tos',
    name: 'Terms of Service',
    component: () =>
      import(/* webpackChunkName: "Tos" */ '@/views/footer/Tos.vue'),
  },
  {
    path: '/privacy',
    name: 'Privacy Policy',
    component: () =>
      import(
        /* webpackChunkName: "PrivacyPolicy" */
        '@/views/footer/PrivacyPolicy.vue'
      ),
  },
  {
    path: '/center',
    name: 'Center',
    component: () =>
      import(/* webpackChunkName: "Center" */ '@/views/footer/Center.vue'),
  },
  {
    path: '/questions',
    name: 'Questions',
    component: () =>
      import(
        /* webpackChunkName: "Questions" */ '@/views/footer/Questions.vue'
      ),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
