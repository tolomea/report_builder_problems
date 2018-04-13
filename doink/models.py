from django.db import models


class Neither(models.Model):
    text = models.TextField()

    text_n = models.TextField()
    neither_n = models.ForeignKey('Neither', related_name='+')
    both_n = models.ForeignKey('Both', related_name='+')
    inner_class_n = models.ForeignKey('InnerClass', related_name='+')
    settings_n = models.ForeignKey('Settings', related_name='+')


class Both(models.Model):
    class ReportBuilder:
        fields = ('text', 'text_b', 'neither', 'both', 'inner_class', 'settings')

    text = models.TextField()

    text_b = models.TextField()
    neither_b = models.ForeignKey('Neither', related_name='+')
    both_b = models.ForeignKey('Both', related_name='+')
    inner_class_b = models.ForeignKey('InnerClass', related_name='+')
    settings_b = models.ForeignKey('Settings', related_name='+')

    text_b_x = models.TextField()
    neither_b_x = models.ForeignKey('Neither', related_name='+')
    both_b_x = models.ForeignKey('Both', related_name='+')
    inner_class_b_x = models.ForeignKey('InnerClass', related_name='+')
    settings_b_x = models.ForeignKey('Settings', related_name='+')


class InnerClass(models.Model):
    class ReportBuilder:
        fields = ('text', 'text_i', 'neither', 'both', 'inner_class', 'settings')

    text = models.TextField()

    text_i = models.TextField()
    neither_i = models.ForeignKey('Neither', related_name='+')
    both_i = models.ForeignKey('Both', related_name='+')
    inner_class_i = models.ForeignKey('InnerClass', related_name='+')
    settings_i = models.ForeignKey('Settings', related_name='+')

    text_i_x = models.TextField()
    neither_i_x = models.ForeignKey('Neither', related_name='+')
    both_i_x = models.ForeignKey('Both', related_name='+')
    inner_class_i_x = models.ForeignKey('InnerClass', related_name='+')
    settings_i_x = models.ForeignKey('Settings', related_name='+')


class Settings(models.Model):
    text = models.TextField()

    text_s = models.TextField()
    neither_s = models.ForeignKey('Neither', related_name='+')
    both_s = models.ForeignKey('Both', related_name='+')
    inner_class_s = models.ForeignKey('InnerClass', related_name='+')
    settings_s = models.ForeignKey('Settings', related_name='+')
