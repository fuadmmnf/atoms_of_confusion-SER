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
