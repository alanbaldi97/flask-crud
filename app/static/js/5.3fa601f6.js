(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[5],{"713b":function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-layout",{attrs:{view:"lHh Lpr lFf"}},[a("q-header",{attrs:{elevated:""}},[a("q-toolbar",{staticClass:"background-color"},[a("q-btn",{attrs:{flat:"",dense:"",round:"",icon:"menu","aria-label":"Menu"},on:{click:function(t){e.leftDrawerOpen=!e.leftDrawerOpen}}}),a("q-toolbar-title"),a("div",[a("q-btn",{staticClass:"q-ml-sm bg-transparent text-white q-mr-sm",attrs:{size:"md",flat:"",dense:""}},[e._v("\n          "+e._s(e.user.username.toLowerCase())+"\n          "),a("q-menu",[a("q-list",[a("q-item",{attrs:{clickable:""},on:{click:e.logout}},[a("q-item-section",[e._v("\n                  Cerrar Sesión\n                ")])],1)],1)],1)],1)],1)],1)],1),a("q-drawer",{attrs:{"show-if-above":"",bordered:"","content-class":"bg-grey-1"},model:{value:e.leftDrawerOpen,callback:function(t){e.leftDrawerOpen=t},expression:"leftDrawerOpen"}},[a("q-list",[a("q-item-label",{staticClass:"text-grey-8",attrs:{header:""}}),e._l(e.essentialLinks,(function(t){return a("EssentialLink",e._b({key:t.title},"EssentialLink",t,!1))}))],2)],1),a("q-page-container",[a("router-view"),a("q-ajax-bar",{ref:"bar",attrs:{position:"top",color:"deep-purple-4",size:"5px","skip-hijack":""}})],1)],1)},n=[],i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"text-muted",attrs:{clickable:"",to:{name:e.routeName}}},[e.icon?a("q-item-section",{attrs:{avatar:""}},[a("q-icon",{attrs:{name:e.icon}})],1):e._e(),a("q-item-section",[a("q-item-label",[e._v(e._s(e.title))]),a("q-item-label",{attrs:{caption:""}},[e._v("\n      "+e._s(e.caption)+"\n    ")])],1)],1)},s=[],l={name:"EssentialLink",props:{title:{type:String,required:!0},caption:{type:String,default:""},routeName:{type:String,default:"#"},icon:{type:String,default:""}}},o=l,c=a("2877"),u=a("66e5"),p=a("4074"),m=a("0016"),b=a("0170"),d=a("714f"),f=a("eebe"),h=a.n(f),q=Object(c["a"])(o,i,s,!1,null,null,null),w=q.exports;h()(q,"components",{QItem:u["a"],QItemSection:p["a"],QIcon:m["a"],QItemLabel:b["a"]}),h()(q,"directives",{Ripple:d["a"]});var v=a("2f62"),g=a("6f9e"),k=a("4a78");const Q=new k["a"],y=[{title:"Administradores",icon:"people",routeName:"managers"}];var _={name:"MainLayout",components:{EssentialLink:w},created(){g["a"].$on("visible-bar",(()=>{this.bar.start()})),g["a"].$on("hide-bar",(()=>{this.bar.stop()}))},data(){return{leftDrawerOpen:!1,essentialLinks:y,bar:null}},mounted(){this.$nextTick((()=>{this.bar=this.$refs.bar}))},computed:{...Object(v["c"])("auth",["user"])},methods:{async logout(){try{this.$q.loading.show();const e=await Q.logout();if(!e.success)return this.$notify(e.msg,"error");this.$router.push("/")}catch(e){this.$serverError(e)}finally{this.$q.loading.hide()}}}},L=_,$=a("4d5a"),x=a("e359"),O=a("65c6"),C=a("9c40"),D=a("6ac5"),E=a("4e73"),I=a("1c1c"),S=a("9404"),j=a("09e3"),N=a("7ea5"),T=Object(c["a"])(L,r,n,!1,null,null,null);t["default"]=T.exports;h()(T,"components",{QLayout:$["a"],QHeader:x["a"],QToolbar:O["a"],QBtn:C["a"],QToolbarTitle:D["a"],QMenu:E["a"],QList:I["a"],QItem:u["a"],QItemSection:p["a"],QDrawer:S["a"],QItemLabel:b["a"],QPageContainer:j["a"],QAjaxBar:N["a"]})}}]);