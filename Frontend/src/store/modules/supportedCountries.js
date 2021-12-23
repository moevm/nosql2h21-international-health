import dataService from '@/store/services/dataService';

const mutations = {
  SET_SUPPORTED_COUNTRIES: (state, supportedCountries) => {
    state.data = supportedCountries;
  },
  UPDATE_SORT: (state, sort) => {
    state.sort = {
      sort_by: sort.prop,
      ascending: sort.order === 'ascending',
    };
  },
};

const actions = {
  GET_SUPPORTED_COUNTRIES: async ({ commit, state }) => {
    const { data } = await dataService.getSupportedCountries(state.sort);
    commit('SET_SUPPORTED_COUNTRIES', data);
  },
};

const state = () => ({
  data: [],
  sort: {
    sort_by: null,
    ascending: null,
  },
});

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
