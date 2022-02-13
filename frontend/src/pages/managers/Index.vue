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
import { mapActions } from 'vuex';
const managerService = new ManagerService();
export default {
    created(){
        this.loadManagers()
    },
    data(){
        return {
            managers:[],
            columns: columns
        }
    },
    methods:{

        ...mapActions('manager',['setIsEdit', 'setIsVisibilty']),

        getImage(manager){
            if(!manager.img) return '';
            return `${process.env.VUE_APP_URL_API}managers/get-image?filename=${manager.img}`
        },

        async loadManagers(){
            const data = await managerService.getAll();
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
        }
    }
    
}
</script>