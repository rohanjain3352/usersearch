from django.db import models


class ModelBase(models.Model):
    """
        This is a abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class User(ModelBase):
    """
    User Model
    """
    login = models.CharField(max_length=254, null=True, blank=True)
    user_id = models.FloatField()
    gravatar_id = models.CharField(max_length=254, default="", blank=True, null=True)
    avatar_url = models.CharField(max_length=254, default="", blank=True, null=True)
    url = models.CharField(max_length=254, blank=True, default="")
    html_url = models.CharField(max_length=254, default="", blank=True, null=True)
    followers_url = models.CharField(max_length=10, default="", blank=True, null=True)
    following_url = models.CharField(max_length=254, default="", blank=True, null=True)
    gists_url = models.CharField(max_length=254, default="", blank=True, null=True)
    starred_url = models.CharField(max_length=254, default="", blank=True, null=True)
    subscriptions_url = models.CharField(max_length=254, default="", blank=True, null=True)
    organizations_url = models.CharField(max_length=254, default="", blank=True, null=True)
    repos_url = models.CharField(max_length=254, default="", blank=True, null=True)
    events_url = models.CharField(max_length=254, default="", blank=True, null=True)
    received_events_url = models.CharField(max_length=254, default="", blank=True, null=True)
    type = models.CharField(max_length=254, default="", blank=True, null=True)
    score = models.FloatField()
    picture = models.CharField(max_length=508, blank=True, null=True)

    def __unicode__(self):
        return self.login

    def get_login(self):
        login = self.login
        if self.login:
            return login
        return self.login


class SearchKeys(ModelBase):
    """
    Table to store the search keys
    """
    search_key = models.CharField(max_length=254, null=True, blank=True)