<template>
  <el-button-group style="margin-top: 10px; margin-right: 10px; float: right">
    <el-button
      style="margin-top: 10px"
      type="primary"
      icon="el-icon-upload2"
      @click="onExport"
    >
      export
    </el-button>
    <el-upload
      class="button"
      ref="upload"
      action="http://5.23.49.205:8765/import_file"
      :show-file-list="false"
      :file-list="fileList"
      :before-remove="beforeRemove"
    >
      <el-button
        type="primary"
        icon="el-icon-download">
        import
      </el-button>
    </el-upload>
  </el-button-group>
</template>

<script>
import dataService from '@/store/services/dataService';

export default {
  name: 'HeaderButtons',
  data() {
    return {
      collectionNames: {
        supported_countries: 'country_names_area',
        population_information: 'midyear_population',
        growth_death_rate: 'birth_death_growth_rates',
      },
      fileList: [],
    };
  },
  methods: {
    async onExport() {
      const key = this.$route.path.replaceAll('-', '_').replace('/', '');
      const response = await dataService.exportDatabase({
        collection_name: this.collectionNames[key],
      });
      const downloadLink = document.createElement('a');
      const blob = new Blob(['\ufeff', response.data]);
      downloadLink.href = URL.createObjectURL(blob);
      downloadLink.download = `${this.collectionNames[key]}.csv`;

      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    },

    beforeRemove(file) {
      return this.$confirm(`Cancel the transfert of ${file.name} ?`);
    },
  },
};
</script>

<style scoped>
.button {
  display: inline-block;
  height: 40px;
}
</style>
