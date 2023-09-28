from celery import shared_task
from apps.sponsors.models import Sponsor
from apps.students.models import StudentSponsor


@shared_task
def send_students_info():
    sponsors = Sponsor.objects.all()
    for sponsor in sponsors:
        print(f"Sponsor: {sponsor.full_name}")
        print(StudentSponsor.objects.filter(sponsor=sponsor).values("student"))
