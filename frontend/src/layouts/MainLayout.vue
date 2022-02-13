<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="background-color">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
         
        </q-toolbar-title>

        <div>
          <q-btn size="md" flat dense class="q-ml-sm bg-transparent text-white q-mr-sm" >
            {{ user.username.toLowerCase() }}
            <q-menu >
              <q-list >
                <q-item clickable @click="logout">
                  <q-item-section >
                    Cerrar Sesión
                  </q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          <!-- Essential Links -->
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
      <q-ajax-bar
        ref="bar"
        position="top"
        color="deep-purple-4"
        size="5px"
        skip-hijack
      />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'
import { mapState } from 'vuex';
import EventBus from 'app/src/common/event-bus';
import { AuthService } from '../services/auth/AuthService';

const authService = new AuthService();

const linksData = [
  {
    title: 'Administradores',
    // caption: 'quasar.dev',
    icon: 'people',
    routeName: 'managers'
  },
  // {
  //   title: 'Github',
  //   caption: 'github.com/quasarframework',
  //   icon: 'code',
  //   link: 'https://github.com/quasarframework'
  // },
  // {
  //   title: 'Discord Chat Channel',
  //   caption: 'chat.quasar.dev',
  //   icon: 'chat',
  //   link: 'https://chat.quasar.dev'
  // },
  // {
  //   title: 'Forum',
  //   caption: 'forum.quasar.dev',
  //   icon: 'record_voice_over',
  //   link: 'https://forum.quasar.dev'
  // },
  // {
  //   title: 'Twitter',
  //   caption: '@quasarframework',
  //   icon: 'rss_feed',
  //   link: 'https://twitter.quasar.dev'
  // },
  // {
  //   title: 'Facebook',
  //   caption: '@QuasarFramework',
  //   icon: 'public',
  //   link: 'https://facebook.quasar.dev'
  // },
  // {
  //   title: 'Quasar Awesome',
  //   caption: 'Community Quasar projects',
  //   icon: 'favorite',
  //   link: 'https://awesome.quasar.dev'
  // }
];

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  created(){

    EventBus.$on('visible-bar',() => {
      this.bar.start();
    });

    EventBus.$on('hide-bar',() => {
      this.bar.stop();
    });

  },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData,
      bar:null
    }
  },
  mounted(){
    this.$nextTick(()=> {
      this.bar = this.$refs.bar;
    })
  },
  computed:{

    ...mapState('auth',['user'])

  },
  methods:{
    async logout(){

      try{

        this.$q.loading.show();

        const response = await authService.logout();

        if(!response.success){
          return this.$notify(response.msg,'error');
        }

        this.$router.push('/');

      }catch(error){
        this.$serverError(error);
      }finally{
        this.$q.loading.hide();
      }

    }
  }
}
</script>
