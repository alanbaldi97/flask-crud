
import { BaseHttp } from "../common/BaseHttp";


export default class ManagerService extends BaseHttp{

    constructor(){
        super();
    }

    async getAll(){
        const { data } = await this.get('managers');
        return data;
    }

    async getById(id){
        const { data } = await this.get(`managers/${id}/get-by-id`);
        return data;
    }


    async insert(payload){
        const { data } = await this.post('managers',payload);
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