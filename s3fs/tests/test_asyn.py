import s3fs
import inspect


def test_when_sync_methods_are_disabled():
    class TestFS(s3fs.S3FileSystem):
        mirror_sync_methods = False

    inst = TestFS()

    # assert that required overrides
    # (meaning AsyncFileSystem throwing NotImplemented errors)
    # are exposed as true async functions
    assert inspect.iscoroutinefunction(inst._info)
    assert not inspect.iscoroutinefunction(inst.info)
    assert inst.info.__qualname__ == "AbstractFileSystem.info"

    # try to assert the same thing for manual attrs using
    # `prop = sync_wrapper(_async_prop)`
    assert inspect.iscoroutinefunction(inst._call_s3)
    assert not inspect.iscoroutinefunction(inst.call_s3)
    assert inst.call_s3.__qualname__ == "S3FileSystem._call_s3"
