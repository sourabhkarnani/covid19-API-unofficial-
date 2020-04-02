from django.db import models

class DataMixin(models.Model):
    total_confirmed_cases = models.IntegerField(blank=True, null=True)
    total_death = models.IntegerField(blank=True, null=True)
    total_recovered = models.IntegerField(blank=True, null=True)
    critical_cases = models.IntegerField(blank=True, null=True)
    active_cases = models.IntegerField(blank=True, null=True)
    cases_today = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class CountryData(DataMixin):
    country = models.CharField(max_length=100, unique=True)
    country_flag = models.ImageField(upload_to='flags/', blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.country, self.total_confirmed_cases)

class StateData(DataMixin):
    state = models.CharField(max_length=50,unique=True)
    state_code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.state, self.total_confirmed_cases)
