from django.urls import path
from GenAI.views import GenAIWebhook



urlpatterns = [
    path('genaiResponse/', GenAIWebhook.as_view()),
    path('response/', GenAIWebhook.GenAI_response)

]

