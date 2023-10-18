<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref, computed, onMounted } from 'vue';
import { setAuthenticated, isAuthenticated } from './store'; // Import the store
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const items = ref([
  { label: 'Register', to: '/register' },
  { label: 'Login', to: '/login' },
  { label: 'Menu', to: '/' },
  { label: 'Orders', to: '/orders' },
  { label: 'Cart', to: '/shopping-cart' },
  { label: 'Logout', icon: 'pi pi-power-off', to: '/logout' }
]);

const filteredItems = computed(() => {
  if (isAuthenticated.value) {
    return items.value.filter(item => item.to === '/' || item.to === '/orders' || item.to === '/logout');
  } else {
        if (route.path === '/') {
          return items.value.filter(item => item.to === '/register' || item.to === '/login');
        } else {
          return [];
        }
  }
});

// Check if the user is authenticated in local storage on component mount
onMounted(() => {
  const userAuthenticated = localStorage.getItem('userAuthenticated');
  if (userAuthenticated === 'true') {
    setAuthenticated(true);
  }
});

function handleTabChange(event) {
  if (event.originalEvent.target.innerText === 'Logout') {
    performLogout();
  }
}

function performLogout() {
  setAuthenticated(false);
  localStorage.removeItem('userAuthenticated');
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
