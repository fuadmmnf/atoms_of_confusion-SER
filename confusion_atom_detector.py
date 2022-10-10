import re


class ConfusionAtomDetector:
    totalAtomCount = 0
    _java_variable_regex = '[a-zA-z_]+[a-zA-z0-9]*'
    def post_increment_decrement(self, code):
        return re.compile(rf'{self._java_variable_regex}\s*(?:\+\+|--)').findall(code)

    def change_of_literal_encoding(self, statement):
        statement.replace(' ', '')
        x = re.split("=", statement)
        lhs = x[0]
        rhs = x[1]
        rhs = rhs.strip()
        w = re.search("^0.*", rhs)
        return True if w else False

