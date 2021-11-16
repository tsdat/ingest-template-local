import os
import shutil
import xarray as xr

from tsdat import Config, DSUtil, FilesystemStorage
from pipeline.pipeline import Pipeline

_test_dir = os.path.dirname(os.path.realpath(__file__))
_project_dir = os.path.dirname(_test_dir)
_config_dir = os.path.join(_project_dir, "config")

DATA_PATH = os.path.join(_project_dir, "data", "inputs")
STORAGE_PATH = os.path.join(_project_dir, "storage", "root", "test")

PIPELINE_CONFIG = os.path.join(_config_dir, "pipeline_config.yml")
STORAGE_CONFIG = os.path.join(_config_dir, "storage_config_dev.yml")

EXAMPLE_FILE = os.path.join(DATA_PATH, "lidar.z06.00.20201201.000000.sta")

EXPECTED_FILE = os.path.join(
    _test_dir, "expected", "morro.buoy_z06-lidar-10min.a1.20201201.001000.nc"
)


def delete_existing_outputs(storage_config_file: str):
    example_path = os.path.dirname(os.path.dirname(storage_config_file))
    storage_path = os.path.join(example_path, "storage")
    if os.path.isdir(storage_path):
        shutil.rmtree(storage_path)


def test_configuration_files_are_valid():
    assert Config.load(PIPELINE_CONFIG)
    assert FilesystemStorage.from_config(STORAGE_CONFIG)


def test_pipeline_produced_expected_data() -> bool:
    delete_existing_outputs(STORAGE_CONFIG)

    filename = os.path.basename(EXPECTED_FILE)
    pipeline = Pipeline(PIPELINE_CONFIG, STORAGE_CONFIG)
    pipeline.run(EXAMPLE_FILE)

    # Retrieve the output data file
    loc_id = pipeline.config.pipeline_definition.location_id
    datastream = DSUtil.get_datastream_name(config=pipeline.config)
    root: str = pipeline.storage._root
    output_file = os.path.join(root, loc_id, datastream, filename)

    # Assert that the basename of the processed file and expected file match
    assert os.path.isfile(output_file)

    # Compare data and optionally attributes to ensure everything matches.
    ds_out: xr.Dataset = xr.open_dataset(output_file)
    ds_exp: xr.Dataset = xr.open_dataset(EXPECTED_FILE)

    xr.testing.assert_allclose(ds_out, ds_exp)
