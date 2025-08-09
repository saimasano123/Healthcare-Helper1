def tag_chunk(
    text,
    procedure_name,
    procedure_code,
    location,
    cost_avg,
    source_name,
    source_url
):
    """
    Tags a CMS procedure chunk with metadata for downstream retrieval.

    Args:
        text (str): Human-readable summary of the procedure and cost.
        procedure_name (str): Standardized procedure name.
        procedure_code (str): HCPCS procedure code.
        location (str): City and state.
        cost_avg (float): Average submitted charge.
        source_name (str): Originating dataset or API (e.g. "CMS").
        source_url (str): URL to raw source data.

    Returns:
        dict: Struct
        ured chunk with searchable metadata.
    """
    return {
        "text": text,
        "procedure_name": procedure_name,
        "procedure_code": procedure_code,
        "location": location,
        "cost_avg": cost_avg,
        "source_name": source_name,
        "source_url": source_url
    }
