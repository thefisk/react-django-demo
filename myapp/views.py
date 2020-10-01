from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets


# make sure this view is only accessible on login
@method_decorator(login_required, name='dispatch')
class oldEmployeeView(TemplateView):
    # our hybrid template, shown above
    template_name = 'myapp/employee_home.html'

    def get_context_data(self, **kwargs):
        # passing the department choices to the template in the context
        return {
            'department_choices': [{
                'id': c[0],
                'name': c[1]
            } for c in Employee.DEPARTMENT_CHOICES],
        }

class EmployeeDataAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # filter queryset based on logged in user
        return self.request.user.employees.all()