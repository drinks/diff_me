from django.db import models
from django.db.models.signals import post_save
from diff_me.base58 import b58encode
import difflib

LANGUAGE_CHOICES = (
    ('0', 'Plain Text'),
    ('1', 'Javascript'),
    ('2', 'HTML/XML'),
    ('3', 'PHP'),
    ('4', 'Python'),
    ('5', 'Ruby'),
    ('6', 'CSS'),
    ('7', 'Perl'),
)

class Diff(models.Model):
    
    base58= models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    language = models.CharField(max_length=4, choices=LANGUAGE_CHOICES)
    original = models.TextField()
    original_revision = models.CharField(max_length=200, blank=True)
    modified = models.TextField()
    modified_revision = models.CharField(max_length=200, blank=True)
    private = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    
    differ = difflib.HtmlDiff(tabsize=4)
    
    def __unicode__(self):
        name = self.slug or self.base58
        return "%s (%s)" % (name, self.parent)
    
    def diff_table(self):
        fromlines = self.original.split(r'\n')
        tolines = self.modified.split(r'\n')
        return differ.make_table(fromlines, tolines)
    
def diff_save_handler(sender, **kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        instance.base58 = b58encode(instance.id)
        instance.save()

post_save.connect(diff_save_handler, sender=Diff)