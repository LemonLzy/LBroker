<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="账户分类">
      <el-select v-model="form.kind" placeholder="please select your zone">
        <el-option label="新建账号" value="shanghai"/>
        <el-option label="已有帐号" value="beijing"/>
      </el-select>
    </el-form-item>
    <el-form-item label="账号归属地">
      <el-select v-model="form.attr" placeholder="please select your zone">
        <el-option label="BR" value="shanghai"/>
        <el-option label="JP" value="beijing"/>
      </el-select>
    </el-form-item>
    <el-form-item label="账号状态">
      <el-radio-group v-model="form.status">
        <el-radio label="仅注册"/>
        <el-radio label="开户成功"/>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="综合账户">
      <el-switch v-model="form.delivery"/>
    </el-form-item>
    <el-form-item label="开户券商">
      <el-select v-model="form.broker" placeholder="please select your zone">
        <el-option label="BR" value="shanghai"/>
        <el-option label="US" value="beijing"/>
      </el-select>
    </el-form-item>
    <el-form-item label="国籍">
      <el-select v-model="form.nation" placeholder="please select your zone">
        <el-option label="CN" value="shanghai"/>
        <el-option label="HK" value="beijing"/>
      </el-select>
    </el-form-item>
    <el-form-item label="交易能力">
      <el-checkbox-group v-model="form.openStock">
        <el-checkbox label="美股" name="type"/>
        <el-checkbox label="港股" name="type"/>
        <el-checkbox label="A股" name="type"/>
        <el-checkbox label="日股" name="type"/>
      </el-checkbox-group>
    </el-form-item>
    <el-form-item label="激活能力">
      <el-checkbox-group v-model="form.activate">
        <el-checkbox label="基金" name="type"/>
        <el-checkbox label="期货" name="type"/>
        <el-checkbox label="外汇" name="type"/>
        <el-checkbox label="债券" name="type"/>
      </el-checkbox-group>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
  <el-dialog
      v-model="centerDialogVisible"
      title="提交成功"
      width="30%"
      align-center
  >
    <el-text class="mx-1" v-model="msg">{{ msg }}</el-text>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="centerDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="centerDialogVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>


<script lang="ts" setup>
import {reactive, ref} from 'vue'
import axios from "axios";

const form = reactive({
  kind: '',
  status: '',
  attr: '',
  broker: '',
  nation: '',
  delivery: false,
  openStock: [],
  activate: [],
})
const centerDialogVisible = ref(false)
let msg = ref('')


const submit = async () => {
  centerDialogVisible.value = true

  // 异步请求接口，并等待异步请求的返回值
  const {data: res} = await axios.post('http://127.0.0.1:5000/individual', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  console.log(res)
}
</script>

<style lang="scss" scoped></style>
