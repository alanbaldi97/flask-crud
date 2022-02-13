<template>

    <q-page>
        <div class="row">
            <div class="q-pa-md q-gutter-sm">
                <q-breadcrumbs gutter="none">
                    <q-breadcrumbs-el label="Inicio"  />
                    <q-breadcrumbs-el label="Administradores"  />
                </q-breadcrumbs>
            </div>
        </div>
        <div class="row q-pa-md">
            <div class="col-12 col-md-12 row justify-end" >
            <q-btn color="indigo-5" icon="add" rounded @click="addManager">

            </q-btn>
            </div>
            <div class="col-12 col-md-12 q-mt-md" >
                <q-table title="Administradores" :data="managers" :columns="columns">

                    <template v-slot:top>
                       
                        <q-input outlined bottom-slots dense debounce="300" color="primary" v-model="filter.search" @keypress.enter="search" placeholder="Buscar">
                            
                            <template v-slot:before>
                                <q-btn size="md" dense icon="filter_alt" class="q-ml-sm bg-indigo text-white q-mr-sm" @click="show = true" >
                                    <q-menu >
                                        <q-list class="q-pa-sm" style="min-width: 300px">
                                            <q-item>
                                                <q-item-section>Filtros de búsqueda</q-item-section>
                                                <q-space />
                                                <q-btn flat size="sm" v-close-popup icon="clear" dense class="q-ml-sm text-black bg-white" />
                                            </q-item>
                                            <q-separator />
                                            <q-item>
                                                <q-item-section>
                                                    <q-select 
                                                    option-value="id" 
                                                    option-label="name"
                                                    v-model="filter.area_type_id"
                                                    dense outlined 
                                                    :options="areaTypes" 
                                                    label="Tipo de Area" 
                                                    emit-value
                                                    map-options ></q-select>
                                                </q-item-section>
                                            </q-item>
                                            <q-item>
                                                <q-item-section>
                                                    <q-select v-model="filter.status" dense outlined :options="['Activo', 'Inactivo']" label="Estado" ></q-select>
                                                </q-item-section>
                                            </q-item>

                                            <q-separator />
                                            <q-item>
                                                <q-item-section>
                                                    <div class="row justify-center">
                                                        <q-btn size="md" dense outline class="q-mr-sm" label="Limpiar" @click="cleanFilter" />
                                                        <q-btn size="md" v-close-popup color="indigo-6" outline label="Aplicar filtros" dense  />
                                                    </div>
                                                </q-item-section>
                                            </q-item>
                                        </q-list>
                                    </q-menu>
                                </q-btn>
                                
                            </template>
                            
                            <template v-slot:prepend>
                                <q-icon name="search" />
                            </template>
                            <template v-slot:after>
                                <q-btn size="md" icon="search" dense class="q-ml-sm bg-indigo text-white" @click="search" />
                            </template>
                        </q-input>                    
                        
                    </template>
                    <template v-slot:body-cell-avatar="props">
                        <q-td :props="props">
                            <q-avatar size="50px">
                                <img :src="getImage(props.row)">
                            </q-avatar>
                        </q-td>
                     </template>
                    <template v-slot:body-cell-status="props">
                        <q-td :props="props">
                           <q-chip :color="props.row.status == 'Activo' ? 'green-13' : 'red-13' " >
                                <span class="text-bold">{{ props.row.status }}</span>
                            </q-chip>
                        </q-td>
                        
                    </template>
                    <template v-slot:body-cell-actions="props">
                        <q-td :props="props">
                            <q-btn color="indigo-3" size="md" icon="edit" round flat  @click="onEdit(props.row)">
                                <q-tooltip content-class="bg-indigo" :offset="[10, 10]">
                                    Editar
                                </q-tooltip>
                            </q-btn>
                            <q-btn color="red" size="md" icon="delete" round flat  @click="onDelete(props.row)">
                                <q-tooltip content-class="bg-indigo" :offset="[10, 10]">
                                    Eliminar
                                </q-tooltip>
                            </q-btn>
                            <q-btn color="indigo-3" size="md" icon="visibility" round flat  @click="onVisibility(props.row)">
                                <q-tooltip content-class="bg-indigo" :offset="[10, 10]">
                                    Visualizar
                                </q-tooltip>
                            </q-btn>
                        </q-td>
                        
                    </template>
                </q-table>
            </div>
            
        </div>
    </q-page>
    

</template>
<script>
import columns from '../../config-tables/config-table-manager';
import ManagerService from 'app/src/services/manager/ManagerService';
import AreaTypeService from 'app/src/services/area-type/AreaTypeService';
import { mapActions } from 'vuex';
const areaTypeService = new AreaTypeService();
const managerService = new ManagerService();
export default {
    created(){
        this.loadManagers()
        this.loadAreaTypes();
    },
    data(){
        return {
            managers:[],
            columns: columns,
            show:false,
            areaTypes:[],
            filter:{
                search:null,
                area_type_id:null,
                status: null,
            }
        }
    },
    methods:{

        ...mapActions('manager',['setIsEdit', 'setIsVisibilty']),

        async loadAreaTypes(){
            const {data} = await areaTypeService.getAll();
            this.areaTypes = data;
        },
        getImage(manager){
            if(!manager.img) return '';
            return `${process.env.VUE_APP_URL_API}managers/get-image?filename=${manager.img}`
        },

        async loadManagers(){
            const data = await managerService.getAll(this.filter);
            this.managers = data;
        },
        onEdit(manager){
            this.setIsVisibilty(false);
            this.setIsEdit(true);
            this.$router.push({
                name:'add-edit-manager',
                params: {
                    id: manager.id
                }
            })

        },
        addManager(){
            this.setIsEdit(false);
            this.setIsVisibilty(false);
            this.$router.push({name:'add-edit-manager'})
        },

        async onDelete(manager){

            const confirm = await this.$confirm('¿Desea eliminar el registro?','Este proceso es irreversible');

            if(!confirm) return;

            try {
                this.$q.loading.show();

                const response = await managerService.deleteManager(manager.id);

                if(!response.success) {
                    return this.$notify(response.msg,'error');
                }

                this.$notify(response.msg);
                this.loadManagers();
            } catch (error) {
                console.log(error);
                this.$serverError(error);
            }finally {
                this.$q.loading.hide();
            }

        },

        onVisibility(manager){

            this.setIsVisibilty(true);
            this.setIsEdit(true);

            this.$router.push({
                name:'add-edit-manager',
                params: {
                    id: manager.id
                }
            })
        },

        cleanFilter(){

            this.filter.area_type_id = null;
            this.filter.search = null;
            this.filter.status = null;

        },
        search(){
            this.loadManagers();
        }
    }
    
}
</script>