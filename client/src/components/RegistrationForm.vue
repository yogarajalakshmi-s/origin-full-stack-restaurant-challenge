<template>
  <div class="centered-form">
    <h2>Register</h2>
    <form @submit.prevent="registerUser">
      <InputText v-model="user.username" placeholder="Username" required />
      <InputText v-model="user.email" placeholder="Email" type="email" required />
      <p v-if="userAlreadyRegistered" class="error-message">User already exists! Please login.</p>
      <InputText v-model="user.password" placeholder="Password" type="password" required />
      <Button label="Register" type="submit"></Button>
    </form>
    <router-link to="/login">Login</router-link>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { setAuthenticated } from '@/store';
import InputText from 'primevue/inputtext';
import Button  from 'primevue/button';


export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      },
      userAlreadyRegistered: false // To skip registration when user already exists.
    };
  },
  components: {
    InputText,
    Button
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
            const responseData = await response.json();
            const userId = responseData.user_id;
            localStorage.setItem('userId', userId); // User id is set to access it across pages, on mounting.

            localStorage.setItem('userAuthenticated', 'true'); // To keep track of logged-in user.
            setAuthenticated(true);
            this.$router.push('/');
        } else {
           const responseText = await response.text();
           const message = JSON.parse(responseText)["detail"];

           if (message === "User already exists") {
             this.userAlreadyRegistered = true;
           }
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
  padding: 10px;
  margin: 10px 0;
}

.error-message {
  font-size: 14px;
  color: red;
  margin-top: 0px;
}

</style>
