from django.urls import include, path
from rest_framework.routers import DefaultRouter
from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewset)

urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answers/",
          qv.QuestionAnswerListAPIView.as_view(),
          name="question-answers-list"),

    path("questions/<slug:slug>/answer/", 
        qv.AnswerCreateAPIView.as_view(), 
        name="create-answers"),

    path("answer/<int:pk>/",
         qv.AnswerRUDAPIView.as_view(),
         name="answer-detail"),

    path("answer/<int:pk>/like/",
         qv.AnswerLikeAPIView.as_view(),
         name="answer-like")
]