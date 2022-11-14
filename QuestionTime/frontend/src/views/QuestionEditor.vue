<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Aggiungi una domanda</h1>
                <form @submit.prevent="onSubmit">
                    <textarea rows="3"
                              class="form-control"
                              placeholder="Cosa vuoi chiedere?"
                              v-model="questionBody">
                    </textarea>
                    <br>
                    <button class="btn btn-success"
                            type="submit"
                            >Pubblica domanada
                    </button>
                </form>
                <p class="muted error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import { apiService } from '@/common/api.service';

    export default{
        name: "QuestionEditor",
        props: {
            slug:{
                type: String,
                required: false
            },
            previousQuestion:{
                type: String,
                required: false
            }
        },

        data(){
            return{
                questionBody: this.previousQuestion || null,
                error: null
            }
        },

        async beforeRouteEnter(to, from, next){
            if (to.params.slug !== undefined){
                let endpoint = `/api/questions/${to.params.slug}/`;
                await apiService(endpoint)
                    .then((data)=>{
                        to.params.previousQuestion = data.content;
                    })
            }
            return next();
        },

        methods: {
            onSubmit(){
                if (! this.questionBody){
                    this.error = "Scrivi qualcosa"
                }else if (this.questionBody.length > 240){
                    this.error = "Hai sperato 240 caratteri consentiti!"
                }else {
                    let endpoint = "/api/questions/";
                    let method = "POST";
                    if (this.previousQuestion){
                        method = "PUT";
                        endpoint += `${this.slug}/`;
                    }
                    apiService(endpoint, method, { content: this.questionBody })
                        .then(question_data => {
                            this.$router.push({
                                name: "question",
                                params: { slug: question_data.slug }
                            });
                        })
                }
            }
        },

        created(){
            document.title = "Editor - QuestionTime";
        }
    }
</script>

<style>

</style>