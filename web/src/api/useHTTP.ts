import { Method } from 'axios';
import requests from '@/api/requests';
import { AxiosRequestHeaders } from 'axios';

export interface HTTPConfig {
  url: string;
  method: Method;
  data?: { [key: string]: unknown };
  params?: { [key: string]: unknown };
  headers?: AxiosRequestHeaders;
}

const useHTTP = <T>(config: HTTPConfig): Promise<T> => {
  return new Promise<T>((resolve, reject) => {
    requests({
      url: config.url,
      method: config.method,
      data: config.data || {},
      params: config.params || {},
      headers: config.headers || { 'Content-Type': 'application/json' },
    })
      .then((resp) => {
        resolve(resp.data);
      })
      .catch((err) => {
        reject(err);
      });
  });
};

export default useHTTP;
