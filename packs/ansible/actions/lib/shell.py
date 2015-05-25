import functools

__all__ = [
    'replace_args',
]


def replace_args(attribute=None):
    """
    Decorator to Apply replacements in a list of command line arguments.

    :param attribute: Class attribute name which stores replacement rules.
    :type attribute: ``str``
    :return:
    :rtype: ``callable``
    """
    def _replace_args(f):
        @functools.wraps(f)
        def _wrapper(self, *args):
            rules = getattr(self, attribute)
            if not rules:
                return f(self, *args)
            return map(lambda a: rules[a] if a in rules else a, f(self, *args))
        return _wrapper
    return _replace_args
