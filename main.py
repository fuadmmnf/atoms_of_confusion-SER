from confusion_atom_detector import ConfusionAtomDetector

if __name__ == '__main__':
    #pass
    filepath = 'code_with_atoms_1.py'
    obj_cad = ConfusionAtomDetector(filepath)

    line_list = obj_cad.read_file_and_write_csv(filepath)

    atom_dict = {}
    obj_cad.count_atoms(line_list, atom_dict)
    print("\n")
    print(atom_dict)
    print("\n")