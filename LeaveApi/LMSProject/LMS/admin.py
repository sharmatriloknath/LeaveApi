from django.contrib import admin
from .models import  Employee, EmpLeaveRequest, LeaveBalance, EmpMgrDept

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmpLeaveRequest)
admin.site.register(LeaveBalance)
admin.site.register(EmpMgrDept)