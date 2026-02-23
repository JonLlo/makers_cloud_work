class Post:
    def __init__(self, title, content, tags=None, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []
