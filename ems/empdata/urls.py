from django.urls import path
from empdata import views
urlpatterns=[
    path('',views.home,name='home'),
    path('sheet/data',views.getSheetData,name='getSheetData'),
    path('postSheetData',views.postSheetData,name='postSheetData'),
    path('empdata/new',views.addemp,name='addemp'),
    path('empdata',views.emps,name='empdata')
]