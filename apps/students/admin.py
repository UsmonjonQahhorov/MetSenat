from django.contrib import admin

from apps.students.models import Student,StudentSponsor
from apps.sponsors.models import Sponsor


admin.site.register(Student)
admin.site.register(Sponsor)
admin.site.register(StudentSponsor)
