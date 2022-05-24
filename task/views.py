from task.models import Task
from task.serializer import TaskSerializer,RegisterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import  login
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class Taskk(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
      
        if self.request.user.is_superuser == True:
            return super().get_queryset().all()
        else:
            return super().get_queryset().filter(user=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        idd=self.kwargs['pk']
        data=Task.objects.filter(user=self.request.user)
        data_id=[]
        for i in data:
            data_id.append(i.id)

        all_dta=Task.objects.all()
        all_data_id=[]
        for i in all_dta:
            all_data_id.append(i.id)

        if int(idd) in all_data_id:
            if idd not in data_id:
                return Response({'error': 'Unauthorized'}, status=401)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['first_name']=self.user.first_name
        data['last_name']=self.user.last_name
        data['email']=self.user.email
        data['username'] = self.user.username
        data['is_active']=self.user.is_active
        
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    