
import { Dialog } from 'quasar';
import Vue from 'vue'
const confirmDialog = ( title, message )  => {
    return new Promise(  resolve => {


        Dialog.create({
            title:  title,
            message: message,
            cancel: true,
            persistent: true
        }).onOk(() => {
            resolve(true);
        }).onCancel(() => {
            resolve(false);
        }).onDismiss(() => {
            resolve(true);
        })
    });

}


Vue.prototype.$confirm = confirmDialog;