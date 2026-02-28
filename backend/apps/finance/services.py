from .models import Invoice, FeeStructure
from apps.students.models import StudentProfile

class FinanceService:
    @staticmethod
    def generate_term_invoices(fee_structure_id):
        fee_structure = FeeStructure.objects.get(id=fee_structure_id)
        students = StudentProfile.objects.filter(is_active=True)

        invoices = []
        for student in students:
            invoice = Invoice(
                student=student,
                fee_structure=fee_structure,
                due_date=fee_structure.due_date,
                amount_due=fee_structure.amount,
                status='PENDING'
            )
            invoices.append(invoice)

        Invoice.objects.bulk_create(invoices)
        return len(invoices)
