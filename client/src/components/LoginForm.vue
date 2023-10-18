<template>
  <div class="login-form centered-form">
    <div class="login-container">
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <input v-model="user.email" placeholder="Email" type="email" @input="resetError" required>
        <p v-if="userNotRegistered" class="error-message">User is not registered. Please register!</p>
        <input v-model="user.password" placeholder="Password" type="password" required>
        <p v-if="incorrectPassword" class="error-message">Please enter the correct password!</p>
        <button type="submit">Login</button>
      </form>
      <router-link to="/register">Register</router-link>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { setAuthenticated } from '@/store';

export default {
  data() {
    return {
      user: {
        email: "",
        password: ""
      },
      userNotRegistered: false,
      incorrectPassword: false,
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
            localStorage.setItem('userAuthenticated', 'true');
            setAuthenticated(true);
            this.$router.push("/");
        } else {
            const responseText = await response.text();
            const message = JSON.parse(responseText)["detail"];

            if (message === "User does not exist") {
              this.userNotRegistered = true;
            }
            else if (message === "Incorrect password") {
              this.incorrectPassword = true;
            }
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

.centered-form {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
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

.error-message {
  font-size: 14px;
  color: red;
  margin-top: 0px;
}

</style>


