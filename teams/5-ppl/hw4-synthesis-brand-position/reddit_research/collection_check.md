# Collection validation

Verified October 17, 2026 using local JSON files only.

- Discovery files: 10; result entries: 232.
- Thread files: 30; distinct embedded post IDs: 30.
- Expected IDs found: 30/30; missing: 0; duplicates: 0.
- Every thread has a post listing and at least one non-deleted/non-removed comment body.
- Non-deleted/non-removed comment bodies: 617, including 1 AutoModerator bodies.
- All 18 ledger excerpts match exact contiguous source text, with source permalinks.
- Selected brand quotes: 5; persona quote allocation: 2 per persona across 6 distinct excerpts.
- Corrected duplicate: the first `thread_GetStudying_1oktpuh.json` contained `1rndkot`; the replacement now contains `1oktpuh`.

These checks establish local content coverage and quote fidelity, not authenticity of claims or completeness of every comment ever posted. See [coverage.md](coverage.md) for the source inventory.

Check the submitted ledger, manifest, and integrated quotes with `python3 reddit_research/validate_research.py` from the HW4 folder. To also verify every quote against raw files and check saved-file hashes, add `--raw /path/to/reddit_corpus/raw`. Raw files are intentionally retained separately.
