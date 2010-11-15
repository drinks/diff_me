from django.db import models
from django.db.models.signals import post_save
from django.forms import ModelForm
from diff_me.base58 import b58encode
import difflib
from pygments.lexers import get_all_lexers

def __get_languages():
    langs = []
    for lex in get_all_lexers():
        langs.append((lex[1][0], lex[0]))
    return langs

LANGUAGE_CHOICES = sorted(__get_languages(), key=lambda lang: lang[1])

class Diff(models.Model):
    
    base58= models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    language = models.CharField(max_length=4, choices=LANGUAGE_CHOICES, default='text')
    original = models.TextField()
    original_revision = models.CharField(max_length=200, default='original')
    modified = models.TextField()
    modified_revision = models.CharField(max_length=200, default='modified')
    private = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    
    differ = difflib.HtmlDiff(tabsize=4)
    
    def __unicode__(self):
        name = self.slug or self.base58
        if self.parent is not None:
            return "%s (%s)" % (name, self.parent)
        else:
            return name
    
    def fromlines(self):
        return self.original.splitlines()
    
    def tolines(self):
        return self.modified.splitlines()
    
    def diff_table(self):
        table = self.differ.make_table(self.fromlines(), self.tolines())
        # woo string hacking!!
        return table.replace('rules="groups"', '').replace('nowrap="nowrap"', 'class="diff_text"').replace('&nbsp;', ' ')
    
    def diff_unified_str(self):
        return '\n'.join(self.__diff_unified())
    
    def diff_unified_html(self):
        return '<br/>'.join(self.__diff_unified())
    
    def __diff_unified(self):
        fromfile = self.original_revision or 'original'
        tofile = self.modified_revision or 'modified'
        lines = []
        for line in difflib.unified_diff(self.fromlines(), self.tolines(), fromfile=fromfile, tofile=tofile, lineterm=''):
            lines.append(line)
        return lines
    
class DiffForm(ModelForm):
    class Meta:
        model = Diff
        fields = ('original', 'modified', 'private', 'original_revision', 'modified_revision')
    
def diff_save_handler(sender, **kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        instance.base58 = b58encode(instance.id)
        instance.save()

post_save.connect(diff_save_handler, sender=Diff)