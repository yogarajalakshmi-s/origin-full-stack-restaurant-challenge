<template>
    <NotLoggedInMessage v-if="!isAuthenticated" />
    <div class="no-items" v-if="plates.length === 0"> There are no items in the cart. </div>
    <div class="p-grid">
    <div class="p-col-12 p-md-6" v-for="plate in plates" :key="plate.id">
      <div class="p-card p-shadow-2">
        <div class="p-card-content">
          <div class="p-card-flex">
             <button @click="removePlate(plate)" class="p-button p-button-icon p-button-danger p-button-xs custom-remove-button">
               <i class="pi pi-times"></i>
             </button>
            <div class="p-card-image">
              <img :src="plate.picture" :alt="plate.plate_name" class="p-card-image" />
            </div>
            <div class="p-card-details">
              <div class="p-card-header p-card-flex">
                <div class="p-card-title">{{ plate.plate_name }}</div>
                <div class="p-card-subtitle">{{ plate.price }} €</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="plates.length > 0">
      <div class="p-col-12">
        <div class="p-card p-shadow-2">
          <div class="p-card-content">
            <div class="p-card-total">
              Total Price: {{ calculateTotalPrice() }} €
            </div>
          </div>
        </div>
      </div>

      <div class="p-col-12">
        <button class="p-button p-button-primary p-button-lg" @click="placeOrder">Place Order</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';

const { isAuthenticated } = defineProps(['isAuthenticated']);
const plates = ref([]);
const userId = localStorage.getItem('userId');

onMounted(async () => {
  const response = await fetch(`/api/cart-items/items/${userId}`);
  const data = await response.json();
  plates.value = data;
});

function calculateTotalPrice() {
  return plates.value.reduce((total, plate) => total + plate.price, 0).toFixed(2);
}

// Removing item from cart
async function removePlate(plate) {
  const plateName = plate.plate_name
  console.log(plate.plate_id)

  try {
    const response = await fetch(`/api/cart-items/remove/${plate.plate_id}/${userId}`, {
      method: 'DELETE'
    });

    if (response.ok) {
      alert(plateName + " removed from cart.");
      window.location.reload();
    } else {
      alert("Failed to remove " + plateName + " from cart.");
    }
  } catch (error) {
    alert("An error occurred while removing " + plateName + " from cart.");
  }
}

// Placing order from cart
async function placeOrder(plate) {
	const cartItemsResponse = await fetch(`/api/cart-items/${userId}`);
    const cartItemsData = await cartItemsResponse.json();

  try {
    const response = await fetch(`/api/orders/add-new-order/${userId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(cartItemsData),
    });

    if (response.ok) {
      alert("Order placed successfully 🥘");
      window.location.reload();
    } else {
      alert("Failed to place order. Please try again after some time.");
    }
  } catch (error) {
    alert("An error occurred while placing order.");
  }
}

</script>

<style scoped>

.p-card-flex {
  display: flex;
  align-items: center;
}

.p-card-content {
  padding: 1.25rem 1rem;
  margin: 10px;
}

.p-card-details {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.p-card .p-card-title {
  font-size: 20px;
}

.p-card-subtitle {
  text-align: right;
}

.p-card-title, .p-card-subtitle {
  display: inline-block;
  margin-right: 10px;
}

.p-card-image {
  max-width: 100px;
  margin-right: 25px;
  margin-left: 10px;
  border-radius: 8px;
}

.p-card-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.p-card-total {
  text-align: right;
  font-weight: bold;
  margin-top: 10px;
  margin-right: 10px;
}

.p-button-danger {
  margin-left: 1rem;
}

.custom-remove-button {
  padding: 0.25rem 0.5rem;
  font-size: 14px;
}

.no-items {
  margin-top: 20px;
  font-size: 20px;
}

.p-button-lg {
  background-color: green;
  margin-top: 10px
}
</style>
