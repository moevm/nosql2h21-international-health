<template>
  <el-container style="min-width: 800px">
    <el-header>
      <Header></Header>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
import Header from '@/components/common/Header.vue';

export default {
  components: { Header },
};
</script>

<style lang="scss">
* {
  font-family: "JetBrains Mono", sans-serif;
}
</style>
