from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from records.models import FinancialRecord
from django.db.models import Sum


class DashboardSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        # 🔥 Step 1: Role-based filtering
        if user.role == 'viewer':
            records = FinancialRecord.objects.filter(user=user)
        else:
            records = FinancialRecord.objects.all()

        # 🔥 Step 2: Aggregations
        total_income = records.filter(type='income').aggregate(
            total=Sum('amount')
        )['total'] or 0

        total_expense = records.filter(type='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0

        net_balance = total_income - total_expense

        # 🔥 Step 3: Category-wise totals
        category_data = (
            records.values('category')
            .annotate(total=Sum('amount'))
        )

        category_breakdown = {
            item['category']: item['total']
            for item in category_data
        }

        # 🔥 Step 4: Recent activity (last 5)
        recent = records.order_by('-created_at')[:5]

        recent_data = [
            {
                "id": r.id,
                "amount": r.amount,
                "type": r.type,
                "category": r.category,
                "date": r.date
            }
            for r in recent
        ]

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance,
            "category_breakdown": category_breakdown,
            "recent_transactions": recent_data
        })