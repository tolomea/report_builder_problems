from django.db import models


class Neither(models.Model):
    text = models.TextField()
    neither = models.ForeignKey('Neither', related_name='+')
    both = models.ForeignKey('Both', related_name='+')
    inner_class = models.ForeignKey('InnerClass', related_name='+')
    settings = models.ForeignKey('Settings', related_name='+')


class Both(models.Model):
    class ReportBuilder:
        fields = ('text', 'neither', 'both', 'inner_class', 'settings')

    text = models.TextField()
    neither = models.ForeignKey('Neither', related_name='+')
    both = models.ForeignKey('Both', related_name='+')
    inner_class = models.ForeignKey('InnerClass', related_name='+')
    settings = models.ForeignKey('Settings', related_name='+')

    text_x = models.TextField()
    neither_x = models.ForeignKey('Neither', related_name='+')
    both_x = models.ForeignKey('Both', related_name='+')
    inner_class_x = models.ForeignKey('InnerClass', related_name='+')
    settings_x = models.ForeignKey('Settings', related_name='+')


class InnerClass(models.Model):
    class ReportBuilder:
        fields = ('text', 'neither', 'both', 'inner_class', 'settings')

    text = models.TextField()
    neither = models.ForeignKey('Neither', related_name='+')
    both = models.ForeignKey('Both', related_name='+')
    inner_class = models.ForeignKey('InnerClass', related_name='+')
    settings = models.ForeignKey('Settings', related_name='+')

    text_x = models.TextField()
    neither_x = models.ForeignKey('Neither', related_name='+')
    both_x = models.ForeignKey('Both', related_name='+')
    inner_class_x = models.ForeignKey('InnerClass', related_name='+')
    settings_x = models.ForeignKey('Settings', related_name='+')


class Settings(models.Model):
    text = models.TextField()
    neither = models.ForeignKey('Neither', related_name='+')
    both = models.ForeignKey('Both', related_name='+')
    inner_class = models.ForeignKey('InnerClass', related_name='+')
    settings = models.ForeignKey('Settings', related_name='+')
