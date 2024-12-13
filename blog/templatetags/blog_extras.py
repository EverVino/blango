from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()

user_model = get_user_model()

@register.filter
def author_details(author):
  if not isinstance(author, user_model=None):
    return ""
  
  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.last_name and author.first_name:
    name = f"{author.last_name} {author.first_name}"
  
  else:
    name = post.author.username
  
  if author.email:
    prefix = format_html("<a href='mailto:{}'>", author.email)
    suffix = format_html("</a>")
  else:
    prefix = ""
    suffix = ""
  
  return format_html("{}{}{}", prefix, name, suffix)
      
    