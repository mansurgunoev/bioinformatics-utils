from helpers.bio_files import get_best_blast_hits

import os

from helpers.fastq import check_gc, check_length, check_quality


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str = "oneline.fasta"
) -> None:
    """
    Convert multiline FASTA to oneline FASTA.

    Args:
        input_fasta: Path to input FASTA file.
        output_fasta: Path to output FASTA file.

    Returns:
        None.
    """
    with open(input_fasta, "r") as input_file:
        with open(output_fasta, "w") as output_file:
            sequence = ""

            for line in input_file:
                line = line.strip()

                if line.startswith(">"):
                    if sequence:
                        output_file.write(sequence + "\n")

                    output_file.write(line + "\n")
                    sequence = ""
                else:
                    sequence = sequence + line

            if sequence:
                output_file.write(sequence + "\n")


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: tuple = (0, 100),
    length_bounds: tuple = (0, 2**32),
    quality_threshold: float = 0
) -> None:
    """
    Filter FASTQ reads by GC content, length and quality.

    Args:
        input_fastq: Input FASTQ file path.
        output_fastq: Output FASTQ filename.
        gc_bounds: Allowed GC percentage range.
        length_bounds: Allowed sequence length range.
        quality_threshold: Minimum average Phred quality.

    Returns:
        None.
    """
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)

    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)

    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)

    with open(input_fastq, "r") as input_file:
        with open(output_path, "w") as output_file:
            while True:
                header = input_file.readline()

                if header == "":
                    break

                sequence = input_file.readline()
                separator = input_file.readline()
                quality = input_file.readline()

                if not sequence or not separator or not quality:
                    raise ValueError("Incomplete FASTQ record")

                seq = sequence.strip()
                scores = quality.strip()

                if len(seq) != len(scores):
                    raise ValueError("Sequence and quality lengths differ")

                if check_gc(seq, gc_bounds):
                    if check_length(seq, length_bounds):
                        if check_quality(scores, quality_threshold):
                            output_file.write(header)
                            output_file.write(sequence)
                            output_file.write(separator)
                            output_file.write(quality)



def parse_blast_output(
    input_file: str,
    output_file: str = "blast_best_hits.txt"
) -> None:
    """
    Save the best BLAST hit descriptions in alphabetical order.

    Args:
        input_file: Path to BLAST results.
        output_file: Path to output text file.

    Returns:
        None.
    """
    descriptions = get_best_blast_hits(input_file)
    descriptions.sort()

    with open(output_file, "w") as result_file:
        for description in descriptions:
            result_file.write(description + "\n")
