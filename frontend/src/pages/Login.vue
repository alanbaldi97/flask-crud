<template>
    <q-layout  class="background-color" style="background-color=#172b4d">
        <q-page-container style="height: 100vh" >
            <div class="row justify-center items-center" style="height: 100%">
                <div class="col-4 col-md-4">
                    <q-card class="col-2 col-md-2 q-mt-md card-color q-pa-lg">
                        <!-- <img src="https://www.eleconomista.com.mx/__export/1559878811565/sites/eleconomista/img/2019/02/20/aeropuerto_cuernavaca.jpg_423392900.jpg" width="50%" alt=""> -->
                        <!-- <q-separator /> -->
                        <q-card-section class="text-muted text-center text-h5">
                            Iniciar Sesión
                        </q-card-section>
                        <q-card-section class="card-color">
                            <q-form ref="form" @submit.prevent="login">
                                <q-input dense outlined v-model="username" :rules="rules" label="Usuario">
                                    <template v-slot:prepend>
                                        <q-icon name="person" />
                                    </template>
                                </q-input>
                                    
                                <q-input dense type="password" outlined v-model="password" :rules="rules" label="Contraseña" @keypress.enter="login">
                                    <template v-slot:prepend>
                                        <q-icon name="lock" />
                                    </template>
                                </q-input>
                                <q-btn :loading="loading" class="full-width" color="indigo-6" rounded label="Iniciar Sesión"  @click="login" />
                            </q-form>
                        </q-card-section>
                    </q-card>
                </div>
                
            </div>
            
        </q-page-container>
    </q-layout>
    
</template>
<script>
import { mapActions } from 'vuex';
import { required } from '../common/rules';
import { AuthService } from '../services/auth/AuthService';

const authService = new AuthService();

export default {
    name:'Login',
    data(){
        return {
            username:null,
            password: null,
            rules:[required],
            loading: false,
        }
    },
    methods:{

        ...mapActions('auth',['setUser']),


        async login(){

            try {
                
                const valid = await this.$refs.form.validate();
                if(!valid) return;

                this.loading = true;
                const response = await authService.login(this.username, this.password);
                if(!response.success) return this.$notify(response.msg,'error');

                const { user, access_token } = response;
                this.setUser(user);
                localStorage.setItem('access_token',access_token);
                

                this.$router.push({name: 'managers'});
                
            } catch (error) {
                this.$serverError(error);
            }finally {
                this.loading = false;
            }
            
        }
    }
}
</script>
<style scope>

</style>