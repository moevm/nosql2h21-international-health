import Vue from 'vue';
import Vuex from 'vuex';
import supportedCountries from './modules/supportedCountries';
import populationInformation from './modules/populationInformation';
import growthDeathRate from '@/store/modules/growthDeathRate';

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  modules: {
    supportedCountries,
    populationInformation,
    growthDeathRate,
  },
});
