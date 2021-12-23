<template>
    <el-table
      :data="supportedCountries"
      @sort-change="backendSort"
      style="width: 100%">
      <el-table-column
        prop="country_code"
        label="Code"
        sortable="custom"
        width="180">
      </el-table-column>
      <el-table-column
        prop="country_name"
        sortable="custom"
        label="Country">
      </el-table-column>
      <el-table-column
        sortable="custom"
        prop="country_area"
        label="Area">
      </el-table-column>
    </el-table>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex';

export default {
  name: 'SupportedCountries',
  async created() {
    await this.GET_SUPPORTED_COUNTRIES();
  },
  computed: {
    ...mapState('supportedCountries', {
      supportedCountries: ({ data }) => data,
    }),
  },
  methods: {
    ...mapActions('supportedCountries', [
      'GET_SUPPORTED_COUNTRIES',
    ]),

    ...mapMutations('supportedCountries', [
      'UPDATE_SORT',
    ]),

    async backendSort({ prop, order }) {
      const sort = {
        prop: order ? prop : null,
        order,
      };
      this.UPDATE_SORT(sort);
      await this.GET_SUPPORTED_COUNTRIES();
    },
  },
};
</script>

<style scoped>

</style>
