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
						<div v-if="calculateAverageRating() === 0"></div> <!-- Hiding Average reviews when no reviews are given -->
						<div v-else>
							<strong>Average rating:</strong> {{ calculateAverageRating() }} / 5
						</div>
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
					<Rating v-model="rating" :max="5" :cancel="false"></Rating>
				</div>
			</div>
		</div>

		<div v-if="allReviews.length > 0">
			<h3>Reviews</h3>
			<div class="review">
				<div v-for="(review, index) in allReviews" :key="index" class="review-item">
					<div class="user-rating">
						<div class="user-info">
							<strong>{{ review.user.username }} </strong> [Rating: {{ review.rating }}/5]
						</div>
					</div>
					<div class="comment">{{ review.comment }}</div>
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
const allReviews = ref([]);

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

  // Checking if user has submitted review for a particular plate - If true, user will not be able to comment and rate.
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

  // Fetching all reviews of all users to display.
  const allReviewsResponse = await fetch(`/api/reviews/all?plate_id=${plateId}`);
  const allReviewsData = await allReviewsResponse.json();
  allReviews.value = allReviewsData;

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
    const response = await fetch(`/api/reviews/add-review`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviewData),
    });
    if (response.ok) {
	  window.location.reload();
    }
  } catch (error) {
      alert('An error occurred while submitting the review');
  }
};

function calculateAverageRating() {
  if (allReviews.value.length === 0) {
    return 0;
  }

  const totalRating = allReviews.value.reduce((total, review) => total + review.rating, 0);
  return (totalRating / allReviews.value.length).toFixed(1);
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

.review {
  text-align: left;
  display: grid;
  grid-gap: 20px;
}

.comment {
	margin-top: 5px;
}

.review-item {
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}

.user-rating {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.user-info {
  margin-right: 10px;
}

.comment {
  margin-top: 5px;
}
</style>
