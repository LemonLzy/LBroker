import useHTTP from '@/api/useHTTP';
import { BasicResp } from '@/api/types';
import {Ability, Kind} from "@/enums/enums.ts";

export interface SearchReq {
  method: string;
  uid: number;
}

export interface SearchRsp {
    account_id: number;
    broker: string;
    closed_time: number;
    enable_market: Ability[];
    kind: Kind;
    market_id: number;
    model: string;
    opened_time: number;
    status: string;
    type: string;
}

export const reqSearch = (params: SearchReq) => {
    //axios http
    return useHTTP<BasicResp<null>>({
        url: `/individual`,
        method: 'post',
        data: { ...params },
    });
};
