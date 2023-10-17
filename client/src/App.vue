<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref, computed, watch, onMounted } from 'vue';
import { setAuthenticated, isAuthenticated } from './store'; // Import the store
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const items = ref([
  { label: 'Register', to: '/register' },
  { label: 'Login', to: '/login' },
  { label: 'Menu', to: '/' },
  { label: 'Orders', to: '/orders' },
]);

const filteredItems = computed(() => {
  if (isAuthenticated.value) {
    return items.value.filter(item => item.to === '/' || item.to === '/orders');
  } else {
        if (route.path === '/') {
          return items.value.filter(item => item.to === '/register' || item.to === '/login');
        } else if (route.path === '/login' || route.path === 'register') {
           return []
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

watch(isAuthenticated, (newValue) => {
   if (!newValue) {
    localStorage.setItem('userAuthenticated', 'false');

    setTimeout(() => {
      router.push('/login');
    }, 5000); // 5000 milliseconds = 5 seconds
  } else {
    localStorage.setItem('userAuthenticated', 'true');
  }
});

</script>

<template>
  <div class="top-0">
    <TabMenu :model="filteredItems" />
    <router-view :isAuthenticated="isAuthenticated" @update-auth="isAuthenticated = $event" />
  </div>
</template>

<style scoped>

</style>
