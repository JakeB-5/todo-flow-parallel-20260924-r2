def safe_divide(numerator, denominator, fallback=None):
    """Divide numerator by denominator, returning fallback for zero."""
    if denominator == 0:
        return fallback
    return numerator / denominator
