import Vue from 'vue'
import { Notify } from "quasar"


const notify = (message, type = 'success') => {

    if(type == 'success'){
        Notify.create({
            color: 'green',
            message,
            position: 'top-right'
        })
    } else if(type == 'error'){
        Notify.create({
            color: 'red',
            message,
            position: 'top-right'
        })
    }
}

Vue.prototype.$notify = notify;