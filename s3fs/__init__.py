from .core import S3FileSystem, S3File
from .core_sync import S3SyncFileSystem, S3SyncFile
from .mapping import S3Map

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
