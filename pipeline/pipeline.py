from typing import Dict

import xarray as xr
from tsdat.pipeline import IngestPipeline


class Pipeline(IngestPipeline):

    def apply_corrections(self, dataset: xr.Dataset, raw_mapping: Dict[str, xr.Dataset]) -> xr.Dataset:
        """-------------------------------------------------------------------
        Pipeline hook that can be used to apply standard corrections for the
        instrument/measurement or calibrations. This method is called
        immediately after the dataset is converted to standard format and
        before any QC tests are applied.

        If corrections are applied, then the `corrections_applied` attribute
        should be updated on the variable(s) that this method applies
        corrections to.

        Args:
            dataset (xr.Dataset):   A standardized xarray dataset where the
                                    variable names correspond with the output
                                    variable names from the config file.
            raw_mapping (Dict[str, xr.Dataset]):    The raw dataset mapping.

        Returns:
            xr.Dataset: The input xarray dataset with corrections applied.
        -------------------------------------------------------------------"""
        return dataset

    def customize_dataset(self, dataset: xr.Dataset, raw_mapping: Dict[str, xr.Dataset]) -> xr.Dataset:
        """-------------------------------------------------------------------
        Hook to allow for user customizations to the standardized dataset such
        as inserting a derived variable based on other variables in the
        dataset.  This method is called immediately after the apply_corrections
        hook and before any QC tests are applied.

        Args:
            dataset (xr.Dataset): The dataset to customize.
            raw_mapping (Dict[str, xr.Dataset]):    The raw dataset mapping.

        Returns:
            xr.Dataset: The customized dataset.
        -------------------------------------------------------------------"""
        return dataset

    def customize_raw_datasets(self, raw_dataset_mapping: Dict[str, xr.Dataset]) -> Dict[str, xr.Dataset]:
        """-------------------------------------------------------------------
        Hook to allow for user customizations to one or more raw xarray Datasets
        before they merged and used to create the standardized dataset.  The
        raw_dataset_mapping will contain one entry for each file being used
        as input to the pipeline.  The keys are the standardized raw file name,
        and the values are the datasets.

        This method would typically only be used if the user is combining
        multiple files into a single dataset.  In this case, this method may
        be used to correct coordinates if they don't match for all the files,
        or to change variable (column) names if two files have the same
        name for a variable, but they are two distinct variables.

        This method can also be used to check for unique conditions in the raw
        data that should cause a pipeline failure if they are not met.

        This method is called before the inputs are merged and converted to
        standard format as specified by the config file.

        Args:
            raw_dataset_mapping (Dict[str, xr.Dataset])     The raw datasets to
                                                            customize.
        Returns:
            Dict[str, xr.Dataset]: The customized raw dataset.
        -------------------------------------------------------------------"""
        return raw_dataset_mapping

    def create_and_persist_plots(self, dataset: xr.Dataset) -> None:
        """-------------------------------------------------------------------
        Hook to allow users to create plots from the xarray dataset after
        processing and QC have been applied and just before the dataset is
        saved to disk.

        To save on filesystem space (which is limited when running on the
        cloud via a lambda function), this method should only
        write one plot to local storage at a time. An example of how this
        could be done is below:

        ```
        filename = DSUtil.get_plot_filename(dataset, "sea_level", "png")
        with self.storage._tmp.get_temp_filepath(filename) as tmp_path:
            fig, ax = plt.subplots(figsize=(10,5))
            ax.plot(dataset["time"].data, dataset["sea_level"].data)
            fig.save(tmp_path)
            storage.save(tmp_path)

        filename = DSUtil.get_plot_filename(dataset, "qc_sea_level", "png")
        with self.storage._tmp.get_temp_filepath(filename) as tmp_path:
            fig, ax = plt.subplots(figsize=(10,5))
            DSUtil.plot_qc(dataset, "sea_level", tmp_path)
            storage.save(tmp_path)
        ```

        Args:
            dataset (xr.Dataset):   The xarray dataset with customizations and
                                    QC applied.
        -------------------------------------------------------------------"""
        pass
