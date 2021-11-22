from django.urls import path
from .views import product_view, categories_view, feedback_view, feedbackupdate_view


urlpatterns = [
	path('', product_view),
	path('categories/', categories_view),
	path('feedback/', feedback_view),
	path('feedback/<int:pk>/', feedbackupdate_view),
]