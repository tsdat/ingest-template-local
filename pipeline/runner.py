import os
from typing import List
from .pipeline import Pipeline
from tsdat import FilesystemStorage


def run_pipeline(input_files: List[str]):

    # Load the config files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_dir = os.path.join(dir_path, "../config")
    pipeline_config = os.path.join(config_dir, 'pipeline_config.yml')
    storage_config = os.path.join(config_dir, 'storage_config.yml')

    # Create storage for running on local filesystem
    storage = FilesystemStorage.from_config(storage_config)

    # Create pipeline
    pipeline = Pipeline(pipeline_config, storage)

    # Run the pipeline on the given files
    for file_path in input_files:
        if os.path.isdir(file_path):
            for root, dirs, files in os.walk(file_path):
                for name in files:
                    path = os.path.join(root, name)
                    pipeline.run(path)
        else:
            pipeline.run(file_path)
