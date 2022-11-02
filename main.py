from confusion_atom_detector import ConfusionAtomDetector

if __name__ == '__main__':
    #pass
    filepath = 'tests/res/PropositionalLogicResolution.java'
    obj_cad = ConfusionAtomDetector(filepath)

    line_list = obj_cad.read_file_and_write_csv(filepath)

    end_1 = obj_cad.count_atoms(line_list)

    line_list_2 = obj_cad.read_file_and_write_csv_for_indentation(filepath)
    end_2 = obj_cad.count_atoms_for_indentation(line_list_2)
    #print(end)
   