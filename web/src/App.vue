<template>
  <div id="app">
    <el-tabs v-model="activeName" class="openTable">
      <el-tab-pane label="个人开户" name="individual">
        <IndividualOpen/>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script lang="ts" setup>
import IndividualOpen from '@/components/Individual.vue';
import {ref} from 'vue'

const activeName = ref('individual')
</script>

<style scoped>
#app {
  padding: 0;
  margin-left: 20px;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(134, 140, 151, 0.24);
  border-radius: 3px;
  max-width: 1000px;
  box-shadow: rgb(53 64 82 / 4%) 0 2px 4px 0;
}

.openTable {
  padding-left: 20px;
  padding-top: 10px;
}
</style>
