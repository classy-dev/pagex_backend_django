from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CodeGenerationSerializer


class CodeGenerationAPI(APIView):
    serializer_class = CodeGenerationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(True)
        serializer.create_code()
        return Response({'detail': 'code created'})
