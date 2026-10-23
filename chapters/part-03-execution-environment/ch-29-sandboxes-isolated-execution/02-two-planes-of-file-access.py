# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 29: Sandboxes: Isolated Execution
# Section: Two planes of file access
# Snippet 2 of this chapter.

backend.upload_files([("/data/sales.csv", csv_bytes)])        # seed before the run (native provider API, not shell)
# ... agent runs ...
results = backend.download_files(["/out/report.png"])          # per-path .path / .content (bytes|None) / .error
