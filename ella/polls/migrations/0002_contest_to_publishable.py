
from south.db import db
from django.db import models
from ella.polls.models import *

from ella.core.migrations_base import BasePublishableDataMigration, alter_foreignkey_to_int

class Migration(BasePublishableDataMigration):

    app_label = 'polls'
    model = 'contest'
    table = '%s_%s' % (app_label, model)

    publishable_uncommon_cols = {}
    
    def alter_self_foreignkeys(self, orm):
        alter_foreignkey_to_int('polls_question', 'contest')
        alter_foreignkey_to_int('polls_contestant', 'contest')

    def move_self_foreignkeys(self, orm):
        pass
        # TODO: migrate new contest IDs to question
        # TODO: migrate new contest IDs to contestant
