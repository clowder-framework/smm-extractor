#!/usr/bin/env python

"""Example extractor based on the clowder code."""
import posixpath

import pandas as pd
import json
import os
import csv
import types
import pickle
from datetime import datetime

import logging
from pyclowder.extractors import Extractor
import pyclowder.files

from algorithm import algorithm
import requests

def save_local_output(localSavePath, fname, output_data):
    """
    save output in memory first to local file
    :param localSavePath: local saved file
    :param remoteSavePath: remote save file path
    :param fname: filename
    :param output_data: the actual data
    :return: local saved file path
    """
    # json
    if isinstance(output_data, dict):
        fname += '.json'
        with open(os.path.join(localSavePath, fname), 'w') as f:
            json.dump(output_data, f)

    # dataframe to csv
    elif isinstance(output_data, pd.DataFrame):
        fname += '.csv'
        output_data.to_csv(fname, encoding='utf-8')

    # string to html
    elif isinstance(output_data, str):
        fname += '.html'
        with open(os.path.join(localSavePath, fname), 'w') as f:
            f.write(output_data)

    # list(list) to csv
    elif isinstance(output_data, list) \
            and (isinstance(output_data[0], list) or isinstance(output_data[0],
                                                                tuple)):
        fname += '.csv'
        with open(os.path.join(localSavePath, fname), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in output_data:
                try:
                    writer.writerow(row)
                except UnicodeEncodeError as e:
                    print(e)

    # special case
    elif isinstance(output_data, types.GeneratorType):
        if fname == 'gephi':
            fname += '.gml'
        elif fname == 'pajek':
            fname += '.net'
        else:
            fname += '.unknown'

        with open(os.path.join(localSavePath, fname), 'w', newline='',
                  encoding='utf-8') as f:
            for line in output_data:
                f.write(line + '\n')

    # else pickle the object
    else:
        fname += '.pickle'
        with open(os.path.join(localSavePath, fname), 'wb') as f:
            pickle.dump(output_data, f)

    return os.path.join(localSavePath, fname)


# TODO wrap this into method on pyclowder
def create_output_folder(dataset_id, host, secret_key):
    url = posixpath.join(host, f'api/v2/datasets/{dataset_id}/folders')
    headers = {"Content-Type": "application/json",
               "X-API-KEY": secret_key}
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    folder_data = {"name": current_timestamp}
    response = requests.post(url, json=folder_data, headers=headers)
    if response.status_code == 200:
        return response.json().get("id")
    else:
        print(f"Error creating folder: {response.status_code} {response.text}")
        return None


class SmmExtractor(Extractor):
    """Count the number of characters, words and lines in a text file."""
    def __init__(self):
        Extractor.__init__(self)

        # parse command line and load default logging configuration
        self.setup()

        # setup logging for the exctractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

    def process_message(self, connector, host, secret_key, resource, parameters):
        # this extractor runs on dataset
        # uncomment to see the resource
        logger = logging.getLogger(__name__)
        inputfile = resource["local_paths"][0]
        dataset_id = resource['parent'].get('id')

        df = pd.read_csv(inputfile)
        connector.message_process(resource, "Loading contents of file...")

        # execute the algorithm
        # Parse user parameters to determine which column to analyze
        userParams = parameters.get('parameters')

        output = algorithm(df, userParams)
        connector.message_process(resource, "Running the algorithm...")

        # Create folder to save output
        clowder_version = int(os.getenv('CLOWDER_VERSION', '1'))
        if clowder_version == 2:
            connector.message_process(resource, "Creating output folder...")
            folder_id = create_output_folder(dataset_id, host, secret_key)
            if folder_id is not None:
                connector.message_process(resource, f"folder id: {folder_id} created ...")
        else:
            folder_id = None
        for fname, output_data in output.items():
            if fname != 'uid':
                local_output_path = save_local_output("", fname, output_data)
                connector.message_process(resource, "Saving " + local_output_path + "...")
                uploaded_file_id = pyclowder.files.upload_to_dataset(connector, host, secret_key, dataset_id,
                                                                     local_output_path,
                                                                     folder_id=folder_id)
                connector.message_process(resource, local_output_path + " saved...")

                connector.message_process(resource, "Writing metadata...")
                metadata = self.get_metadata(userParams, 'file', uploaded_file_id, host)
                pyclowder.files.upload_metadata(connector, host, secret_key, uploaded_file_id, metadata)
                connector.message_process(resource, "Metadata written...")


if __name__ == "__main__":
    extractor = SmmExtractor()
    extractor.start()
