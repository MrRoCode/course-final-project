<template>
    <div class="singel-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>

            <QuestionActions
                v-if="isOwner"
                :slug="slug"
            />

            <p class="mb-0">
            Domanda aggiunta da: <span class="author-name">{{ question.author }}</span>
          </p>
          <p>{{ question.created_at }}</p>
          <hr>
          <template v-if="userHasAnswered">
            <p class="answer-added">Hai gia risposto a questa domanda</p>
          </template>
          <template v-else-if="showForm">
            <form class="card"  @submit.prevent="onSubmit">
                <div class="card-header px-3">
                    Aggiungi una risposta alla domanda
                </div>
                <div>
                    <textarea 
                        rows="5"
                        class="form-control"
                        placeholder="Aggiungi una risposta alla domanda"
                        v-model="newAnswerBody">
                    </textarea>
                </div>
                <div class="card-footer px-3">
                    <button type="submit" 
                            class="btn btn-success"
                            >Aggiungi 
                    </button>
                </div>
                <p class="error ms-2 mt-2">{{ error }}</p>
            </form>
          </template>
          <template v-else>
            <button class="btn btn-sm btn-success"
                    @click= "showForm = true"
                    >Rispondi
            </button>
          </template>
          <AnswerComponent
            v-for="(answer, index) in answers"
            :answer="answer"
            :requestUser="requestUser"
            @delete-answer="deleteAnswer"
            :key="answer.id"
          />
          <p v-show="loadinAnswers">...loadind...</p>
          <div class="my-4">
                <p v-show="loadinAnswers">...loading...</p>
                <button v-show="next"
                        @click="getQuestionAnswer"
                        class="btn btn-sm btn-outline-success"
                        >Carica ancora
                </button>
          </div>
        </div>
    </div>
</template>

<script>
import { apiService } from '@/common/api.service';
import AnswerComponent from '../components/Answer.vue';
import QuestionActions from '@/components/QuestionActions.vue';

    export default{
        name: "QuestionView",

        props: {
            slug: {
                type: String,
                required: true
            }
        },

        components:{
    AnswerComponent,
    QuestionActions
},

        data(){
            return{
                question: {},
                loadinAnswers: false,
                answers: [],
                userHasAnswered: false,
                showForm: false,
                newAnswerBody: null,
                error: null,
                next: null,
                requestUser: null
            }
        },
        computed: {
            isOwner(){
                return this.question.author === this.requestUser;
            }
        },

        methods: {
            setPageTitle(title){
                document.title = title;
            },
            setRequestUser(){
                this.requestUser = window.localStorage.getItem("username");
            },

            getQuestionData(){
                let endpoint = `/api/questions/${this.slug}/`;
                apiService(endpoint)
                    .then(data => {
                        console.log(data)
                        this.question = data;
                        this.userHasAnswered = data.user_has_hanswered;
                        this.setPageTitle(data.content);
                    })
            },
            getQuestionAnswer(){
            let endpoint = `/api/questions/${this.slug}/answers/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadinAnswers = true;
            apiService(endpoint)
                .then(data => {
                    this.answers.push(...data.results);
                    this.loadinAnswers = false;
                    if (data.next){
                        this.next = data.next;
                    }else {
                        this.next = null;
                    }
                })
            },
            onSubmit(){
                if (this.newAnswerBody){
                    let endpoint = `/api/questions/${this.slug}/answer/`;
                    apiService(endpoint, "POST", {body: this.newAnswerBody})
                        .then(data => {
                            this.answers.unshift(data);
                        })
                    this.newAnswerBody = null;
                    this.showForm = false,
                    this.userHasAnswered = true
                    if (this.error){
                        this.error = null;
                    }
                } else{
                    this.error = "Scrivi qualcosa"
                }
            },
            async deleteAnswer(answer){
                let endpoint = `/api/answer/${answer.id}/`;
                try {
                    await apiService(endpoint, "DELETE");
                    this.answers.splice(this.answers.indexOf(answer), 1);
                    this.userHasAnswered = false;
                }
                catch (err){
                    console.log(err)
                }
            }
        },

        created(){
            this.getQuestionData();
            this.getQuestionAnswer();
            this.setRequestUser();
        }
    }
</script>

<style>
    .answer-added{
        color: green;
        font-weight: bold;
    }
    .error{
        color: red;
        font-weight: bold;
    }
</style>