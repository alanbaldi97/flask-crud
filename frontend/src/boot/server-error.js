import Vue from 'vue'


const serverError = function(error){
    let msg = 'Lo sentimos ocurrio un error';
    const response = error.response;
    if(response) {
        const data = response.data;
        if(data){
            const message = data.msg;
            if(message) msg = message
        }
    }



    this.$notify(msg, 'error');

}

Vue.prototype.$serverError = serverError;
