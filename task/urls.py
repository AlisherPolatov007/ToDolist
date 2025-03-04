from django.urls import path  , include
from rest_framework.routers import DefaultRouter
from .views import (TaskViewSet , TaskCreateView ,  TaskLIstView ,
                    TaskDeleteView , TaskUpdateView , TaskRetrieveView,
                    TaskCreateApiView , TaskUpdateApiView ,TaskDeletApiView , 
                    TaskListApiView , TaskRetrieveApiView , TaskListCreateView,
                    TaskRetrieveUpdateDelete)




# DRF-ysg 

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo API",
        default_version='v1',
        description="ToDo loyihasi uchun API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns =[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




# viewsets  urls

router = DefaultRouter () # Router orqali avtomatik URL yaratamiz
router.register(r'task', TaskViewSet)  # task endpoint yaratildi 

urlpatterns += [
    path('' ,include(router.urls)) ,   # Barcha API marshrutlarini kiritish
]


# generic urls

urlpatterns +=[
    path('generic/create-task/' ,TaskCreateView.as_view() , name='create_task') ,
    path('generic/update-task/<int:pk>' , TaskUpdateView.as_view() , name='update_task') , 
    path('generic/delet-task/<int:pk>', TaskDeleteView.as_view() , name='delet_task'),
    path('generic/list-task/', TaskLIstView.as_view() , name='list_task'),
    path('generic/retrieve-task/<int:pk>', TaskRetrieveView.as_view() , name='retrieve_task'),
]

#generic more urls

urlpatterns+=[
    path('crud//list-create-task/',TaskListCreateView.as_view() , name='tasks_list_create' ),
    path('crud/rud-task/<int:pk>' , TaskRetrieveUpdateDelete.as_view() , name='task_rud') ,
]

# ApiView   urls 


urlpatterns +=[
    path('api/createapi-task/' ,TaskCreateApiView.as_view() , name='createapi_task' ),
    path('api/updateapi-task/<int:pk>' ,TaskUpdateApiView.as_view() , name='updateapi_task' ),
    path('api/deleteapi-task/<int:pk>' ,TaskDeletApiView.as_view() , name='deleteapi_task' ),
    path('api/listapi-task/' ,TaskListApiView.as_view() , name='listapi_task' ),
    path('api/retrieveapi-task/<int:pk>' ,TaskRetrieveApiView.as_view() , name='retrieveapi_task' ),
]
