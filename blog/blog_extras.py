from django.utils.text import slugify

from .models import Post


def _build_unique_post_slug(title, current_post=None):
    """Create a unique slug for a post title, preserving the current post when editing."""
    base_slug = slugify(title) or "post"
    candidate = base_slug
    suffix = 2

    while Post.objects.exclude(pk=getattr(current_post, "pk", None)).filter(slug=candidate).exists():
        candidate = f"{base_slug}-{suffix}"
        suffix += 1

    return candidate


def save_post_from_form(form, *, original_title=None, original_slug=None):
    """Persist a post from a validated form and handle slug generation consistently."""
    post = form.save(commit=False)

    if not post.slug:
        post.slug = _build_unique_post_slug(post.title)
    else:
        title_changed = original_title is not None and post.title != original_title
        slug_was_auto_generated = original_title is not None and original_slug == slugify(original_title)
        if title_changed and slug_was_auto_generated:
            post.slug = _build_unique_post_slug(post.title, current_post=post)

    post.save()
    return post
