from . import operation

class ShellOperation(operation.Operation):
    """ Executes a shell operation. """

    def __init__(self, command):
        subprocess.popen(command.split()
