import { Store } from "src/store";
import { BaseHttp } from "../common/BaseHttp";

export class AuthService extends BaseHttp{

    constructor(){
        super();
    }

    async login( username, password ){
        const { data } = await this.http.post(`auth/login`,{
            username,
            password
        });

        return data;
    }


    async isAutenticate(){

        try{
            
            const token = localStorage.getItem('access_token');
            if(!token) return false;
            const { data } = await this.get('/auth/user');
            const { user, access_token } = data;
            localStorage.setItem('access_token',access_token);
            Store.dispatch('auth/setUser', user);
            return true;
        }catch(error){
            return false;
        }

    }




}