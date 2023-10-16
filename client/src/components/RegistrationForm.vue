<template>
  <body>
      <div class="registration-form centered-form">
        <h2>Register</h2>
        <form @submit.prevent="registerUser">
          <input v-model="user.username" placeholder="Username" required>
          <input v-model="user.email" placeholder="Email" type="email" required>
          <input v-model="user.password" placeholder="Password" type="password" required>
          <button type="submit">Register</button>
        </form>
        <router-link to="/login">Login</router-link>
      </div>
  </body>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      }
    };
  },
  methods: {
    async registerUser() {
      try {
        // Make an API request to the backend to register the user
        const response = await fetch('/api/users/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)
        });
        if (response.ok) {
          // Registration successful, redirect to the Menu
          this.$router.push('/menu');
        } else {
          alert('Registration failed.');
        }
      } catch (error) {
        console.error(error);
        alert('An error occurred.');
      }
    }
  }
}
</script>

<style scoped>

body {
body {
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

