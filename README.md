# ingest-template-local

This is a template repository that can be used to set up tsdat ingests on your local computer. 

- other templates: https://github.com/tsdat/template-repositories
- tsdat homepage: https://github.com/tsdat/tsdat
- tsdat documentation: https://tsdat.readthedocs.io

## Getting Started

1. Install dependencies. We recommend using [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to manage your environment:
    ```
    $ conda create --name tsdat-local python=3.8
    ...
    $ conda activate tsdat-local
    $ pip install -r requirements.txt
    ```

2. Add your data:
    * `data/inputs/<your data file>`

3. Customize the configuration files:
    * `config/pipeline_config.yml`
    * `config/storage_config_dev.yml`
    * `config/storage_config_prod.yml` (Optional – can delete this)

4. Customize pipeline code:
    * `pipeline/pipeline.py`
    * `pipeline/filehandlers.py` (Optional)
    * `pipeline/qc.py` (Optional)
    * `pipeline/runner.py` (Optional)

5. Run your ingest:
    ```
    $ python run_pipeline.py
    ```

    Note that you can also specify some other options:
    ```    
    # Specify which storage configuration to use (defaults to prod)
    $ python run_pipeline.py --mode prod
    $ python run_pipeline.py --mode dev

    # Specify path to different inputs
    $ python run_pipeline.py [PATH_TO_INPUTS]

    # Run the test suite and generate a coverage report
    pytest --cov --report-type=html
    ```

6. Customize this README to better reflect your project

## Additional Resources

- Data standards specifications: https://github.com/tsdat/data_standards
- Learn more about xarray: 
    - https://xarray.pydata.org
    - https://github.com/pydata/xarray
- Other useful python tips and tricks:
    - matplotlib guide: https://realpython.com/python-matplotlib-guide/
    - pytest: https://github.com/pytest-dev/pytest
    - black: https://black.readthedocs.io/