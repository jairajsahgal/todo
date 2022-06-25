from django.urls import path, include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.Views.register import register
from api.Views.all_todos import getTodos
from api.Views.login import login_api
from api.Views.create_note import create_note
from api.Views.create_point import create_point
from api.Views.Point_OCR import get_text_from_image
from api.Views.deleteNote import deleteNote
from api.Views.deletePoint import deletePoint

urlpatterns = [
        path('register/',register,name="register"),
        path('all_todos/',getTodos,name="all-todos"),
        path('login/',login_api,name="login-api"),
        path('create_note/',create_note,name="create-note"),
        path('create_point/',create_point,name="create-point"),
        path('point_ocr/',get_text_from_image,name="point_ocr"),
        path('delete_note/<str:title>/',deleteNote,name="delete_note"),
        path('delete_point/<str:id>/',deletePoint,name="delete_point"),
    ]