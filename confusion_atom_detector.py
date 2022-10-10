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

    def check_infix_operator_precedence(self, statement):
        plus = re.findall("[+]", statement)
        minus = re.findall("[-]", statement)
        mul = re.findall("[*]", statement)
        div = re.findall("[/]", statement)

        # exp = re.findall("["**.*"]", txt)
        # print(len(exp))

        total_op = plus + minus + mul + div
        par = re.findall("[(]", statement)

        if (len(total_op) > 1 and len(par) == 0):
            return True
        else:
            return False

