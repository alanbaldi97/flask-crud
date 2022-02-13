<template>
    <div class="q-pa-md q-gutter-sm">
        <div v-show="onLoad" >
            <vue-croppie ref="croppie" 
            :enableOrientation="true" 
            :boundary="{ width: 150, height: 150}" >
            </vue-croppie>
            <div class="row justify-center">
                <q-btn class="text-weight-bolder" color="indigo-5" size="sm" @click="onCrop">Cortar</q-btn>
            </div>
        </div>
        

        
        <template v-if="!onLoad">
            <q-avatar size="150px">
                <img :src="getSource">
            </q-avatar>
            <div class="row justify-center">
                <q-btn :disable="disable" class="text-weight-bolder" color="indigo-5" size="sm" @click="openFileManager">Seleccionar imagen</q-btn>
            </div>
        </template>

        
    </div>
</template>
<script>
export default {
    props:{
        src:{
            type:String,
            default: null,
        },
        disable:{
            type: Boolean,
            default: false,
        }
    },
    data(){
        return {
            onLoad: false,
            source: this.src,
            cropped:null,
        }
    },
    computed:{
        getSource(){
            return this.source || 'https://cdn.quasar.dev/img/avatar.png';
        },
    },
    watch:{
        src(){
            this.source = this.src;
        }
    },
    methods:{
        openFileManager(){
            let input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*'
            input.onchange = (event) => {
                const file = event.target.files[0];
                this.source = URL.createObjectURL(file);
                this.$refs.croppie.bind({url: this.source });
                this.onLoad = true;
            }
            input.click();
        },
        async onCrop(){
            let options = {
                format: 'png', 
                circle: true
            }
            const output = await this.$refs.croppie.result(options);

            const response = await fetch(output);

            const blob = await response.blob();

            const filename = `image_${+new Date()}.${options.format}`  ;

            const file = new File([blob], filename, {type: "image/png"});
            
            this.source = URL.createObjectURL(file);

            this.onLoad = false;

            this.$emit('result',file);

        },

    }
    
}
</script>