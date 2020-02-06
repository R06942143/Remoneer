from django.utils.timezone import now
from rest_framework import serializers
from job_api.models import job


class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        # fields = '__all__'
        fields = ('id', 'title', 'keywords', 'job_description', 'hr_email','salary','last_modify_date','created')
    def get_days_since_created(self, obj):
       return (now() - obj.created).days