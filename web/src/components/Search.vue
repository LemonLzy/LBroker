<template>
  <el-main>
    <el-form ref="ruleFormRef" :model="searchForm" :rules="rules" label-position="left" @submit.native.prevent>
      <el-row :gutter="16">
        <el-col :span="6">
          <el-form-item prop="uid">
            <el-input
                v-model.number="searchForm.uid"
                :width="200"
                placeholder="请输入账号"
                maxlength="9"
                clearable
                @keydown.enter.native='submit'
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-button class="search" type="primary" @click="submit">查询</el-button>
        </el-col>
      </el-row>
    </el-form>

    <el-row>
      <el-table
          border
          :data="formattedTableData"
          style="width: 100%"
          show-header
          stripe
          header-align="center"
          max-height="400"
          class="accountInfo"
          v-loading="loadingShow"
      >
        <el-table-column type="expand">
          <template #default="props">
            <el-form label-position="left" inline class='expand'>
              <el-form-item label="状态">
                <span>{{ props.row.status }}</span>
              </el-form-item>
              <el-form-item label="开通时间">
                <span>{{ props.row.opened_time }}</span>
              </el-form-item>
              <el-form-item label="关闭时间">
                <span>{{ props.row.closed_time }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column prop="broker" label="券商" align="center" width="70" :resizable="false"></el-table-column>
        <el-table-column prop="kind" label="kind" align="center" width="70" :resizable="false"></el-table-column>
        <el-table-column prop="model" label="model" align="center" width="90" :resizable="false"></el-table-column>
        <el-table-column prop="type" label="类型" align="center" width="70" :resizable="false"></el-table-column>
        <el-table-column prop="ability" label="交易能力" align="center"></el-table-column>
        <el-table-column prop="account_id" label="账户id" width="150" align="center"></el-table-column>
        <template v-slot:empty>
          <el-empty image-size:30 description="未查询到账户信息"></el-empty>
        </template>
      </el-table>
    </el-row>
  </el-main>
</template>

<script lang="ts" setup>
import {Ability, Broker, Kind, Model, Status, Type} from "@/enums/enums.ts";
import { conversionTimestamp } from "@/app/utils.ts";
import {reqSearch, SearchRsp} from "@/api/brokerApi.js";
import type { FormInstance, FormRules } from 'element-plus';
import {computed, reactive, ref} from "vue";

const ruleFormRef = ref<FormInstance>();
const rules = reactive<FormRules>({
  uid: [
    { required: true, message: 'Please input Activity name', trigger: 'blur' },
  ]
});
const loadingShow = ref(false);

const searchForm = reactive({
  method: "Search",
  uid: '',
});

const tableData = reactive<SearchRsp[]>([]);

const formattedTableData = computed(() => {
  return tableData.map((item) => {
    return {
      broker: Broker[item.broker],
      kind: Kind[item.kind],
      model: Model[item.model],
      type: Type[item.type],
      ability: item.enable_market.map((ability) => Ability[ability]).join(' | '),
      account_id: item.account_id,
      status: Status[item.status],
      opened_time: conversionTimestamp(item.opened_time),
      // 当closed_time为""时，显示为'-'，否则显示时间
      closed_time: item.closed_time ? conversionTimestamp(item.closed_time) : '-',
    };
  });
});

const submit = () => {
  ruleFormRef.value?.validate(async (valid) => {
    if (valid) {
      const uid = Number(searchForm.uid);
      let {code, data} = await reqSearch({...searchForm, uid});
      if (code !== 0) {
        console.log('error submit!!');
        return false;
      }
      console.log('success submit!!');
      tableData.splice(0, tableData.length, ...data); // 更新 tableData 数组
    } else {
      console.log('error submit!!');
      return false;
    }
  });
};
</script>

<style scoped>
.search {
  color: #fff;
  background-color: #206bc4;
  border-color: #206bc4;
}

.search:hover {
  color: #fff;
  background-color: #1b59a3;
  border-color: #195398;
}

.search:focus {
  color: #fff;
  background-color: #206bc4;
  border-color: #206bc4;
}

.search:active {
  color: #fff;
  background-color: #1b59a3;
  border-color: #195398;
}

.expand label {
  width: 100px;
  color: #99a9bf;
}

:deep(.expand .el-form-item) {
  margin-right: 0;
  margin-bottom: 0;
  margin-left: 10px;
  width: 50%;
  font-size: 8px;
}

:deep(.expand .el-form-item__label) {
  font-size: 8px;
}
</style>
