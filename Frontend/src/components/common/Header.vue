<template>
  <el-menu
        @select="handleSelect"
        :default-active="$route.name"
        mode="horizontal"
  >
        <el-menu-item
          v-for="item in menuItems"
          :key="item"
          :index="item">
          {{ lowerCase(item) }}
        </el-menu-item>
        <HeaderButtons></HeaderButtons>
  </el-menu>
</template>

<script>
import { lowerCase } from 'lodash/string';
import HeaderButtons from '@/components/common/HeaderButtons.vue';

export default {
  name: 'Header',
  components: { HeaderButtons },
  data() {
    return {
      menuItems: [
        'SupportedCountries',
        'PopulationInformation',
        'GrowthDeathRate',
      ],
    };
  },

  methods: {
    lowerCase,

    handleSelect(index) {
      if (this.$route.name !== index) {
        this.$router.push({
          name: index,
        });
      }
    },
  },
};
</script>

<style lang="scss">
  .el-header {
    line-height: 60px;
  }
</style>
