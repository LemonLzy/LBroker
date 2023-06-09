import { dayjs } from 'element-plus';

const formDate = (d: number) => {
  return dayjs(d).format('YYYY-MM-DD HH:mm:ss');
};

function conversionTimestamp(timestamp: number) {
  const isMilliseconds = String(timestamp).length === 13; // 判断时间戳的长度是否为 13，以判断单位是秒还是毫秒

  const date = new Date(timestamp * (isMilliseconds ? 1 : 1000)); // 根据单位判断是否需要乘以 1000
  const year = date.getFullYear();
  const month = ('0' + (date.getMonth() + 1)).slice(-2);
  const day = ('0' + date.getDate()).slice(-2);
  const hours = ('0' + date.getHours()).slice(-2);
  const minutes = ('0' + date.getMinutes()).slice(-2);
  const seconds = ('0' + date.getSeconds()).slice(-2);
  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

export { formDate, conversionTimestamp };
