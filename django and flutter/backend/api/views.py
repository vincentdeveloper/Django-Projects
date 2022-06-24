
from rest_framework import  generics
from api.models import Todo
from api.serializers import TodoSerializer


class TodoGetCreate(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

    # def get_queryset(self):
    #     data= self.kwargs['pk']
    #     print(data)
    #     return Todo.objects.filter(title=data)

class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer