import axios from 'axios';

export default {
  async getSupportedCountries(sort) {
    // eslint-disable-next-line no-return-await
    return await axios.get('http://5.23.49.205:8765/get_supported_countries', {
      params: sort,
    });
  },

  async getPopulationInformation(params) {
    // eslint-disable-next-line no-return-await
    return await axios.get('http://5.23.49.205:8765/get_population_information', {
      params,
    });
  },

  async getGrowthDeathRate(params) {
    return axios.get('http://5.23.49.205:8765/get_growth_rate', {
      params,
    });
  },

  async exportDatabase(params) {
    return axios.get('http://5.23.49.205:8765/export_file', {
      params,
    });
  },
};
