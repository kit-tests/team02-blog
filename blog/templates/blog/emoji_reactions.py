from django import template
from django.contrib.contenttypes.models import ContentType

from emoji_reactions.models import EmojiReaction
from emoji_reactions.views import (
    build_object_session_key,
    get_session_reaction_state,
)

register = template.Library()


@register.inclusion_tag("emoji_reactions/widget.html", takes_context=True)
def reaction_widget(context, obj):
    """Build widget payload, including session state to enforce one reaction per browser session."""
    request = context.get("request")
    content_type = ContentType.objects.get_for_model(obj, for_concrete_model=False)
    object_session_key = build_object_session_key(content_type.pk, obj.pk)
    selected_reaction = None

    if request:
        _reaction_map, state = get_session_reaction_state(request, object_session_key)
        selected_reaction = state.get("reaction")

    return {
        "content_type_id": content_type.pk,
        "object_id": obj.pk,
        "next_url": request.get_full_path() if request else "/",
        "buttons": EmojiReaction.button_payload_for(obj),
        "selected_reaction": selected_reaction,
    }