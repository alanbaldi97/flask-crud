
import { BaseHttp } from "../common/BaseHttp";

export default class AreaTypeService extends BaseHttp{

    constructor(){
        super();
    }

    getAll(){
        return this.get('area-types');
    }




}