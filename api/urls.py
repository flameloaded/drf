from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee'),

urlpatterns = [
    path('students/', views.studentView),
    path('student/<int:pk>/',views.StudentDetailView),
    # path('employee/', views.Employees.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls)),
    path('blogs', views.BlogViews.as_view()),
    path('comments', views.CommentViews.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
     path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]