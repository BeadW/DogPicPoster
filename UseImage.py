class PostImage:
    def __init__(self, content):
            self.key = None
            self.content = content

    def set_token(self):
        setattr(self, 'key', ('######'))
