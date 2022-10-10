from unittest import TestCase

from confusion_atom_detector import ConfusionAtomDetector


class TestConfusionAtomDetector(TestCase):
    cad = ConfusionAtomDetector()

    def test_post_increment_decrement(self):
        code = 'v   ++; a--: --v; _--'
        self.assertEqual(self.cad.post_increment_decrement(code), ['v   ++', 'a--', '_--'])

    def test_change_of_literal_encoding(self):
        statements = ["v1 = 013;", "v2 =045;"]
        expected = [True, True]
        for i in range(len(statements)):
            self.assertEqual(self.cad.change_of_literal_encoding(statements[i]), expected[i])

    def test_check_infix_operator_precedence(self):
        statements = ["(2/4)-(2*3)-9", "2-4/3", "2-4", "2-4/2+9"]
        expected = [False, True, False, True]
        for i in range(len(statements)):
            self.assertEqual(self.cad.check_infix_operator_precedence(statements[i]), expected[i])

    def test_check_post_inc_dec(self):
        statements = ["var1=var1++", "var1=var2++", "var1=var2", "var1+=1", "var1+=1", "something=previous++",
                      "var1=var2"]
        expected = [False, True, False, False, False, True, False]
        for i in range(len(statements)):
            self.assertEqual(self.cad.check_post_inc_dec(statements[i]), expected[i])

    def test_check_pre_inc_dec(self):
        statements = ["var1=++var1", "var1=++var2", "var1=var2", "var1+=1", "var1+=1", "something=++previous",
                      "var1=var2"]
        expected = [False, True, False, False, False, True, False]
        for i in range(len(statements)):
            self.assertEqual(self.cad.check_pre_inc_dec(statements[i]), expected[i])

    def test_check_constant_variable(self):
        statements = ['var1=var2', 'var1="saaj"', 'var1=5']
        expected = [True, False, False]
        for i in range(len(statements)):
            self.assertEqual(self.cad.check_constant_variable(statements[i]), expected[i])

    def test_check_conditional_operator(self):
        statements = ['v2=v1==3?2:1;','v1==3?2:1+v==5', 'if v1==3 {v2=2} else {v2=1}']
        expected = [True, True, False]
        for i in range(len(statements)):
            self.assertEqual(self.cad.check_conditional_operator(statements[i]), expected[i])
