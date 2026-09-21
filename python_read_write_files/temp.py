from tempfile import SpooledTemporaryFile as _SpooledTemporaryFile


class SpooledTemporaryFile(_SpooledTemporaryFile):
    def __getattr__(self, item):
        return getattr(self._file, item)
