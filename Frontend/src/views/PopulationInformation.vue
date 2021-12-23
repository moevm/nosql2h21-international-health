<template>
  <el-main>
    <el-select
      v-model="country"
      placeholder="Select any country"
      clearable
      @input="updateSort"
    >
      <el-option
        v-for="{country_name} in supportedCountries"
        :key="country_name"
        :label="country_name"
        :value="country_name">
      </el-option>
    </el-select>
    <el-table
      :data="populationInformation"
      @sort-change="updateSort"
      style="width: 100%">
      <el-table-column
        prop="country"
        label="Country"
        sortable="custom"
        width="180">
      </el-table-column>
      <el-table-column
        prop="min_population"
        label="Min. Population">
      </el-table-column>
      <el-table-column
        prop="max_population"
        label="Max. Population">
      </el-table-column>
      <el-table-column
        prop="average_population"
        label="Average Population">
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex';

export default {
  name: 'PopulationInformation',
  data() {
    return {
      country: null,
    };
  },
  async created() {
    if (!this.supportedCountries.length) {
      await this.GET_SUPPORTED_COUNTRIES();
    }
    await this.GET_POPULATION_INFORMATION();
  },
  beforeDestroy() {
    this.SET_EMPTY();
  },
  computed: {
    ...mapState('supportedCountries', {
      supportedCountries: ({ data }) => data,
    }),

    ...mapState('populationInformation', {
      populationInformation: ({ data }) => data,
    }),
  },
  methods: {
    ...mapActions('supportedCountries', [
      'GET_SUPPORTED_COUNTRIES',
    ]),

    ...mapActions('populationInformation', [
      'GET_POPULATION_INFORMATION',
    ]),

    ...mapMutations('populationInformation', [
      'UPDATE_SORT',
      'SET_EMPTY',
    ]),

    async updateSort({ order = null }) {
      const sort = {
        ascending: order ? order === 'ascending' : null,
        country: this.country,
      };
      this.UPDATE_SORT(sort);
      await this.GET_POPULATION_INFORMATION();
    },
  },
};
</script>

<style scoped>

</style>
