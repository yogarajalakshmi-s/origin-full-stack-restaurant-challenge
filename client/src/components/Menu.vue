
<template>
    <div class="card">
        <DataView :value="plates" :layout="layout">
            <template #header>
                <div class="flex justify-content-end">
                    <DataViewLayoutOptions v-model="layout" />
                </div>
            </template>

            <template #list="slotProps">
                <div class="col-12">
					<router-link :to="{ name: 'plate-detail', params: { plateId: slotProps.data.plate_id } }">
						<div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
							<img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
							<div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
								<div class="flex flex-column align-items-center sm:align-items-start gap-3">
									<div class="text-2xl font-bold text-900">{{ slotProps.data.plate_name }}</div>
								</div>
								<div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
									<span class="text-2xl font-semibold">{{ slotProps.data.price }} € </span>
									<Button
										icon="pi pi-shopping-cart"
										@click="addToCart(slotProps.data)"
										rounded :disabled="slotProps.data.addedToCart">
									</Button>
								</div>
							</div>
						</div>
					</router-link>
                </div>
            </template>

            <template #grid="slotProps">
                <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2">
					<router-link :to="{ name: 'plate-detail', params: { plateId: slotProps.data.plate_id } }">
						<div class="p-4 border-1 surface-border surface-card border-round">
							<div class="flex flex-column align-items-center gap-3 py-5">
								<img class="w-9 shadow-2 border-round" :src="slotProps.data.picture" :alt="slotProps.data.plate_name" />
								<div class="text-2xl font-bold">{{ slotProps.data.plate_name }}</div>
							</div>
							<div class="flex align-items-center justify-content-between">
								<span class="text-2xl font-semibold">{{ slotProps.data.price }} €</span>
								<Button
									icon="pi pi-shopping-cart"
									@click="addToCart(slotProps.data)"
									rounded :disabled="slotProps.data.addedToCart">
								</Button>
							</div>
                    	</div>
                    </router-link>
                </div>
            </template>
        </DataView>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Button from 'primevue/button';
import { isAuthenticated } from '@/store';

import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions'   // optional


const plates = ref();
const layout = ref('grid');
const user = ref(null);

onMounted(async () => {
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();

    // Disabling cart button for items which are already present in shopping cart, by adding "addToCart" key.
    if (isAuthenticated.value) {
        const userId = localStorage.getItem('userId');

        // Finding items which are already added in the cart, filtering using user id.
        const cartItemsResponse = await fetch(`/api/cart-items/${userId}`);
        const cartItemsData = await cartItemsResponse.json();

        if (Array.isArray(cartItemsData) && cartItemsData.length > 0) {
          plates.value = data.map(plate => ({
            ...plate,
            addedToCart: cartItemsData.some(item => item.plate_id === plate.plate_id),
          }));
        } else {
            plates.value = data.map(plate => ({ ...plate, addedToCart: false }));
        }
    } else {
        plates.value = data.map(plate => ({ ...plate, addedToCart: false }));
    }

});

async function addToCart(plate) {
  if (!isAuthenticated.value) {
    alert('You are not authenticated. Please login to add dish to cart.');
    return;
  }

  if (!plate.addedToCart) {
    plate.addedToCart = true;

    const requestData = {
      id: null,
      user_id: localStorage.getItem('userId'),
      plate_id: plate.plate_id,
      plate_quantity: 1
    };

    try {
      // Adding items to the shopping cart
      const response = await fetch('/api/cart-items/add-to-cart', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (response.ok) {
        alert('Item added to the cart successfully.');
      } else {
        alert('Failed to add item to the cart.');
      }
    } catch (error) {
      alert('An error occurred while adding item to the cart');
    }
  } else {
    alert('Item is already in the cart.');
  }
}
</script>

<style scoped>
.text-2xl {
	color: black;
}
</style>