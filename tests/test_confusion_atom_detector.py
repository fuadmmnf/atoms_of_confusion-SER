from unittest import TestCase

from confusion_atom_detector import ConfusionAtomDetector


class TestConfusionAtomDetector(TestCase):
    cad = ConfusionAtomDetector()

    def test_post_increment_decrement(self):
        code = 'v   ++; a--: --v; _--'
        self.assertEqual(self.cad.post_increment_decrement(code), ['v   ++', 'a--', '_--'])

