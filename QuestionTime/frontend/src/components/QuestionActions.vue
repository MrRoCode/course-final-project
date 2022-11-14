<template>
    <div class="question-actions">
        <router-link 
            class="btn btn-sm btn-outline-secondary my-1 me-1"
            :to="{name: 'question-editor', params: { slug: slug }}"
            >Modifica
        </router-link>
       
        <button
            class="btn btn-sm btn-outline-danger"
            @click="deleteQuestion"
            >Cancella
        </button>
    </div>
</template>

<script>
import { apiService } from '@/common/api.service';

    export default{
        name: "QuestionActions",
        props: {
            slug: {
                type: String,
                required: true

            }
        },
        methods: {
            async deleteQuestion(){
                let endpoint = `/api/questions/${this.slug}/`;
                try{
                    await apiService(endpoint, "DELETE");
                    this.$router.push("/");
                }catch (err){
                    console.log(err);
                }
            }
        }
    }
</script>