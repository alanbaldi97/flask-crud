import Vue from 'vue'
import axios from 'axios'

Vue.prototype.$axios = axios

export const api = axios.create({
    baseURL: process.env.VUE_APP_URL_API
});
