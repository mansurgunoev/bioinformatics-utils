# Bioinformatics Utils

Homework 4 for Python.

This project contains functions for working with FASTQ, FASTA and BLAST result files.

## Requirements

Python 3 is required. No additional libraries are needed.

## Functions

### filter_fastq()

This function filters FASTQ reads by GC content, sequence length and average quality.

The limits for each parameter can be changed. The result is saved in the `filtered` folder.

### convert_multiline_fasta_to_oneline()

This function converts a multiline FASTA file into a one-line FASTA file. The headers are kept, and each sequence is written on one line.

### parse_blast_output()

This function reads BLAST results and selects the first hit for each query.

The descriptions are sorted alphabetically and saved in a separate file.

## Usage

Import the required function from `bioinformatics_utils.py` and provide the input and output file names. Filtering parameters can also be set for FASTQ files.

## Project structure

`bioinformatics_utils.py` contains the main functions.

`helpers/fastq.py` contains helper functions for FASTQ filtering.

`helpers/bio_files.py` contains a helper function for BLAST results.
