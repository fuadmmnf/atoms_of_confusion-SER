import re


class ConfusionAtomDetector:
    _java_variable_regex = '[a-zA-z_]+[a-zA-z0-9]*'
    def post_increment_decrement(self, code):
        return re.compile(rf'{self._java_variable_regex}\s*(?:\+\+|--)').findall(code)
