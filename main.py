import glob
import os
import sys
import pathlib
import shutil
import subprocess
import threading
import zipfile
from collections import defaultdict
from os.path import join
from threading import Thread
from typing import Optional, List

import pandas as pd

import git

# from metric_generator import generate_report


from pathlib import Path

from confusion_atom_detector import ConfusionAtomDetector

if __name__ == '__main__':
    folder_path = 'test_systems'
    # pass
    obj_cad = ConfusionAtomDetector()

    folder_absolute_path = pathlib.Path(__file__).parent / folder_path
    project_folders = [join(folder_absolute_path, f) for f in os.listdir(folder_absolute_path) if
                       os.path.isdir(join(folder_absolute_path, f))]
    for project_folder in project_folders:
        Path(pathlib.Path(__file__).parent / 'res/atoms' / project_folder.split('/')[-1]).mkdir(parents=True,
                                                                                                exist_ok=True)
        print(project_folder)
        if project_folder.split('/')[-1] not in ['elasticsearch']:
            continue

        repo = git.Repo(project_folder)
        master_branch = str(repo.branches[0])
        # if 'master' in str(repo.branches):
        #     master_branch = 'master'
        # elif 'trunk' in str(repo.branches):
        #     master_branch = 'trunk'
        # elif 'main' in str(repo.branches):
        #     master_branch = 'main'
        repo.git.checkout(master_branch, force=True)
        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

        for i in range(len(tags)):
            # print(repo.head.object.hexsha)
            repo.git.checkout(tags[i].path, force=True)
            # print(repo.head.object.hexsha)
            print(f"{i + 1}/{len(tags)}: {project_folder.split('/')[-1]}")
            files_dict = []
            for root, subdirs, files in os.walk(project_folder):
                for file in files:
                    if not file.endswith('.java'):
                        continue
                    files_dict.append(obj_cad.count_atoms(str(os.path.join(root, file))).copy())

            output_absolute = pathlib.Path(__file__).parent / 'res/atoms' / project_folder.split('/')[
                -1] / f"{i}_{tags[i].path.split('/')[-1]}.csv"

            pd.DataFrame(files_dict).to_csv(output_absolute)
            # line_list_2 = obj_cad.read_file_and_write_csv_for_indentation(filepath)
    # end_2 = obj_cad.count_atoms_for_indentation(line_list_2)
    # print(end)
