import glob
import os
import sys
import pathlib
from collections import defaultdict
from os.path import join
import pandas as pd
from pathlib import Path

identified_atoms_list = ['type_conversion', 'post_inc_dec', 'pre_inc_dec', 'constant_variable', 'conditional_operator',
                         'arithmetic_as_logic', 'logic_as_control_flow', 'repurposed_variable', 'dead_repeated',
                         'omitted_curly_braces', 'change_of_literal_encoding', 'infix_operator_precedence']

class_metrics_list = ['cbo', 'cboModified', 'fanin', 'fanout', 'wmc', 'dit', 'noc', 'rfc', 'lcom', 'lcom*', 'tcc',
                      'lcc', 'totalMethodsQty', 'staticMethodsQty', 'publicMethodsQty', 'privateMethodsQty',
                      'protectedMethodsQty', 'defaultMethodsQty', 'visibleMethodsQty', 'abstractMethodsQty',
                      'finalMethodsQty', 'synchronizedMethodsQty', 'totalFieldsQty', 'staticFieldsQty',
                      'publicFieldsQty', 'privateFieldsQty', 'protectedFieldsQty', 'defaultFieldsQty', 'finalFieldsQty',
                      'synchronizedFieldsQty', 'nosi', 'loc', 'returnQty', 'loopQty', 'comparisonsQty', 'tryCatchQty',
                      'parenthesizedExpsQty', 'stringLiteralsQty', 'numbersQty', 'assignmentsQty', 'mathOperationsQty',
                      'variablesQty', 'maxNestedBlocksQty', 'anonymousClassesQty', 'innerClassesQty', 'lambdasQty',
                      'uniqueWordsQty', 'modifiers', 'logStatementsQty']


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

        project_wise_metric_df.to_csv(folder_absolute_path / f"{project_folder.split('/')[-1]}.csv")


# combine_atom_revisions()
def calculate_atom_statistics():
    folder_absolute_path = pathlib.Path(__file__).parent / "res/atoms"

    project_folders = [join(folder_absolute_path, f) for f in os.listdir(folder_absolute_path) if
                       os.path.isdir(join(folder_absolute_path, f))]
    for project_folder in project_folders:
        project_name = project_folder.split('/')[-1]
        project_df = pd.read_csv(str(folder_absolute_path / (project_name + '.csv')))
        revision_wise_atom_totals = project_df.groupby('revision').sum()[identified_atoms_list]
        revision_wise_atom_totals.to_csv(str(folder_absolute_path / (project_name + '_total.csv')))


# calculate_atom_statistics()


def calculate_metric_statistics():
    folder_absolute_path = pathlib.Path(__file__).parent / "res/ck"

    for file in os.listdir(folder_absolute_path):
        project_name = file.split('.')[0]
        project_df = pd.read_csv(str(folder_absolute_path / (project_name + '.csv')))
        revision_wise_metric_totals = project_df.groupby('revision').sum()[class_metrics_list]
        revision_wise_metric_totals.to_csv((str(folder_absolute_path) + '/' + project_name + '_total.csv'))


calculate_metric_statistics()
