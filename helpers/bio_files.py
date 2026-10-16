def get_best_blast_hits(input_file: str) -> list[str]:
    """
    Get descriptions of the best BLAST hits.

    Args:
        input_file: Path to BLAST results file.

    Returns:
        List of best hit descriptions.
    """
    descriptions = []

    with open(input_file, "r") as blast_file:
        for line in blast_file:
            if line.startswith("Sequences producing significant alignments:"):
                next(blast_file)
                next(blast_file)

                best_hit = next(blast_file, "")

                if best_hit.strip():
                    description = best_hit.split("  ")[0].strip()
                    descriptions.append(description)

    return descriptions
