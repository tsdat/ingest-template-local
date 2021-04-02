import xarray as xr
from tsdat.io import AbstractFileHandler
from tsdat import Config


class DummyFileHandler(AbstractFileHandler):
    """-------------------------------------------------------------------
    Class containing placeholder code for a custom file reader.

    See https://tsdat.readthedocs.io/ for more file handler examples.
    -------------------------------------------------------------------"""
    @staticmethod
    def write(ds: xr.Dataset, filename: str, config: Config, **kwargs):
        """-------------------------------------------------------------------
        Classes derived from the FileHandler class can implement this method
        to save to a custom file format.

        Args:
            ds (xr.Dataset): The dataset to save.
            filename (str): An absolute or relative path to the file including
                            filename.
            config (Config, optional):  Optional Config object. Defaults to
                                        None.
        -------------------------------------------------------------------"""
        raise NotImplementedError("Error: this file format should not be used to write to.")

    @staticmethod
    def read(filename: str, **kwargs) -> xr.Dataset:
        """-------------------------------------------------------------------
        Classes derived from the FileHandler class can implement this method.
        to read a custom file format into a xr.Dataset object.

        Args:
            filename (str): The path to the file to read in.

        Returns:
            xr.Dataset: An xr.Dataset object
        -------------------------------------------------------------------"""

        # Create dummy data dictionary
        dictionary = {
            # Dimensions / coordinates
            "time": {"dims": ["time"], "data": [1, 2, 3]},

            # Data variables
            "a": {"dims": ["time"], "data": [1.1, 2.2, 3.3]},
            "b": {"dims": ["time"], "data": [1.4, 2.5, 3.6]},
            "c": {"dims": ["time"], "data": [1.7, 2.8, 3.9]}
        }
        return xr.Dataset.from_dict(dictionary)
