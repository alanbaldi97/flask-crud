export const required = (v) => v != null && v != '' || 'Campo requerido';
export const email = v => {
    if((v || '').length==0){
        return true;
    }else{
        return /.+@.+\..+/.test(v) || 'Correo no válido'
    }
};