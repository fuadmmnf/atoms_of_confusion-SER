from confusion_atom_detector import ConfusionAtomDetector

if __name__ == '__main__':
    #pass
    filepath = 'code_with_atoms_1.py'
    obj_cad = ConfusionAtomDetector(filepath)
    obj_cad.read_file_and_write_csv(filepath)