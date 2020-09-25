from .serializers import QuoteSerializer, CategorySerializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import Quote, QuoteCategory


class QuoteApi(APIView):
    def get(self, request):
        model = Quote.objects.all()
        serializer = QuoteSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetail(APIView):
    def get_quote(self, id):
        try:
            model = Quote.objects.get(id=id)
            return model
        except Quote.DoesNotExist:
            return

    def get(self, request, id):
        if not self.get_quote(id):
            return Response(f'There are no id {id} in database.', status=status.HTTP_400_BAD_REQUEST)
        model = Quote.objects.get(id=id)
        serializer = QuoteSerializer(model)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

    def put(self, request, id):
        if not self.get_quote(id):
            return Response(f'There are no id {id} in database.', status=status.HTTP_400_BAD_REQUEST)
        serializer = QuoteSerializer(self.get_quote(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = self.get_quote(id)
        model.delete()
        return Response(status=status.HTTP_410_GONE)


class CategoryApi(APIView):
    def get(self, request):
        model = QuoteCategory.objects.all()
        serializer = CategorySerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
