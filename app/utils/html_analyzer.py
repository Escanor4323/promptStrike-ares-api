"""
ares-api · HTML Analyzer (html_analyzer.py)

Purpose
-------
Auto-detect LLM type by analyzing the HTML content of a target
URL's response page. Inspects page metadata rather than the URL
itself.

Responsibilities
----------------
- Fetch the HTML body from a given URL (use ``httpx`` or similar
  async HTTP client).
- Parse the ``<title>``, ``<meta>`` tags, and ``<script>`` tags
  for identifiable markers of known LLM platforms.
- Map detected markers to a canonical LLM name string
  (e.g., ``"ChatGPT"``, ``"Claude"``, ``"Gemini"``).
- Return ``None`` when no match is found (graceful failure).

Key Interfaces
--------------
    async def detect_llm_type(url: str) -> str | None:
        \"\"\"Fetch the HTML at *url*, analyze it, and return the
        detected LLM platform name or None if unrecognised.\"\"\"
        ...
"""
