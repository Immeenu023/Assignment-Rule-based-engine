from django.db import models


class AddRule(models.Model):
    ruleName = models.CharField(max_length=13, help_text="Rule Name")
    campaign = models.CharField(max_length=13, help_text="campaign Name")
    schedule = models.TimeField(max_length=13, help_text="Schedule Time")
    action = models.CharField(max_length=13, help_text="Action")
    status = models.CharField(max_length=13, help_text="Status")

    def __str__(self):
        return "{0}{1}{2}{3}{4}".format(self, self.ruleName, self.campaign, self.schedule, self.action, self.status)
