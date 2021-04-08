# ingest-template-local
Ingest template for a new pipeline that runs on your local filesystem.

## Prerequisites
Install Python 3

Install the tsdat Python dependencies:

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
./run_pipeline.py $LIST_OF_FOLDERS_OR_FILES
```
Example:
```bash
./run_pipeline.py tests/data
```

Will process all the files in the tests/data folder.

## Running/debugging the pipeline via a unit test