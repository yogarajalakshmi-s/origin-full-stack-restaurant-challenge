<template>
  <body>
      <div class="registration-form centered-form">
        <h2>Register</h2>
        <form @submit.prevent="registerUser">
          <input v-model="user.username" placeholder="Username" required>
          <input v-model="user.email" placeholder="Email" type="email" required>
          <p v-if="userAlreadyRegistered" class="error-message">User already exists! Please login.</p>
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
import { setAuthenticated } from '@/store'; // Import the store


export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      },
      userAlreadyRegistered: false
    };
  },
  methods: {
    async registerUser() {

      try {
        const response = await fetch('/api/users/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)
        });
        if (response.ok) {
          const responseText = await response.text();
          if (responseText === '"User already exists! Please login."') {
            this.userAlreadyRegistered = true;
            console.log("Response Text:", responseText);
          } else {
            localStorage.setItem('userAuthenticated', 'true');
            setAuthenticated(true);
            this.$router.push('/');
          }
        } else {
          alert('Registration failed.');
        }
      } catch (error) {
        console.error(error);
        alert('An error occurred when trying to register. Please try again.');
      }
    }

  }
}
</script>

<style scoped>

.centered-form {
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

.error-message {
  font-size: 10px;
  color: red;
  margin-top: 0px;
}
</style>
