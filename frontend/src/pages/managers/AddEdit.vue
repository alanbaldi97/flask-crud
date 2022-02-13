<template>
    <q-page >
        <div class="row">
            <div class="q-pa-md q-gutter-sm">
                <q-breadcrumbs gutter="none">
                    <q-breadcrumbs-el label="Administradores" :to="{name:'managers'}" />
                    <q-breadcrumbs-el label="Agregar Administrador" />
                </q-breadcrumbs>
            </div>
        </div>
        <div class="row q-pa-md justify-center">
            
            
            <div class="col-md-7">
                <div class="row justify-center">
                    <div class="col-md-12">
                        <q-card >
                            <q-card-section>
                                <div class="row justify-center">
                                    <cropper :src="img" @result="onResult" :disable="isVisibility"></cropper>
                                </div>
                            </q-card-section>
                            <q-card-section>
                                <q-form ref="form">
                                    <div class="row">
                                        <div class="col-md-12">
                                            <q-input v-model="name" dense outlined placeholder="Nombre(s)" :rules="[rules.required]" :disable="isVisibility"></q-input>
                                        </div>
                                        <div class="col-md-12 q-mt-sm">
                                            <q-input v-model="last_name" dense outlined placeholder="Apellido(s)" :rules="[rules.required]" :disable="isVisibility"></q-input>
                                        </div>
                                        <div class="col-md-12 q-mt-sm">
                                            <q-input v-model="email" dense outlined placeholder="Correo Electrónico" :rules="[rules.required, rules.email]" :disable="isVisibility"></q-input>
                                        </div>
                                        <div class="col-md-12 q-mt-sm">
                                            <q-select 
                                            option-value="id" option-label="name"
                                            v-model="area_type_id" 
                                            dense outlined 
                                            :options="areaTypes" 
                                            label="Tipo de Area" 
                                            :rules="[rules.required]"
                                            emit-value
                                            map-options
                                            :disable="isVisibility"
                                            ></q-select>
                                        </div>
                                        <div class="col-md-12 q-mt-sm">
                                            <q-select v-model="status" dense  outlined :options="['Activo','Inactivo']" label="Estatus" :rules="[rules.required]" :disable="isVisibility"></q-select>
                                        </div>
                                    </div>
                                    <div class="row justify-center">
                                        <q-btn outline size="md" color="secondary" @click="$router.push({name:'managers'})">Cancelar</q-btn>
                                        <q-btn v-if="!isVisibility" class="q-ml-sm" size="md" color="indigo-7" @click="save">
                                            {{ !isEdit ? 'Agregar' : 'Editar'}} Administrador
                                        </q-btn>
                                    </div>
                                </q-form>
                              
                            </q-card-section>
                        </q-card>
                    </div>
                    
                </div>
            </div>
        </div>
    </q-page>
    
</template>
<script>
import Cropper from 'components/Cropper.vue';
import AreaTypeService from 'app/src/services/area-type/AreaTypeService';
import ManagerService from 'app/src/services/manager/ManagerService';
import { required, email } from 'app/src/common/rules';

const areaTypeService = new AreaTypeService();
const managerService = new ManagerService();

import { mapState } from 'vuex';

export default {
  components: { Cropper },
    created(){
        this.load();

        console.log(this.isVisibility)
    },
    data(){
        return {
            image:null,
            id:null,
            name:null,
            last_name:null,
            img:null,
            email:null,
            area:null,
            area_type_id:null,
            status:null,
            rules:{required,email},
            areaTypes:[]
        };
    },

    computed:{
        ...mapState('manager',{
            isEdit: state => state.isEdit,
            isVisibility: state => state.isVisibility
        })
    },
    methods:{

        async load(){
            this.$q.loading.show();
            await this.loadAreaTypes();
            await this.loadData();
            this.$q.loading.hide();
        },

        async loadData(){
            try {

                if(!this.isEdit) return;

                const { id } = this.$route.params;
                const { manager } = await managerService.getById(id);

                if(!manager) return

                this.id = manager.id;
                this.name = manager.name;
                this.last_name = manager.last_name;
                this.email = manager.email;
                this.area_type_id = manager.area_type_id;
                this.status = manager.status;
                this.img = manager.img 
                ? `${process.env.VUE_APP_URL_API}managers/get-image?filename=${manager.img}`
                : null;

            } catch (error) {

                console.log(error);
                
            }
            
        },

        async loadAreaTypes(){
            const {data} = await areaTypeService.getAll();
            this.areaTypes = data;
        },
        onResult(file){
            this.image = file;
        },
        async save(){

            if(!this.image && !this.isEdit) return this.$notify('Debe seleccionar una image','error');


            const valid = await this.$refs.form.validate();

            if(!valid) return;

            try {
                this.$q.loading.show();

                const form = new FormData();

                if(this.image) form.append('image', this.image);
                
                form.append('name', this.name);
                form.append('last_name', this.last_name);
                form.append('email', this.email);
                form.append('area_type_id', this.area_type_id);
                form.append('status', this.status);


                const response = !this.isEdit ? await managerService.insert(form) : await managerService.update(this.id, form);

                if(!response.success) {
                    return this.$notify(response.msg,'error');
                }

                this.$notify(response.msg);

                this.$router.push({name:'managers'})
            } catch (error) {
                this.$notify('Lo sentimos ocurrio un error','error');
            }finally {
                this.$q.loading.hide();
            }





        }

    }
    
}
</script>