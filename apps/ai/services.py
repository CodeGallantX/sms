import openai
from django.conf import settings

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def generate_report_comment(self, student_name, subjects_scores):
        prompt = f"Write a brief academic report comment for {student_name} who has the following results: {subjects_scores}."
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating comment: {str(e)}"

    def predict_at_risk_students(self, student_data):
        # AI logic to identify low performance trends
        pass

    def auto_draft_fee_reminder(self, parent_name, amount_due):
        prompt = f"Draft a polite but firm email to {parent_name} regarding an overdue fee of {amount_due}."
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error drafting email: {str(e)}"
