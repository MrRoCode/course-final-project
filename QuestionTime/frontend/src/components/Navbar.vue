<!-- eslint-disable -->
<template>
    
    <nav class="navbar navbar-expand-lg navbar-light bg-light mynav">
        <div class="container">

            <router-link 
               class="navbar-brand" 
               :to="{ name: 'home'}"
               >QuestionTime
            </router-link>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <router-link 
                      :to="{ name: 'home'}" 
                      class="btn btn-warning me-1" 
                      aria-current="page"
                      >Home 
                    </router-link>
                </li>
                <li class="nav-item">
                   <router-link 
                      :to="{ name: 'question-editor'}" 
                      class="btn btn-danger" 
                      aria-current="page"
                      >Aggiungi domanda 
                    </router-link>
                </li>
                <li>
                    <a class="btn btn-outline-secondary ms-1" href="/accounts/logout/">Logout</a>
                </li>
              </ul>
            </div>
        </div>
    </nav>
    
  
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>
<style lang="css">
    .mynav{
        border-bottom: solid 2px #DDD;
    }
    .navbar-brand{
        font-weight: bold;
        font-size: 130%;
    }
    .navbar-brand:hover{
       color: red !important;
    }

</style>
