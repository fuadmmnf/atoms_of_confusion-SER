import re


class ConfusionAtomDetector:
    totalAtomCount = 0
    _java_variable_regex = '[a-zA-z_]+[a-zA-z0-9]*'

    #def post_increment_decrement(self, code):
    #    return re.compile(rf'{self._java_variable_regex}\s*(?:\+\+|--)').findall(code)

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

    def check_arithmetic_as_logic(self, statement):
        w = re.search(".+\*.+!=.+", statement)
        return True if w else False

    def check_logic_as_control_flow(self, statement):
        arithmetic_operators = "(\+\+|--|\+=|-=|\*=|/=|%=)"
        w = re.search(f".*{arithmetic_operators}.*(\|\||&&).*{arithmetic_operators}.*", "v1=++v1>0||++v2>0;")
        # print(w)
        print(statement)
        return True if w else False

    def check_repurposed_variable(self, statement, next_statement):
        w = re.search("^for.*", statement)
        # print(w)
        if (w):
            next_w = re.search("^for.*", next_statement)
            # print(next_w)
            if (next_w):
                x = re.split(";", statement)
                # print(x)
                term1 = x[0]
                term3 = x[2]

                i = re.split(" ", term1)
                # print(i[2])
                j = re.split("=", i[2])
                # print(j[0])

                # check if j[0] matches with nextStatements 3rd term
                next_x = re.split(";", next_statement)
                next_term3 = next_x[2]
                # print(next_term3)

                res = ''
                for i in range(len(next_term3) - 3):
                    res += next_term3[i]

                print(statement)
                print(next_statement)
                return True if res == j[0] else False

    def check_dead_repeated(self, statement, next_statement):
        statement.replace(" ", "")
        x = re.split("=", statement)

        lhs = x[0]
        rhs = x[1]

        next_statement.replace(" ", "")
        y = re.split("=", next_statement)

        next_lhs = y[0]
        next_rhs = y[1]

        print(statement)
        print(next_statement)
        return True if lhs == next_lhs else False

    def check_omitted_curly_braces(self, statement):
        w = re.search("^if.*", statement)
        print(statement)
        return True if w and ('{' not in statement) else False

    def check_type_conversion(self, statement):
        print(statement)
        if ('(int)' or '(double)' or '(float)' or ('str')) in statement:
            return False if ("Math.ceil" in statement) or ("Math.floor" in statement) else True
