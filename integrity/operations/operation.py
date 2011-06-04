class Operation(object):
    def __call__(self, *args, **kwargs):
        self.execute(*args, **kwargs)

    def execute(self):
        raise NotImplementedError()

