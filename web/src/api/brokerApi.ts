import useHTTP from '@/api/useHTTP';
import { BasicResp } from '@/api/types';

export interface SearchReq {
  method: string;
  uid: number;
}

export const reqSearch = (params: SearchReq) => {
    //axios http
    return useHTTP<BasicResp<null>>({
        url: `/individual`,
        method: 'post',
        data: { ...params },
    });
};
