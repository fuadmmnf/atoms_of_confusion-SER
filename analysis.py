import glob
import os
import sys
import numpy as np
import pathlib
from collections import defaultdict
from os.path import join
import pandas as pd
from pathlib import Path
import seaborn as sns
from scipy import stats
import scikit_posthocs as sp

import matplotlib.pyplot as plt

plt.show()

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
    print(os.listdir(folder_absolute_path))
    for file in os.listdir(folder_absolute_path):

        project_name = file.split('.')[0]
        if '_total' in file or project_name in ['hadoop']:
            continue
        print('processing:', file)
        project_df = pd.read_csv(str(folder_absolute_path / file))
        revision_wise_metric_totals = project_df.groupby('revision').sum()[class_metrics_list]
        revision_wise_metric_totals.to_csv((str(folder_absolute_path) + '/' + project_name + '_total.csv'))


# calculate_metric_statistics()


def latest_atom_revision():
    folder_absolute_path = pathlib.Path(__file__).parent / "res/atoms"

    latest_atoms = pd.DataFrame()
    for file in os.listdir(folder_absolute_path):
        if '_total' not in file:
            continue
        project_name = file.split('_total')[0]
        print(project_name)
        metric_df = pd.read_csv(str(pathlib.Path(__file__).parent / f"res/ck/{project_name}_total.csv"))
        project_df = pd.read_csv(str(folder_absolute_path / file))
        project_df = project_df.assign(project=project_name)
        project_df = project_df.assign(
            loc=metric_df.loc[metric_df['revision'] == metric_df['revision'].max()]['loc'].iloc[0]/1000)
        # project_df['loc'] = metric_df.loc[metric_df['revision'] == metric_df['revision'].max()]['loc'].to_numpy()
        # print(metric_df.loc[metric_df['revision'] == metric_df['revision'].max()]['loc'].iloc[0])
        latest_atoms = pd.concat([latest_atoms, project_df.loc[project_df['revision'] == project_df['revision'].max()]])
    latest_atoms.to_csv(str(folder_absolute_path / 'latest_revisions.csv'))


# latest_atom_revision()


def atom_rates_graph():
    project_wise_df = pd.read_excel(str(pathlib.Path(__file__).parent / "res/merged.xlsx"),
                                    sheet_name='project_wise_rate')
    g = sns.catplot(data=project_wise_df.sort_values('Rate', ascending=False), x="Rate", y="Project", kind="bar",
                    alpha=0.35)
    g.fig.set_size_inches(15, 8)
    g.fig.subplots_adjust(top=0.81, right=0.86)

    # extract the matplotlib axes_subplot objects from the FacetGrid
    ax = g.facet_axis(0, 0)

    # iterate through the axes containers
    for c in ax.containers:
        labels = [f'{(v.get_width()):.4f}' for v in c]
        ax.bar_label(c, labels=labels, label_type='center')
    # fig = sns.barplot(data=project_wise_df[['Project', 'Rate']], orient='h')
    g.savefig(str(pathlib.Path(__file__).parent / "res/graphs/project_wise_rate"))
    plt.clf()

    atom_wise_df = pd.read_excel(str(pathlib.Path(__file__).parent / "res/merged.xlsx"),
                                 sheet_name='atom_wise_rate')
    g = sns.catplot(data=atom_wise_df.sort_values('Rate', ascending=False), x="Rate", y="Atom", kind="bar",
                    alpha=0.35)
    g.fig.set_size_inches(15, 8)
    g.fig.subplots_adjust(top=0.81, right=0.86)

    # extract the matplotlib axes_subplot objects from the FacetGrid
    ax = g.facet_axis(0, 0)

    # iterate through the axes containers
    for c in ax.containers:
        labels = [f'{(v.get_width()):.4f}' for v in c]
        ax.bar_label(c, labels=labels, label_type='edge')
    # fig = sns.barplot(data=project_wise_df[['Project', 'Rate']], orient='h')
    g.savefig(str(pathlib.Path(__file__).parent / "res/graphs/atom_wise_rate"))
    plt.clf()

    latest = pd.read_excel(str(pathlib.Path(__file__).parent / "res/merged.xlsx"),
                           sheet_name='merged')
    pivot_df = pd.DataFrame()

    for index, row in latest.iterrows():
        for a in identified_atoms_list:
            pivot_df = pivot_df.append({"project": row['project'], "atom": a, "count": row[a] / (row['loc']/1000)},
                                       ignore_index=True)
    pivot_df = pivot_df.pivot("atom", 'project', 'count')
    fig, ax = plt.subplots(figsize=(40, 22))  # Sample figsize in inches
    sns.set(font_scale=1.4)
    sns.color_palette("light:b", as_cmap=True)

    g = sns.heatmap(pivot_df, annot=pivot_df.rank(axis="rows"), ax=ax, cmap="Blues")
    g.set_xticklabels(g.get_xticklabels(), fontsize=20)
    g.set_yticklabels(g.get_yticklabels(), fontsize=20)

    # g.xaxis.tick_top()  # x axis on top
    # g.xaxis.set_label_position('top')
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45)
    # g.set(xlabel="projects", ylabel="atom")
    g.get_figure().savefig(str(pathlib.Path(__file__).parent / "res/graphs/heatmap"))

    plt.clf()


