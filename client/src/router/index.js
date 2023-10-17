import { createRouter, createWebHashHistory } from 'vue-router'

import Menu from '@/components/Menu.vue'
import Orders from '@/components/Orders.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'
import LoginForm from '@/components/LoginForm.vue';
import NotLoggedInMessage from '@/components/NotLoggedInMessage.vue';
import { isAuthenticated } from '@/store';

// Define a function to check authentication
const isAuthenticatedGuard = (to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated.value) {
    // If the route requires authentication and the user is not authenticated, redirect to the login page
    next({ name: 'not-logged-in' });
  } else {
    // For routes that don't require authentication or for authenticated users, proceed
    next();
  }
};

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
  { path: '/', component: Menu },
  {
    path: '/orders',
    component: Orders,
    meta: { requiresAuth: true } // Add a meta field for authentication requirement

  },
  { path: '/register', component: RegistrationForm },
  { path: '/login', component: LoginForm},
  { path: '/not-logged-in', name: 'not-logged-in', component: NotLoggedInMessage }, // Define a named route for NotLoggedInMessage
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

router.beforeEach(isAuthenticatedGuard); // Apply the authentication guard

export default router;
