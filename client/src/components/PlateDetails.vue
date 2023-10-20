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
		<div v-if="userHasPlacedOrder && !hasSubmittedReview">
			<div class="comment-section">
				<div class="comment-box">
					<form @submit="onSubmit" class="flex flex-column gap-2">
						<Textarea id="value" v-model="comment" rows="4" cols="30" />
						<Button @click="submitReview" type="submit" label="Submit" />
					</form>
				</div>

				<div class="rating-box">
					<Rating v-model="rating" :cancel="false" :max="5"></Rating>
				</div>
			</div>
		</div>

	</div>
</template>

<script setup>
import { ref, onMounted, defineProps, computed } from 'vue';
import { useRoute } from 'vue-router';
import Textarea from 'primevue/textarea';
import Rating from 'primevue/rating';
import Button  from 'primevue/button';

const route = useRoute();
const plateId = route.params.plateId;
const plate = ref(null);
const userHasPlacedOrder = ref(false);
const hasSubmittedReview = ref(false);

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

// Checking if user has submitted review for a particular plate - If true, user will not have option to comment and rate.
  const reviewResponse = await fetch(`/api/reviews/${userId}/${plateId}`);
  const reviewResponseData = await reviewResponse.json();
  hasSubmittedReview.value = reviewResponseData.reviewPresent;

  // Checking if user has placed an order on the particular plate.
  if(isAuthenticated) {

	 const response = await fetch(`/api/orders/check-order/${userId}/${plateId}`);
	 const order_response = await response.json();

	 // Displaying comment and rating feature, only if this is true.
	 userHasPlacedOrder.value = order_response.orderExists;
  }

  isLoading.value = false;

});


// Submitting comment and rating
const submitReview = async (e) => {

  const reviewData = {
    "plate_id": plateId,
    "user_id": userId,
    "comment": comment.value,
    "rating": rating.value,
  };

  console.log(comment.value);
  try {
    const response = await fetch(`https://localhost:8443/api/reviews/add-review`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviewData),
    });
    if (response.ok) {
	  userSubmittedReview.value = true;
	  window.location.reload();
    }
  } catch (error) {
      alert('An error occurred while submitting the review');
  }
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

.comment-section {
	display: flex;
	justify-content: space-around;
	width: 420px;
}

.comment-box {
	flex: 1;
	max-width: 60%;
}

.p-inputtext {
	resize: none;
}

.rating-box {
	width: 20%;
	margin-top: 1rem;
}

</style>
