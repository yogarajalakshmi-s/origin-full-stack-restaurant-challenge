import { createRouter, createWebHashHistory } from 'vue-router'

import Menu from '@/components/Menu.vue'
import Orders from '@/components/Orders.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'
import LoginForm from '@/components/LoginForm.vue';


// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: '/menu', component: Menu, meta: { showOrdersTab: true } },
  { path: '/orders', component: Orders, meta: { showMenuTab: true } },
  { path: '/', component: RegistrationForm },
  { path: '/login', component: LoginForm}
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

export default router;
