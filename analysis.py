import glob
import os
import sys
import pathlib
from collections import defaultdict
from os.path import join
import pandas as pd
from pathlib import Path


def combine_atom_revisions():
    folder_absolute_path = pathlib.Path(__file__).parent / "res/atoms"

    project_folders = [join(folder_absolute_path, f) for f in os.listdir(folder_absolute_path) if
                       os.path.isdir(join(folder_absolute_path, f))]
    for project_folder in project_folders:
        project_wise_metric_df = pd.DataFrame()
        for file in os.listdir(project_folder):
            revision_df = pd.read_csv(project_folder + '/' + file)
            revision_df['revision'] = file.split('_')[0]
            project_wise_metric_df = pd.concat([project_wise_metric_df, revision_df.copy()])
        
        project_wise_metric_df.to_csv(folder_absolute_path / f"merged_{project_folder.split('/')[-1]}.csv")


combine_atom_revisions()
