"""
ares-api · CSV Parser (csv_parser.py)

Purpose
-------
Parse analyst-uploaded CSV files containing LLM target URLs.
Validates file format, extracts URLs, and returns a structured,
deduplicated list.

Responsibilities
----------------
- Validate that the uploaded file is a well-formed CSV with the
  expected columns (at minimum a ``url`` column).
- Extract all URL values from the designated column.
- Deduplicate URLs (case-insensitive).
- Strip whitespace and reject obviously malformed URLs.
- Return a list of validated URL strings, or raise a descriptive
  error if the file is invalid.

Key Interfaces
--------------
    def parse_target_csv(file_content: bytes | str) -> list[str]:
        \"\"\"Parse a CSV and return a deduplicated list of
        validated target URLs.

        Raises ValueError on invalid format or missing columns.
        \"\"\"
        ...
"""
