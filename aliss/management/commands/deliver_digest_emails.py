
from django.core.management.base import BaseCommand, CommandError
from aliss.models import *

from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from datetime import datetime
from datetime import timedelta
import pytz

class Command(BaseCommand):
    def handle(self, *args, **options):

        def process_datetime_string(datetime_string):
            utc = pytz.UTC
            datetime_string = datetime_string.split('+')
            datetime_string = datetime_string[0]
            d = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S.%f')
            utc.localize(d)
            d = datetime.strftime(d, '%d %b %Y, %I:%M %p')
            return d

        def send_digest_email(user):
            #Need to setup the comparison date:
            utc = pytz.UTC
            current_date = datetime.now()
            current_date = utc.localize(current_date)
            number_of_weeks = 4
            comparison_date = current_date - timedelta(weeks=number_of_weeks)


            # Focus on the situation where Digest Selections have been created and have updated services.
            message = "\n\n-----\n\n\nYour Weekly Digest Selection\n\n"

            for digest_object in user.digest_selections.all():
                message += "\n\n-----\n\nDigest for {digest_postcode} and {digest_category} updated services:".format(
                    digest_postcode=digest_object.postcode,
                    digest_category=digest_object.category,)
                r = digest_object.retrieve(comparison_date)[:3]
                if not r:
                    message += '\n\n No updated services for this Digest Selection'
                else:
                    for service in r:
                        message += '\n\n {service_name} \n\n {service_updated_on}'.format(
                            service_name=service.name,
                            service_updated_on=process_datetime_string(service.updated_on),
                            )
        #Send the email to the user.
            send_mail(
                'Subject: Test Test Test',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=True,
                )

        users = ALISSUser.objects.all()
        for user in users:
            if DigestSelection.objects.filter(user=user):
                send_digest_email(user)

        self.stdout.write(
            self.style.SUCCESS('Successfully sent Digest Emails')
        )
