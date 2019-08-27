
class Operation:

    def __init__(self, id, type, title, platform, artifact, image, dependencies=None ):
        self._id = id
        self._type = type
        self._title = title
        self._platform = platform
        self._artifact = artifact
        self._image = image
        if dependencies:
            self._dependencies = dependencies
        else:
            self._dependencies = []

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def title(self):
        return self._title

    @property
    def platform(self):
        return self._platform

    @property
    def artifact(self):
        return self._artifact

    @property
    def image(self):
        return self._image

    @property
    def dependencies(self):
        return self._dependencies

    def __eq__(self, other: object) -> bool:
        if isinstance(self, other.__class__):
            return self.id == other.id and \
                   self.type == other.type  and \
                   self.title == other.title  and \
                   self.platform == other.platform  and \
                   self.artifact == other.artifact  and \
                   self.image == other.image and \
                   self.dependencies == other.dependencies


class Pipeline:

    def __init__(self, id, title):
        self._id = id
        self._title = title
        self._operations = {}

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def operations(self):
        return self._operations

    def __eq__(self, other: object) -> bool:
        if isinstance(self, other.__class__):
            return self.title == other.title and \
                   self.operations == other.operations
