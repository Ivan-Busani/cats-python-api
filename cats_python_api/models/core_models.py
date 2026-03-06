from django.db import models

class Cat(models.Model):
    cat_id      = models.CharField(max_length=200, unique=True, null=False, blank=False)
    url         = models.CharField(max_length=200, null=False, blank=False)
    width       = models.IntegerField()
    height      = models.IntegerField()
    breeds      = models.JSONField(default=list)
    api_used    = models.CharField(max_length=200, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'cats'

    def __str__(self):
        return self.cat_id or str(self.id)