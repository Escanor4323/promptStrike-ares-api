"""
ares-api · PDF Generator (pdf_generator.py)

Purpose
-------
Assemble assessment data into a professional PDF or HTML report
using WeasyPrint.

Responsibilities
----------------
- Accept structured report data (project metadata, assessments,
  attack results, statistics).
- Render an HTML template with the following sections:
    • Timestamp per page.
    • Project metadata (name, owner, creation date).
    • LLM count visualization data (targets tested).
    • Attack success / fail counts (totals and per-target
      breakdowns).
    • All successful payloads (the prompts that bypassed the
      LLM's defenses).
- Convert the rendered HTML to PDF via WeasyPrint.
- Return the path to the generated file.

Key Interfaces
--------------
    def generate_pdf(report_data: dict, output_path: Path) -> Path:
        \"\"\"Render *report_data* to a PDF file at *output_path*.
        Returns the path to the written file.\"\"\"
        ...

    def generate_html(report_data: dict, output_path: Path) -> Path:
        \"\"\"Render *report_data* to a standalone HTML file.\"\"\"
        ...
"""
