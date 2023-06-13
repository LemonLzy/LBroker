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
        <el-option
            v-for="(value, key) in Attribution"
            :key="key"
            :label="value"
            :value="key"
        />
      </el-select>
    </el-form-item>
    <el-form-item label="账号状态">
      <el-radio-group v-model="form.status">
        <el-radio label="仅注册"/>
        <el-radio label="开户成功"/>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="综合账户">
      <el-switch v-model="form.is_uni"/>
    </el-form-item>
    <el-form-item label="开户券商">
      <el-select v-model="form.broker" placeholder="please select your zone">
        <el-option
            v-for="(value, key) in Broker"
            :key="key"
            :label="value"
            :value="key"
        />
      </el-select>
    </el-form-item>
    <el-form-item label="国籍">
      <el-select v-model="form.nation" placeholder="please select your zone">
        <el-option
            v-for="(value, key) in Nation"
            :key="key"
            :label="value"
            :value="key"
        />
      </el-select>
    </el-form-item>
    <!-- 交易能力 -->
    <el-form-item label="交易能力">
      <el-checkbox-group v-model="form.open">
        <el-checkbox
            v-for="ability in openRef"
            :label="ability"
            :key="ability"
            name="type"
        >{{ ability }}</el-checkbox>
      </el-checkbox-group>
    </el-form-item>
    <!-- 激活能力 -->
    <el-form-item label="激活能力">
      <el-checkbox-group v-model="form.activate">
        <el-checkbox
            v-for="ability in activateRef"
            :label="ability"
            :key="ability"
            name="type"
        >{{ ability }}</el-checkbox>
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
import {onMounted, ref, watch} from 'vue'
import axios from "axios";
import {Attribution, Broker, BrokerActivateAbility, BrokerOpenAbility, Nation} from "@/enums/enums.ts";

const form = ref({
  kind: '',
  status: '',
  attr: Broker.BY,
  broker: Broker.BY,
  nation: Nation.CN,
  is_uni: false,
  open: [],
  activate: [],
})

const openRef = ref<string[]>([]);
const activateRef = ref<string[]>([]);

onMounted(() => {
  const keyByValue = getKeyByValue(Broker, form.value.broker);
  openRef.value = BrokerOpenAbility[keyByValue] || [];
  activateRef.value = BrokerActivateAbility[keyByValue] || [];
});

watch(() => form.value.broker, (newBroker) => {
  openRef.value = BrokerOpenAbility[newBroker] || [];
  activateRef.value = BrokerActivateAbility[newBroker] || [];
});

const centerDialogVisible = ref(false)
let msg = ref('')

const submit = async () => {
  centerDialogVisible.value = true

  console.log(form)
  // 异步请求接口，并等待异步请求的返回值
  const {data: res} = await axios.post('http://127.0.0.1:5000/individual', {
    firstName: 'Fred',
    lastName: 'test'
  })
  console.log(res)
}

function getKeyByValue(obj: Record<string, string>, value: string): string | undefined {
  return Object.keys(obj).find((key) => obj[key] === value);
}
</script>

<style lang="scss" scoped></style>
