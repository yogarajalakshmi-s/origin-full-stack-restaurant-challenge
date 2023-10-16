<template>
  <div  class="background-image">
      <div class="login-form centered-form">
        <div class="login-container">
          <h2>Login</h2>
          <form @submit.prevent="loginUser">
            <input v-model="user.email" placeholder="Email" type="email" required>
            <input v-model="user.password" placeholder="Password" type="password" required>
            <button type="submit">Login</button>
          </form>
          <router-link to="/">Register</router-link>
        </div>
      </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      user: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await fetch("/api/users/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.user)
        });

        if (response.ok) {
          const data = await response.json();
          // Save the token to localStorage or Vuex store
          localStorage.setItem("access_token", data.access_token);

          // Redirect to the Menu page or any other route
          this.$router.push("/menu");
        } else {
          alert("Login failed.");
        }
      } catch (error) {
        console.error(error);
        alert("An error occurred.");
      }
    }
  }
};
</script>

<style scoped>
.background-image {
  background-image: url("/restaurant.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
}

.centered-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.registration-form {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
}

h2 {
  font-size: 24px;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  margin: 10px 0;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  background-color: #646cff;
  color: white;
  font-weight: 500;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

</style>
