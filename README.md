# ingest-template-local
Ingest template for a new pipeline that runs on your local filesystem.

## Prerequisites
Install Python 3.8+. We recommend using anaconda or venv to manage your python environment.

Install tsdat:

```bash
pip3 install tsdat
```

## Project Hierarchy
* config
* pipeline
* tests
* run_pipeline.py

## Running the pipeline from the command line
```bash
python3 run_pipeline.py [LIST_OF_FOLDERS_OR_FILES]
```
Example:
```bash
python3 run_pipeline.py data/inputs
```

Will process all the files in the data/inputs folder.

## Running/debugging the pipeline via a unit test

```bash
python3 tests/test_pipeline.py
```
