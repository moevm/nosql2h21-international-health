import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [

  {
    path: '/',
    redirect: '/supported-countries',
  },
  {
    path: '/supported-countries',
    name: 'SupportedCountries',
    component: () => import('@/views/SupportedCountries.vue'),
  },
  {
    path: '/population-information',
    name: 'PopulationInformation',
    component: () => import('@/views/PopulationInformation.vue'),
  },
  {
    path: '/growth-death-rate',
    name: 'GrowthDeathRate',
    component: () => import('@/views/GrowthDeathRate.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
