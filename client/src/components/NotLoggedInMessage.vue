<template>
  <div class="not-logged-in-message">
    <p>You are not logged in. Please <router-link to="/login">log in</router-link> or <router-link to="/register">register</router-link> to access this page.</p>
  </div>
</template>

<script>
export default {
  name: 'NotLoggedInMessage',
};
</script>
