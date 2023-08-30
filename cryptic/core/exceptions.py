
class StorageClosedError(Exception):

    def __init__(self, storage):
        super().__init__(f'Storage "{storage.name}" at {storage.location} is closed')
