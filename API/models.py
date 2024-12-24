from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES=sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES= sorted([(item, item) for item in get_all_styles()])

class user(User):
    name=models.CharField(max_length=200)
    age = models.IntegerField()
    created_at= models.DateTimeField(default=datetime.now(), db_default=datetime.now(), blank=True)

class Snippet(models.Model):
    title=models.CharField(max_length=255)
    code=models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), db_default=datetime.now(), blank=True)
    lineos= models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style=models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=255)
    owner = models.ForeignKey(user, related_name='snippet', on_delete=models.CASCADE)
    highlighted= models.TextField(db_default="Hello")

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        lineos = 'table' if self.lineos else False
        options = {'title' : self.title} if self.title else{}
        formatter= HtmlFormatter(style=self.style, lineos=lineos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)

        super().save(*args, **kwargs)
