<template>
  <div id="app">
    <el-tabs v-model="activeName" class="openTable">
      <el-tab-pane label="个人开户" name="individual">
        <Individual/>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script lang="ts" setup>
import Individual from '@/components/Individual.vue';
import {ref} from 'vue'

const activeName = ref('individual')
</script>

<style scoped>
#app {
  padding: 0;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(134, 140, 151, 0.24);
  border-radius: 3px;
  max-width: 800px;
  max-height: 60vh;
  box-shadow: rgb(53 64 82 / 4%) 0 2px 4px 0;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}

.openTable {
  padding-left: 20px;
  padding-top: 10px;
}
</style>
