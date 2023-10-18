<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref, computed, onMounted } from 'vue';
import { setAuthenticated, isAuthenticated } from './store';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const items = ref([
  { label: 'Register', to: '/register' },
  { label: 'Login', to: '/login' },
  { label: 'Menu', to: '/' },
  { label: 'Orders', to: '/orders' },
  { label: 'Shopping Cart', icon: 'pi pi-shopping-cart', to: '/cart-items' },
  { label: 'Logout', icon: 'pi pi-power-off', to: '/logout' }
]);

const filteredItems = computed(() => {
  if (isAuthenticated.value) {

    // When user is logged in, showing all relevant tabs on all pages.
    return items.value.filter(item => item.to === '/' || item.to === '/orders' || item.to === '/cart-items' || item.to === '/logout');
  } else {
        // When user is not logged in, showing only Login and Register tab on the Menu page.
        if (route.path === '/') {
          return items.value.filter(item => item.to === '/register' || item.to === '/login');
        } else {
          return [];
        }
  }
});

// Checking if the user is authenticated in local storage on component mount
onMounted(() => {
  const userAuthenticated = localStorage.getItem('userAuthenticated');
  if (userAuthenticated === 'true') {
    setAuthenticated(true);
  }
});

// Handling logout
function handleTabChange(event) {
  if (event.originalEvent.target.innerText === 'Logout') {
    performLogout();
  }
}

// Removing all keys set during login and redirecting user to login page after Logout tab is clicked.
function performLogout() {
  setAuthenticated(false);
  localStorage.removeItem('userAuthenticated');
  localStorage.removeItem('userId');
  router.push('/login');
}

</script>

<template>
  <div class="page">
    <h1 class="title">Origin Restaurant</h1>
    <div class="top-0">
      <TabMenu :model="filteredItems" @tab-change="handleTabChange"  />
      <router-view :isAuthenticated="isAuthenticated" @update-auth="isAuthenticated = $event" />
    </div>
  </div>
</template>

<style scoped>
   .page {
    text-align: center;
    font-family: 'Lato', sans-serif;
  }

  .title {
    font-size: 36px;
    margin-top: 20px;
  }
</style>
