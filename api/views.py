from base.models import ApiData
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import ApiDataSerializer

'''
This block for JWT Authorization
'''


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refersh',
#     ]

#     return Response(routes)


'''
This block for Information
'''


class InformationView(APIView):
    def get(self, request, *args, **kwargs):
        qs = ApiData.objects.all()
        serializer = ApiDataSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ApiDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class fileView(APIView):
    def get(self, request, pk,  *args, **kwargs):
        qs = ApiData.objects.get(id=pk)
        serializer = ApiDataSerializer(qs, many=False)
        return Response(serializer.data)
