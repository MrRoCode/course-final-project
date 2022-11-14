
<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>
<script>
import { apiService } from "./common/api.service";
import NavbarComponent from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    NavbarComponent,
  },
  data(){
    return{
      userUsername: null
    }
  },
  methods: {
    async setUserInfo(){
      await apiService("/api/user/")
        .then(result => {
          console.log("user:" + result.username)
          this.userUsername = result.username;
          window.localStorage.setItem("username", this.userUsername);
        })
    }
  },
  created(){
    this.setUserInfo();
  }
}
</script>
<!-- eslint-disable -->
<style>
body{
      font-family: 'Playfair Display', serif;
    }
.btn{
  box-shadow: none !important;
}
</style>
