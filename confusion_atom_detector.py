import re


class ConfusionAtomDetector:
    totalAtomCount = 0
    _java_variable_regex = '[a-zA-z_]+[a-zA-z0-9]*'

    def __init__(self, file):
        self.file = file

    #def post_increment_decrement(self, code):
    #    return re.compile(rf'{self._java_variable_regex}\s*(?:\+\+|--)').findall(code)

    def check_change_of_literal_encoding(self, statement):
        statement.replace(' ', '')
        if ("while" not in statement) and ("for" not in statement) and ("if" not in statement):
            if "=" in statement:
                x = re.split("=", statement)
                lhs = x[0]
                rhs = x[1]
                rhs = rhs.strip()
                w = re.search("^0.*", rhs)
                return True if (w and len(rhs)>1) else False

    def check_infix_operator_precedence(self, statement):
        plus = re.findall("[+]", statement)
        minus = re.findall("[-]", statement)
        mul = re.findall("[*]", statement)
        div = re.findall("[/]", statement)

        # exp = re.findall("["**.*"]", txt)
        # print(len(exp))

        total_op = plus + minus + mul + div
        par = re.findall("[(]", statement)

        return True if (len(total_op) > 1 and len(par) == 0 and "++" not in statement and "--" not in statement) else False

    def check_post_inc_dec(self, statement):
        statement.replace(" ", "")

        if "=" in statement and "==" not in statement:
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
        #statement.replace(" ", "")
        #statement = (re.sub(r"\s+", "", statement), sep = '')

        #statement = statement.rstrip("w.")
        if "=" in statement and "==" not in statement:
            x = re.split("=", statement)
            # print(x)

            lhs = x[0]
            rhs = x[1]

            lhs = lhs.strip()
            rhs = rhs.strip()

            if rhs[0] == "+" and rhs[1] == "+":
                rhs = rhs.replace("++", "")
                if rhs != lhs:
                    #print(rhs + lhs)
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

        if "=" in statement:
            if ('+' not in statement) and ('-' not in statement) and ('*' not in statement) and ('/' not in statement) and ('(' not in statement) and ('[' not in statement) and ('pow' not in statement) and ('?' not in statement) and ('!' not in statement) and (':' not in statement) and ('<' not in statement) and ('>' not in statement) and ('&' not in statement) and ('|' not in statement) and ('%' not in statement) and ('{' not in statement):
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
                
                rhs = rhs.strip()
                if rhs.isdigit():
                    is_number = True

                if is_number == False:
                    if quote_exists:
                        return False
                    #w = re.search("[a-zA-z_]+[a-zA-z0-9]*", statement)
                    # print("atom")
                    #return True if w else False
                    if quote_exists == False:
                        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        #print(statement)
                        return True
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
        w = re.search(f".*{arithmetic_operators}.*(\|\||&&).*{arithmetic_operators}.*", statement)
        # print(w)
        print(statement)
        return True if w else False

    def check_repurposed_variable(self, statement, next_statement):
        w = re.search("^for.*", statement)
        print(next_statement)
        next_statement = next_statement.strip()
        print(next_statement)

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

        if "=" in statement:
            x = re.split("=", statement)

            lhs = x[0]
            rhs = x[1]

            next_statement.replace(" ", "")

            if "=" in next_statement:
                y = re.split("=", next_statement)

                next_lhs = y[0]
                next_rhs = y[1]

                #print(statement)
                #print(next_statement)
                #return True if (lhs == next_lhs and '+' not in next_rhs and '-' not in next_rhs) else False
                return True if lhs == next_lhs else False

    def check_omitted_curly_braces(self, statement):
        w = re.search("^if.*", statement)
        #print(statement)
        return True if w and ('{' not in statement) else False

    def check_type_conversion(self, statement):
        #print(statement)
        if ('(int)' or '(double)' or '(float)' or ('str')) in statement:
            return False if ("Math.ceil" in statement) or ("Math.floor" in statement) else True

    def read_file_and_write_csv(self, file):
        # Python code to
        # demonstrate readlines()

        # Using readlines()
        file1 = open(file, 'r')
        Lines = file1.readlines()

        count = 0
        line_list = []
        # Strips the newline character
        for line in Lines:
            count += 1
            line = line.strip()
            #print("Line{}: {}".format(count, line))
            if len(line)!=0:
            #print(line[0])
                if (line[0]!='#'):
                    line_list.append(line)

        return line_list

    def count_atoms(self, line_list):

        atom_dict = {}
        tracker_dict = {}
        # type_conversion
        atom_type_conversion_count = 0
        atom_post_inc_dec_count = 0
        atom_pre_inc_dec_count = 0
        atom_constant_variable_count = 0
        atom_conditional_operator_count = 0
        atom_arithmetic_as_logic_count = 0
        atom_logic_as_control_flow_count = 0
        atom_repurposed_variable_count = 0
        atom_dead_repeated_count = 0
        atom_omitted_curly_braces_count = 0
        atom_change_of_literal_encoding_count = 0
        atom_infix_operator_precedence_count = 0

        check_type_conversion = []
        check_post_inc_dec = []
        check_pre_inc_dec = []
        check_constant_variable = []
        check_conditional_operator = []
        check_arithmetic_as_logic = []
        check_logic_as_control_flow = []
        check_omitted_curly_braces = []
        check_change_of_literal_encoding = []
        check_infix_operator_precedence = []


        for line in line_list:
            if self.check_type_conversion(line):
                atom_type_conversion_count += 1
                print(atom_type_conversion_count)
                print("Atom")
                check_type_conversion.append(line)
            else:
                print("Not atom")

            if self.check_post_inc_dec(line):
                print(line)
                atom_post_inc_dec_count += 1
                print(atom_post_inc_dec_count)
                print("Atom")
                check_post_inc_dec.append(line)
            else:
                print("Not atom")

            if self.check_pre_inc_dec(line):
                atom_pre_inc_dec_count += 1
                print(atom_pre_inc_dec_count)
                print("Atom")
                check_pre_inc_dec.append(line)
            else:
                print("Not atom")

            if self.check_constant_variable(line):
                atom_constant_variable_count += 1
                print(atom_constant_variable_count)
                print("Atom")
                check_constant_variable.append(line)
            else:
                print("Not atom")

            if self.check_conditional_operator(line):
                atom_conditional_operator_count += 1
                print(atom_conditional_operator_count)
                print("Atom")
                check_conditional_operator.append(line)
            else:
                print("Not atom")

            if self.check_arithmetic_as_logic(line):
                atom_arithmetic_as_logic_count += 1
                print(atom_arithmetic_as_logic_count)
                print("Atom")
                check_arithmetic_as_logic.append(line)
            else:
                print("Not atom")

            if self.check_logic_as_control_flow(line):
                atom_logic_as_control_flow_count += 1
                print(atom_logic_as_control_flow_count)
                print("Atom")
                check_logic_as_control_flow.append(line)
            else:
                print("Not atom")

            if self.check_omitted_curly_braces(line):
                atom_omitted_curly_braces_count += 1
                print(atom_omitted_curly_braces_count)
                print("Atom")
                check_omitted_curly_braces.append(line)
            else:
                print("Not atom")

            if self.check_change_of_literal_encoding(line):
                atom_change_of_literal_encoding_count += 1
                print(atom_change_of_literal_encoding_count)
                print("Atom")
                check_change_of_literal_encoding.append(line)
            else:
                print("Not atom")

            if self.check_infix_operator_precedence(line):
                atom_infix_operator_precedence_count += 1
                print(atom_infix_operator_precedence_count)
                print("Atom")
                check_infix_operator_precedence.append(line)
            else:
                print("Not atom")

        check_repurposed_variable = []
        check_dead_repeated = []

        for i in range (len(line_list)-1):
            if self.check_repurposed_variable(line_list[i], line_list[i+1]):
                atom_repurposed_variable_count += 1
                print(atom_repurposed_variable_count)
                print("Atom")
                check_repurposed_variable.append(line)
            else:
                print("Not atom")

            if self.check_dead_repeated(line_list[i], line_list[i+1]):
                atom_dead_repeated_count += 1
                print(atom_dead_repeated_count)
                print("Atom")
                cs = line_list[i] + ', ' + line_list[i+1]
                check_dead_repeated.append(cs)
            else:
                print("Not atom")


        #print("Total type conversion atoms:")
        #print(atom_type_conversion_count)

        #dead_repeated and repurposed need two consecutive statements
        atom_dict["type_conversion"] = atom_type_conversion_count
        atom_dict["post_inc_dec"] = atom_post_inc_dec_count
        atom_dict["pre_inc_dec"] = atom_pre_inc_dec_count
        atom_dict["constant_variable"] = atom_constant_variable_count
        atom_dict["conditional_operator"] = atom_conditional_operator_count
        atom_dict["arithmetic_as_logic"] = atom_arithmetic_as_logic_count
        atom_dict["logic_as_control_flow"] = atom_logic_as_control_flow_count
        atom_dict["repurposed_variable"] = atom_repurposed_variable_count
        atom_dict["dead_repeated"] = atom_dead_repeated_count
        atom_dict["omitted_curly_braces"] = atom_omitted_curly_braces_count
        atom_dict["change_of_literal_encoding"] = atom_change_of_literal_encoding_count
        atom_dict["infix_operator_precedence"] = atom_infix_operator_precedence_count

        tracker_dict["type_conversion"] = check_type_conversion
        tracker_dict["post_inc_dec"] = check_post_inc_dec
        tracker_dict["pre_inc_dec"] = check_pre_inc_dec
        tracker_dict["constant_variable"] = check_constant_variable
        tracker_dict["conditional_operator"] = check_conditional_operator
        tracker_dict["arithmetic_as_logic"] = check_arithmetic_as_logic
        tracker_dict["logic_as_control_flow"] = check_logic_as_control_flow
        tracker_dict["repurposed_variable"] = check_repurposed_variable
        tracker_dict["dead_repeated"] = check_dead_repeated
        tracker_dict["omitted_curly_braces"] = check_omitted_curly_braces
        tracker_dict["change_of_literal_encoding"] = check_change_of_literal_encoding
        tracker_dict["infix_operator_precedence"] = check_infix_operator_precedence

        print("\n")
        print(atom_dict)
        print('\n')
        
        for key in tracker_dict:
            print("atom type: ", key)
            dash_len = len("atom type: ") + len(key)
            dash_string = ""
            for dl in range(0, dash_len+2):
                dash_string = dash_string + '-'
            print(dash_string)
            vc = 0
            for value in tracker_dict[key]:
                vc = vc + 1
                if key!='dead_repeated' or key!='repurposed_variable':
                    print("Statement {}: {}".format(vc, value))
                else:
                    print("Statement pair {}: {}".format(vc, value))

            print('\n')
        print("\n")

        return "end"