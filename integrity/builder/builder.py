class Build(object):
    """ A specific build which needs to occur. """

    # This represents the process that occurs when the build executes. It should
    # be an iterable of callables.
    process = []

    def __init__(self, hosts):
        self.hosts = hosts

    def initialize(self):
        """ Does any work that is required to occur prior to being building. """

        pass

    def clean(self):
        """ Clean up any data that might be left after a build finishes. """

        pass

    def __call__(self, *args, **kwargs):
        """ Allows builds to be executed as functions. """

        self.run(*args, **kwargs)

    def execute(self):
        """ Executes the steps required in order to perform this build. """

        for operation in self.process:
            operation()
