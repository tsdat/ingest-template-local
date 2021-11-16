import xarray as xr
from tsdat.io import AbstractFileHandler
from tsdat import Config


class DummyFileHandler(AbstractFileHandler):
    """-------------------------------------------------------------------
    Dummy FileHandler. Users should customize this class if they want to
    read or write data in a format that is not supported out-of-the-box.

    To register this FileHandler for use in the IngestPipeline, users must
    update the config/storage_config_<dev or prod>.yml file. Note that the
    classname for this FileHandler should be: `pipeline.filehandlers.DummyFileHandler`

    See https://tsdat.readthedocs.io/ for more file handler examples.
    -------------------------------------------------------------------"""

    def write(self, ds: xr.Dataset, filename: str, config: Config, **kwargs):
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
        raise NotImplementedError

    def read(self, filename: str, **kwargs) -> xr.Dataset:
        """-------------------------------------------------------------------
        Classes derived from the FileHandler class can implement this method.
        to read a custom file format into a xr.Dataset object.

        Args:
            filename (str): The path to the file to read in.

        Returns:
            xr.Dataset: An xr.Dataset object
        -------------------------------------------------------------------"""
        raise NotImplementedError
