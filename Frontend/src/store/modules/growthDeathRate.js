import dataService from '@/store/services/dataService';

const initialState = () => ({
  data: [],
  sort: {
    country: null,
    year: null,
  },
});

const mutations = {
  SET_EMPTY: (state) => {
    Object.assign(state, initialState());
  },
  SET_GROWTH_RATE: (state, populationInformation) => {
    state.data = populationInformation;
  },
  UPDATE_SORT: (state, sort) => {
    state.sort = sort;
  },
};

const actions = {
  GET_GROWTH_RATE: async ({ commit, state }) => {
    const sort = {};
    Object.keys(state.sort).forEach((key) => {
      if (state.sort[key]) {
        sort[key] = state.sort[key];
      }
    });
    const { data } = await dataService.getGrowthDeathRate(sort);
    commit('SET_GROWTH_RATE', data);
  },
};

export default {
  namespaced: true,
  state: initialState,
  mutations,
  actions,
};
