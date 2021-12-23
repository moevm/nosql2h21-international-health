import dataService from '@/store/services/dataService';

const initialState = () => ({
  data: [],
  sort: {
    country: null,
    ascending: null,
  },
});

const mutations = {
  SET_EMPTY: (state) => {
    Object.assign(state, initialState());
  },
  SET_POPULATION_INFORMATION: (state, populationInformation) => {
    state.data = populationInformation;
  },
  UPDATE_SORT: (state, sort) => {
    state.sort = sort;
  },
};

const actions = {
  GET_POPULATION_INFORMATION: async ({ commit, state }) => {
    const sort = {};
    Object.keys(state.sort).forEach((key) => {
      if (state.sort[key] !== null && state.sort[key].length) {
        sort[key] = state.sort[key];
      }
    });
    const { data } = await dataService.getPopulationInformation(sort);
    commit('SET_POPULATION_INFORMATION', data);
  },
};

export default {
  namespaced: true,
  state: initialState,
  mutations,
  actions,
};
