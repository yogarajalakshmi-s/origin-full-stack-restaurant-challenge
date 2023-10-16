<template>
  <div class="top-0">
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, onBeforeRouteUpdate } from 'vue-router';

const items = ref([]);

// Function to toggle tab visibility based on the current route
const updateTabVisibility = () => {
  const route = useRoute();
  items.value = [
    { label: 'Register', to: '/', show: route.path === '/' },
    { label: 'Register', to: '/login' },
    { label: 'Menu', to: '/menu', show: route.meta.showOrdersTab },
    { label: 'Orders', to: '/orders', show: route.meta.showMenuTab },
  ];
};

onBeforeRouteUpdate(updateTabVisibility);

// Initialize tab visibility on component mount
updateTabVisibility();
</script>
