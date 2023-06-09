import axios from 'axios';


const requests = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});

//请求拦截器
requests.interceptors.request.use((config) => {
  config = config || {};
  // @ts-ignore
  if (config.headers['Content-Type'] === 'multipart/form-data') {
    let form = new FormData(); // 构造函数 解决传递头部参数格式不正确
    for (let key in config.data) {
      form.append(key, config.data[key]);
    }
    config.data = form;
  }
  return config;
});

//响应拦截器
requests.interceptors.response.use(
  (resp) => {
    const { code, msg } = resp.data || {};
    const err = new Error(msg);
    if (code !== 0) {
        console.log(code, err)
        return Promise.reject(err);
    }
    return Promise.resolve(resp);
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default requests;
