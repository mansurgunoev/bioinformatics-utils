def check_gc(sequence: str, gc_bounds: tuple) -> bool:
    """
    Check if GC content is within the given bounds.

    Args:
        sequence: DNA sequence.
        gc_bounds: Minimum and maximum GC percentage.

    Returns:
        True if GC content is within bounds, otherwise False.
    """
    sequence = sequence.upper()

    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = gc_count / len(sequence) * 100

    min_gc = gc_bounds[0]
    max_gc = gc_bounds[1]

    if gc_percent >= min_gc and gc_percent <= max_gc:
        return True
    else:
        return False

def check_length(sequence: str, length_bounds: tuple) -> bool:
    """
    Check if sequence length is within the given bounds.

    Args:
        sequence: DNA sequence.
        length_bounds: Minimum and maximum length.

    Returns:
        True if length is within bounds, otherwise False.
    """
    length = len(sequence)

    min_length = length_bounds[0]
    max_length = length_bounds[1]

    if length >= min_length and length <= max_length:
        return True
    else:
        return False

def check_quality(quality: str, quality_threshold: float) -> bool:
    """
    Check the average Phred+33 quality score.

    Args:
        quality: FASTQ quality string.
        quality_threshold: Minimum average quality.

    Returns:
        True if average quality is high enough, otherwise False.
    """
    total_quality = 0

    for symbol in quality:
        score = ord(symbol) - 33
        total_quality = total_quality + score

    average_quality = total_quality / len(quality)

    if average_quality >= quality_threshold:
        return True
    else:
        return False
