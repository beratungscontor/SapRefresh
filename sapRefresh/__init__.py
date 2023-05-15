# -*- coding: utf-8 -*-
"""
Created on 3/14/2021
Author: Arnold Souza
Email: arnoldporto@gmail.com
"""
import pathlib
import os
import pandas as pd
import yaml

from sapRefresh.Core.Time import timeit

@timeit
def import_global_configurations():
    """import all the necessary information so that the script can work well"""
    # Pfad des aktuellen Moduls
    current_module_path = os.path.abspath(__file__)
    # Verzeichnis des aktuellen Moduls
    current_module_directory = os.path.dirname(current_module_path)
    # Pfad zur Konfigurationsdatei im Modulverzeichnis
    config_file_path = os.path.join(current_module_directory, 'config.yml')
    # Config Datei einlesen
    with open(config_file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    df_global_configs = pd.read_excel(yaml_data['CONFIG_PATH'], sheet_name='global_configs')
    os.environ['CONFIG_PATH'] = yaml_data['CONFIG_PATH']
    os.environ['LOG_PATH'] = str(pathlib.Path(df_global_configs.query('description=="path-log_directory"')['value'].values[0]))
    return df_global_configs


# import global configurations
global_configs_df = import_global_configurations()
