
from MovieAPP import serializer
from MovieAPP.serializer import MovieSerializer
from MovieAPP.models import Movie

from rest_framework import mixins,generics,viewsets

# Create your views here.

# Mixins

#APIView for listing and creating movie records
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
# #APIView for read/update/delete existing movie record
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def patch(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

# generics

# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer



# Viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer





