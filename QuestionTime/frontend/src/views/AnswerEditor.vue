<template>
  <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 class="mb-3">Modifica la tua risposta</h1>
                <form @submit.prevent="onSubmit">
                    <textarea rows="3"
                              class="form-control"
                              v-model="answerBody">
                    </textarea>
                    <br>
                    <button class="btn btn-success"
                            type="submit"
                            >Pubblica risposta
                    </button>
                </form>
                <p class="error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from '@/common/api.service';

export default{
    props: {
        id: {
            type: String,
            required: true
        },
        previousAnswer: {
            type: String,
            required: true
        },
        questionSlug: {
            type: String,
            required: true
        }
    },

    async beforeRouteEnter(to, from, next){
        let endpoint = `/api/answer/${to.params.id}/`;
        await apiService(endpoint)
                .then(data => {
                    to.params.previousAnswer = data.body;
                    to.params.questionSlug = data.question_slug;
                })
        return next();
    },

    data(){
        return{
            answerBody: this.previousAnswer,
            error: null
        }
    },
    methods: {
        onSubmit(){
            if (this.answerBody){
                let endpoint = `/api/answer/${this.id}/`;
                apiService(endpoint, "PUT", {body: this.answerBody})
                .then(()=>{
                    this.$router.push({
                        name: "question",
                        params: { slug: this.questionSlug}
                    })
                })
            }else{
                this.error = "Scrivi qualcosa!";
            }
        }
    }
    // methods:{
    //     async getAnswerData(){
    //         let endpoint = `/api/answer/${this.id}/`;
    //         await apiService(endpoint)
    //             .then(data => {
    //                 this.answerBody = data.body;
    //             })
    //     }
    // },
    // created(){
    //     this.getAnswerData();
    // }
}
</script>

<style>

</style>