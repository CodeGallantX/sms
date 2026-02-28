from django.db.models import Avg
from .models import ExamScore, ReportCard, Term

class AcademicService:
    @staticmethod
    def calculate_gpa(student_id, term_id):
        scores = ExamScore.objects.filter(student_id=student_id, exam__term_id=term_id)
        if not scores.exists():
            return 0.0

        # Simple average for now, could be weighted
        avg_score = scores.aggregate(Avg('score'))['score__avg']
        # Convert to 4.0 scale (assuming max score is 100)
        gpa = (avg_score / 100) * 4.0
        return round(gpa, 2)

    @staticmethod
    def generate_report_cards(term_id):
        # Logic to bulk generate report cards and calculate rankings
        pass
