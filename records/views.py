from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer


class RecordListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        #  Role-based filtering
        if user.role == 'viewer':
            records = FinancialRecord.objects.filter(user=user)

        elif user.role == 'analyst':
            records = FinancialRecord.objects.all()

        elif user.role == 'admin':
            records = FinancialRecord.objects.all()

        serializer = FinancialRecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        #  Only viewer + admin can create
        if user.role not in ['viewer', 'admin']:
            return Response(
                {"error": "You are not allowed to create records"},
                status=403
            )

        serializer = FinancialRecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    



class RecordDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(FinancialRecord, pk=pk)

    def get(self, request, pk):
        record = self.get_object(pk)

        #  Viewer can only see own
        if request.user.role == 'viewer' and record.user != request.user:
            return Response({"error": "Forbidden"}, status=403)

        serializer = FinancialRecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk):
        record = self.get_object(pk)

        # Only admin can update
        if request.user.role != 'admin':
            return Response({"error": "Only admin can update"}, status=403)

        serializer = FinancialRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        record = self.get_object(pk)

        #  Only admin can delete
        if request.user.role != 'admin':
            return Response({"error": "Only admin can delete"}, status=403)

        record.delete()
        return Response(status=204)