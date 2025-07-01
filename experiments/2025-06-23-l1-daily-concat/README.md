# PADRE MEDDEA Data Processing Notebooks

Below are detailed descriptions of the three notebooks used for processing PADRE MEDDEA mission data.


## test_file_generation.ipynb

### Purpose
This notebook validates the raw-to-L0 data processing pipeline by reprocessing raw data files and verifying the output.

### Methodology
1. Processes raw `.DAT` files from the PADRE-MEDDEA mission using the calibration pipeline
2. Converts raw telemetry packets into structured FITS files
3. Logs SOLARNET Validation errors for the L0 FITS files


## file_concat_testing.ipynb

### Purpose
This notebook develops and tests the file concatenation functionality used in the PADRE-MEDDEA data pipeline.

### Methodology
1. Loads test files from the project's test directory
2. Implements key concatenation functions:
   - Data structure initialization
   - Input file concatenation
   - Sorting data by timestamp
   - Filtering data by time range
   - Splitting data by day boundaries
3. Tests concatenation on multiple file types (photon events, housekeeping, spectrum)
4. Validates outputs against SOLARNET metadata schema standards

## concat_pipeline_validation.ipynb

### Purpose
This notebook explores the pipeline-generated L1 files, downloads examples, and performs validation checks.

### Methodology
1. Downloads L1 data files from the PADRE-MEDDEA pipeline server
2. Examines file structure and metadata of different data products
3. Inspects provenance information tracking the source of concatenated data
4. Validates files against the SOLARNET metadata schema
5. Analyzes data content and structure for different data products (spectrum, housekeeping)
