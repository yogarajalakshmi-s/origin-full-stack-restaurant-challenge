import { createRouter, createWebHashHistory } from 'vue-router'

import Menu from '@/components/Menu.vue'
import Orders from '@/components/Orders.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'
import LoginForm from '@/components/LoginForm.vue';
import NotLoggedInMessage from '@/components/NotLoggedInMessage.vue';
import { isAuthenticated } from '@/store';

// Defining function to check authentication
const isAuthenticatedGuard = (to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated.value) {
    // If the route requires authentication and the user is not authenticated, redirecting to the login page
    next({ name: 'not-logged-in' });
  } else if (isAuthenticated.value && (to.path === '/login' || to.path === '/register')) {
    next('/'); // Redirecting to the menu page if authenticated user tries to access login or registration
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
    meta: { requiresAuth: true } // Adding a meta field for authentication requirement

  },
  { path: '/register', component: RegistrationForm },
  { path: '/login', component: LoginForm},
  { path: '/not-logged-in', name: 'not-logged-in', component: NotLoggedInMessage }, // Redirect to this page when users try to access pages other than Menu.
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

router.beforeEach(isAuthenticatedGuard); // Applying the authentication guard

export default router;
