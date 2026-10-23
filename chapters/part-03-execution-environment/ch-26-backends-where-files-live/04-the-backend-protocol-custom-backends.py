# Deep Agents: The Complete Guide to LangChain's Deep Agents (Unofficial)
# Part III: Execution Environment
# Chapter 26: Backends: Where Files Live
# Section: The backend protocol (custom backends)
# Snippet 4 of this chapter.

# Sketch: map virtual paths to object-store keys (S3-style). Import paths/types: check your version.
class S3Backend(BackendProtocol):
    def __init__(self, bucket, prefix): ...
    def ls(self, path):        ...   # list keys under prefix + path -> LsResult(entries=[FileInfo(...)])
    def read(self, file_path, offset=0, limit=2000): ...   # get_object -> ReadResult
    def write(self, file_path, content): ...               # put_object if absent else error result
    def edit(self, file_path, old_string, new_string, replace_all=False): ...
    def glob(self, pattern, path=None): ...
    def grep(self, pattern, path=None, glob=None): ...     # literal search
