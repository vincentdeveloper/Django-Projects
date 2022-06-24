from django.urls import path
from api.views import(
    TodoGetCreate,
    TodoUpdateDelete
)

urlpatterns=[
  
    path('',TodoGetCreate.as_view()),
    path('<int:pk>',TodoUpdateDelete.as_view()),
]