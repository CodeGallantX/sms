from rest_framework.views import APIView
from rest_framework.response import Response
from .services import AIService

class GenerateCommentView(APIView):
    def post(self, request):
        student_name = request.data.get('student_name')
        scores = request.data.get('scores')
        ai_service = AIService()
        comment = ai_service.generate_report_comment(student_name, scores)
        return Response({'comment': comment})

class DraftFeeReminderView(APIView):
    def post(self, request):
        parent_name = request.data.get('parent_name')
        amount = request.data.get('amount')
        ai_service = AIService()
        draft = ai_service.auto_draft_fee_reminder(parent_name, amount)
        return Response({'draft': draft})
