from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('add/<int:n1>/<int:n2>', views.addition, name='adding'),
    path('htmlrender', views.hello_html_view, name='hello_html'),
    path('specials', views.special, name='special_redirect'),
    path('helloquery', views.another_view, name='another_view'),
    path('postexample', views.post_example, name='post_example'),
    path('submit', views.submit_example, name='submit_example'),
    path('submit_django_form', views.submit_django_form, name='submit_django_form'),
    path('templating', views.template_view, name = 'template_view'),
    path('todos', views.todos_view, name='todos_view'),
    path('person/<int:person_id>', views.person_details_view, name='person_todos_view'),
    path('delete_todo/<int:todo_id>', views.delete_todo_view, name='delete_todo_view'),
    path('toggle_todo/<int:todo_id>', views.toggle_todo_view, name='toggle_todo_view'),
]
