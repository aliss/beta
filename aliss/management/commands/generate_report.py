from django.core.management.base import BaseCommand, CommandError
from aliss.models import *
from django.db.models import F
from django.contrib import messages
from django.conf import settings
from django.urls import reverse

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-p', '--verbose', type=bool, help='Print more details -p 1',)

    def handle(self, *args, **options):
        self.stdout.write("\nGenerating Report\n")
        #self.stderr.write(self.style.SUCCESS('Checking service urls'))
        print(options)
        self.verbose = options['verbose']

        import_user    = ALISSUser.objects.get(email="technical@aliss.org")
        admins         = ALISSUser.objects.exclude(email="technical@aliss.org").filter(is_staff=True)
        alliance_users = ALISSUser.objects.filter(email__icontains="alliance-scotland.org.uk")
        editors        = ALISSUser.objects.filter(is_editor=True).exclude(email="technical@aliss.org").exclude(is_staff=True)
        other_users    = ALISSUser.objects.exclude(email="technical@aliss.org").difference(alliance_users, editors)

        published      = Organisation.with_services().filter(published=True)
        oscr_imported  = published.filter(created_by=import_user)
        admin_created  = published.filter(created_by__in=admins)
        staff_created  = published.filter(created_by__in=alliance_users)
        editor_created = published.filter(created_by__in=editors)
        other_created  = published.filter(created_by__in=other_users)
        claimed        = published.exclude(claimed_by=None)
        claimant_created = claimed.filter(created_by=F('claimed_by'))

        print("\nUsers:")
        print("  Total number:",    ALISSUser.objects.count())
        print("  Admin status:",    admins.count())
        print("  Editor status:",   editors.count())
        print("  [email]@alliance-scotland.org.uk:", alliance_users.count())
        print("  Other:", other_users.count())

        print("\nOrganisations:")
        print("  Total number:", Organisation.objects.count())
        print("  Total published:", published.count())
        print("\nPublished organisations")
        print("  Total claimed:", claimed.count())
        print("  Created by OSCR import:", oscr_imported.count())
        print("  Created by admins:",      admin_created.count())
        print("  Created by staff:",       staff_created.count())
        print("  Created by editor:",      editor_created.count())
        print("  Created by other:",       other_created.count())
        print("  Created by claimant:",    claimant_created.count())

        print("\nServices:")
        print("  Total number:",    Service.objects.count())
        print("  Total published:", Service.published().count())
        print("\nPublished services")
        print("  Belong to claimed org:", Service.published().filter(organisation__in=claimed).count())
        print("  Created by staff:",    Service.published().filter(created_by__in=alliance_users).count())
        print("  Created by admins:",   Service.published().filter(created_by__in=admins).count())
        print("  Created by editor:",   Service.published().filter(created_by__in=editors).count())
        print("  Created by other:",    Service.published().filter(created_by__in=other_users).count())


def graph(qs=ALISSUser.objects, field='date_joined', bins=5):
    #from aliss.models import *
    import matplotlib.pyplot as plt
    import pandas as pd

    #setup dataframe
    fig, ax = plt.subplots()
    values = qs.values(field)
    res = []
    for x in values:
        res.append(x[field])
    dataset=pd.DataFrame({ 'date':res })
    #plot by bins
    ax = dataset["date"].hist(bins=bins, color='teal', alpha=0.8, rwidth=0.999)
    ax.set(xlabel='Date', ylabel='Count')
    plt.show()