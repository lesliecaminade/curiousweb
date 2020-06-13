from django.urls import path
from . import views

app_name = 'testimonials'

urlpatterns = [
    path('',views.Testimonial.as_view(),name='all'),
    path('create/', views.CreateTestimony.as_view(), name='create_testimony'),
    path('delete/<pk>', views.DeleteTestimony.as_view(), name='delete_testimony'),
    path('edit/<pk>', views.EditTestimony.as_view(), name='edit_testimony'),
    path('show/<pk>', views.ShowTestimony.as_view(), name='show_testimony'),

]
