<template>
	<div v-if="isLoading">Loading orders...</div>
	<div v-else>
		<div class="p-grid p-justify-center">
		  <div class="p-col-12 p-md-6">
			<div class="p-card">
			  <img :src="plate.picture" :alt="plate.plate_name" class="plate-image" />
			  <div class="p-card-title">{{ plate.plate_name }}</div>
			  <div class="p-card-subtitle">Price: {{ plate.price }} €</div>
			  <div class="p-card-content">
				<p>{{ plate.description }}</p>
			  </div>
			</div>
		  </div>
		</div>

		<!--  Commenting and Rating feature -->
        <div class="p-grid p-justify-center" v-if="userHasPlacedOrder">
		  <div class="p-col-12 p-md-6">
			  <h2>Leave a Comment</h2>
			   <div class="p-field">
                  <textarea id="comment" v-model="comment" rows="4"></textarea>
               </div>
		  </div>

		  <div class="p-col-12 p-md-6">
			  <h2>Rate this Plate</h2>
			  <div class="p-field">
                  <Rating v-model="rating" :cancel="false" :max="5"></Rating>
              </div>
		  </div>

		  <div class="p-field">
			<Button label="Submit" type="submit" />
		  </div>
		</div>

	</div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';
import { useRoute } from 'vue-router';
import Rating from 'primevue/rating';
import Button  from 'primevue/button';

const route = useRoute();
const plateId = route.params.plateId;
const plate = ref(null);
const userHasPlacedOrder = ref(false);
const comment = ref('');
const rating = ref(0);

const { isAuthenticated } = defineProps(['isAuthenticated']);
const userId = localStorage.getItem('userId');

const isLoading = ref(true);


// Fetching plate details using plateId
onMounted(async () => {

  try {
    const response = await fetch(`/api/plates/${plateId}`);
    if (response.ok) {
      plate.value = await response.json();
    } else {
      alert('Failed to fetch plate details');
      this.$router.push("/");
    }
  } catch (error) {
  	alert('An error occurred while fetching plate details');
  }

  if(isAuthenticated) {
	 const response = await fetch(`/api/orders/check-order/${userId}/${plateId}`);
	 const order_response = await response.json();
	 console.log(order_response);
	 userHasPlacedOrder.value = order_response.orderExists;
  }

  isLoading.value = false;
});

const submitReview = async (e) => {
  e.preventDefault();

  // You can send the comment and rating data to your backend and save it to the database.
  const reviewData = {
    plateId: plateId,
    userId: userId,
    comment: comment,
    rating: rating,
  };

  // Make an API request to save the review data (implement this part in your API).
  const URL_ORDERS = `https://localhost:8443/api/reviews/${userId}`
};

</script>

<style scoped>
.p-card {
  margin: 20px;
}

.p-card .p-card-title {
  margin: 10px;
}

.plate-image {
  max-width: 100%;
  max-height: 300px;
  margin: 10px;
  border-radius: 5px;
}
</style>
