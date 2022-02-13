
import { BaseHttp } from "../common/BaseHttp";


export default class ManagerService extends BaseHttp{

    constructor(){
        super();
    }

    async getAll( params = {} ){
        const { data } = await this.post('managers', params);
        return data;
    }

    async getById(id){
        const { data } = await this.get(`managers/${id}/get-by-id`);
        return data;
    }


    async insert(payload){
        const { data } = await this.post('managers/store',payload);
        return data;
    }

    async update(id, payload){
        const { data } = await this.post(`managers/${id}`,payload);
        return data;
    }

    async deleteManager(id){
        const { data } = await this.delete(`managers/${id}`);
        return data;
    }


}