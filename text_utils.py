def compact(text):
    """Collapse whitespace runs to ASCII spaces and trim surrounding whitespace."""
    return ' '.join(text.split())
