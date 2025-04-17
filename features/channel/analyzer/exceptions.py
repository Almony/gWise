class AnalyzerDisabled(Exception):
    """Raised when analyzer is not enabled for the channel."""
    pass

class NotAdminError(Exception):
    """Raised when the bot lacks admin privileges in the target channel."""
    pass
