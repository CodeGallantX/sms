from django.urls import path
from .views import GenerateCommentView, DraftFeeReminderView

urlpatterns = [
    path('generate-comment/', GenerateCommentView.as_view(), name='generate-comment'),
    path('draft-reminder/', DraftFeeReminderView.as_view(), name='draft-reminder'),
]
