"""Custom template filters for the blog app.

Load in templates with: {% load blog_extras %}
"""

import math

from django import template

register = template.Library()


@register.filter
def reading_time(text):
    """Return a human-readable reading-time estimate for post content."""
    if not text or not text.strip():
        return "Less than a minute read"

    word_count = len(text.split())
    if word_count == 0:
        return "Less than a minute read"

    minutes = math.ceil(word_count / 200)
    if minutes == 1:
        return "1 minute read"
    return f"{minutes} minute read"
