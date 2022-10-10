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

        return True if (len(total_op) > 1 and len(par) == 0) else False

    def check_post_inc_dec(self, statement):
        statement.replace(" ", "")

        x = re.split("=", statement)
        # print(x)

        lhs = x[0]
        rhs = x[1]

        print(statement)
        if rhs[len(rhs) - 1] == "+" and rhs[len(rhs) - 2] == "+":
            rhs = rhs.replace("++", "")
            if rhs != lhs:
                # print("atom")
                return True
            else:
                # print("not atom")
                return False
        else:
            # print("not atom")
            return False

    def check_pre_inc_dec(self, statement):
        statement.replace(" ", "")
        x = re.split("=", statement)
        # print(x)

        lhs = x[0]
        rhs = x[1]

        print(statement)
        if rhs[0] == "+" and rhs[1] == "+":
            rhs = rhs.replace("++", "")
            if rhs != lhs:
                # print("atom")
                return True
            else:
                # print("not atom")
                return False
        else:
            # print("not atom")
            return False

    def check_constant_variable(self, statement):
        statement.replace(" ", "")
        print(statement)

        x = re.split("=", statement)
        # print(x)

        lhs = x[0]
        rhs = x[1]

        y = re.search("^\".*\"$", rhs)
        # print(rhs)
        quote_exists = False
        is_number = False

        if y:
            quote_exists = True
        if rhs.isdigit():
            is_number = True

        if is_number == False and quote_exists == False:
            # print("atom")
            return True
        else:
            # print("not atom")
            return False

    def check_conditional_operator(self, statement):
        print(statement)
        # w = re.search("[a-zA-z_]+[a-zA-z0-9_]*=[a-zA-z_]+[a-zA-z0-9_]*==[0-9]*?[0-9]*:[0-9]*;", statement)
        w = re.search(".+\?.+:.+", statement)
        return True if w else False
