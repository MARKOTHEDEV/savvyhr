from django.urls import path
from . import views




urlpatterns = [        
    path("",views.indexPage),
    path('service-detail/<int:pk>/',views.serviceDetail,name='serviceDetail'),

    path("research-insight/",views.researchInsight,name='researchInsight'),
    path("solutions/",views.solutionsPage,name='our-solutions'),
    path("contact-us/",views.contactUs,name='contact-us'),
]