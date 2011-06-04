class Service(object):
    """ A single service that exists on a specific host. """

    name = None
    port = None
    default_port = None

    def __init__(self, port=None):
        self.port = port
        self.provided_by = provided_by
        self.provides = provides
