<template>
  <el-main>
    <el-select
      v-model="country"
      placeholder="Select any country"
      clearable
      @input="updateSort"
    >
      <el-option
        v-for="{ country_name } in supportedCountries"
        :key="country_name"
        :label="country_name"
        :value="country_name">
      </el-option>
    </el-select>
    <el-date-picker
      v-model="year"
      type="year"
      placeholder="Pick a year"
      style="margin-left: 20px;"
      @input="updateSort"
    >
    </el-date-picker>

    <el-table
      :data="growthDeathRate"
      style="width: 100%"
      empty-text="Select country or year."
    >
      <el-table-column
        prop="country"
        label="Country"
        width="180">
      </el-table-column>
      <el-table-column
        prop="year"
        label="Year">
      </el-table-column>
      <el-table-column
        prop="birth_rate"
        label="Birth Rate">
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex';

export default {
  name: 'GrowthDeathRate',
  data() {
    return {
      country: null,
      year: null,
    };
  },
  async created() {
    if (!this.supportedCountries.length) {
      await this.GET_SUPPORTED_COUNTRIES();
    }
  },
  beforeDestroy() {
    this.SET_EMPTY();
  },
  computed: {
    ...mapState('supportedCountries', {
      supportedCountries: ({ data }) => data,
    }),

    ...mapState('growthDeathRate', {
      growthDeathRate: ({ data }) => data,
    }),
  },
  methods: {
    ...mapActions('supportedCountries', [
      'GET_SUPPORTED_COUNTRIES',
    ]),

    ...mapActions('growthDeathRate', [
      'GET_GROWTH_RATE',
    ]),

    ...mapMutations('growthDeathRate', [
      'UPDATE_SORT',
      'SET_EMPTY',
    ]),

    async updateSort() {
      if (this.country || this.year) {
        this.UPDATE_SORT({
          country: this.country,
          year: this.year?.getFullYear(),
        });
        await this.GET_GROWTH_RATE();
      } else {
        this.SET_EMPTY();
      }
    },
  },
};
</script>

<style scoped>

</style>
