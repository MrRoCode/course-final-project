import { createRouter, createWebHistory } from "vue-router";
import AnswerEditor from "@/views/AnswerEditor.vue";
import HomeView from "../views/HomeView.vue";
import QuestionView from "../views/QuestionView.vue";
import QuestionEditor from "../views/QuestionEditor.vue";



const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/question/:slug",
    name: "question",
    component: QuestionView,
    props: true
  },
  {
    path: "/ask/:slug?",
    name: "question-editor",
    component: QuestionEditor,
    props: true
  },
  { 
  path: "/answer/:id/",
  name: "answer-editor",
  component: AnswerEditor,
  props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
