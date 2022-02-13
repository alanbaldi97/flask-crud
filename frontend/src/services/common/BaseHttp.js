import { api } from "src/boot/axios";
import { Store } from "src/store";



export class BaseHttp{

    constructor(){
        this.http = api
        this.token = localStorage.getItem('access_token');
        

    }

    async getToken(){
        this.http.defaults.headers['Accept'] = 'application/json';
        this.http.defaults.headers['Authorization'] = `Bearer ${this.token}`;
        const { data } = await this.http.get('/auth/user');
        const { user, access_token } = data;
        localStorage.setItem('access_token',access_token);
        Store.dispatch('auth/setUser', user);
        return access_token;
    }

    async get(source){
        const token = await this.getToken(); //Obtengo un fresh token
        this.http.defaults.headers['Accept'] = 'application/json';
        this.http.defaults.headers['Authorization'] = `Bearer ${token}`;
        return this.http.get(source);
    }


    async post(source, payload){
        const token = await this.getToken(); //Obtengo un fresh token
        this.http.defaults.headers['Accept'] = 'application/json';
        this.http.defaults.headers['Authorization'] = `Bearer ${token}`;
        return this.http.post(source, payload ? payload : null);
    }

    async delete(source){
        const token = await this.getToken(); //Obtengo un fresh token
        this.http.defaults.headers['Accept'] = 'application/json';
        this.http.defaults.headers['Authorization'] = `Bearer ${token}`;
        return this.http.delete(source);
    }

}