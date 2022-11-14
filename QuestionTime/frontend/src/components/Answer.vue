<template>
    <div class="single-answer">
        <p class="text-muted">
            <strong>@ {{ answer.author }}</strong>
             ha risposto il {{ answer.created_at }}
        </p>
        <p>
            {{ answer.body }}
        </p>
        <div v-if="isAnswerAuthor" class="answer-owner">
            <router-link
                :to="{ name: 'answer-editor', params: {id: answer.id}}"
                class="btn btn-sm btn-outline-secondary my-1 me-1"
                > <span>Modifica</span>
            </router-link>

            <button
                class="btn btn-sm btn-outline-danger"
                @click="triggerDeleteAnswer"
                >Cancella
            </button>
        </div>
        <div v-else class="like-answer">
            <button 
                class="btn btn-sm"
                :class="{
                    'btn-danger': userLikedAnswer,
                    'btn-outline-danger': !userLikedAnswer,
                }"
                @click="toogleLike"
                >
                <strong>Mi piace [{{ likesNumber }}]</strong>
            </button>
        </div>
        <hr class="line">
    </div>
</template>

<script>
import { apiService } from '@/common/api.service';

    export default{
        name: "AnswerComponent",
        props: {
            answer: {
                type: Object,
                required: true
            },
            requestUser: {
                type: String,
                required: true
            }
        },
        data(){
            return{
                userLikedAnswer: this.answer.user_has_voted,
                likesNumber: this.answer.likes_count
            }
        },
        computed:{
            isAnswerAuthor(){
                return this.answer.author === this.requestUser;
            }
        },
        methods: {
            triggerDeleteAnswer(){
                this.$emit("delete-answer", this.answer);
            },
            toogleLike(){
                this.userLikedAnswer === false
                    ? this.likeAnswer()
                    : this.unLikeAnswer()
            },
            likeAnswer(){
                this.userLikedAnswer = true;
                this.likesNumber += 1;
                let endpoint = `/api/answer/${this.answer.id}/like/`
                apiService(endpoint, "POST");
            },
            unLikeAnswer(){
                this.userLikedAnswer = false;
                this.likesNumber -= 1;
                let endpoint = `/api/answer/${this.answer.id}/like/`
                apiService(endpoint, "DELETE");
            }
        }
    }
</script>

<style>
    .line{
        border: dotted rgb(96, 179, 77);
    }
</style>