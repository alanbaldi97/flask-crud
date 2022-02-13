
const routes = [
  {
    path: "/",
    redirect: {name: 'login'}
  },
  {
    path: "/login",
    component: () => import("pages/Login.vue"),
    name: 'login',
    meta: { auth: false }
  },
  {
    path: '/managers',
    component: () => import('layouts/MainLayout'),
    meta: { auth:true },
    children: [
      { 
        path: '', 
        component: () => import('pages/managers/Index.vue'), 
        name: 'managers',
        meta: { auth:true }
      },
      { 
        path: '/managers/manager/:id?', 
        component: () => import('pages/managers/AddEdit.vue'), 
        name:'add-edit-manager',
        meta: { auth:true }
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
