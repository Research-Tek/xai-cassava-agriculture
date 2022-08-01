import re

"""
Convert camel case names to snake case names.

https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
"""
_pattern = re.compile(r'(?<!^)(?=[A-Z])')


def camel_to_snake(name: str):
    return re.sub(_pattern, '_', name).lower()