# atom_rates_graph()

def friedman_test():
    latest = pd.read_excel(str(pathlib.Path(__file__).parent / "res/latest_revisions.xlsx"),
                           sheet_name='latest_revisions')
    groups = []
    for a in identified_atoms_list:
        # print(row[identified_atoms_list].values)
        groups.append(latest[a].values / (latest['loc'].values/1000))
    print('friendman test:\n')
    print(
        stats.friedmanchisquare(groups[0], groups[1], groups[2], groups[3], groups[4], groups[5], groups[6], groups[7],
                                groups[8], groups[9], groups[10], groups[11]))

    # Combine three groups into one array

    # print(len(groups))
    data = np.array(groups)

    # Conduct the Nemenyi post-hoc test
    df = sp.posthoc_nemenyi_friedman(data.T)
    print(df)
    df.columns = identified_atoms_list
    df.index = identified_atoms_list
    df.to_csv(str(pathlib.Path(__file__).parent / "res/friedman_nemenyi.csv"))
    print('\nfriendman nemenyi test:\n')
    print(df)
    print('\n\n\n')


friedman_test()


def atom_metric_correlation():
    folder_absolute_path = pathlib.Path(__file__).parent / "res/atoms"

    project_folders = [join(folder_absolute_path, f) for f in os.listdir(folder_absolute_path) if
                       os.path.isdir(join(folder_absolute_path, f))]
    total_atom_df = pd.DataFrame()
    total_metric_df = pd.DataFrame()
    # get all project all revision normalized stats in one csv
    for project_folder in project_folders:
        project_name = project_folder.split('/')[-1]
        atom_df = pd.read_csv(str(folder_absolute_path / (project_name + '_total.csv'))).sort_values('revision')
        metric_df = pd.read_csv(str(pathlib.Path(__file__).parent / f"res/ck/{project_name}_total.csv")).sort_values('revision')
        # print(project_name, len(atom_df), len(metric_df))
        for a in identified_atoms_list:
            atom_df[a] = atom_df[a]/(metric_df['loc']/1000)
        total_atom_df = pd.concat([total_atom_df, atom_df[identified_atoms_list]])
        for a in class_metrics_list:
            if a in ['loc']:
                metric_df[a] = metric_df[a] / 1000
            else:
                metric_df[a] = metric_df[a] / (metric_df['loc']/1000)
        total_metric_df = pd.concat([total_metric_df, metric_df[class_metrics_list]])

    # print(total_atom_df.info())
    # print(total_metric_df.info())

    for col in total_metric_df.columns:
        print('Calculating coorelation for: ', col)
        print(total_atom_df.corrwith(total_metric_df[col]), end='\n\n')

atom_metric_correlation()
