import socket
import copy

from .. import services

error_messages = {
    'signed_dup': 'Can not multiply a {0} object by negative values.'
}

def get_hostname(self):
    return self._hostname

def set_hostname(self, value):
    self._hostname = value
    self._address = socket.gethostbyname(value)

def get_address(self):
    return self._address

def set_address(self, value):
    self._address = value
    self._hostname = socket.gethostbyaddr(value)

class Host(object):
    """ A single device which can be used by our systems. """

    hostname = property(get_hostname, set_hostname)
    _hostname = None

    address = property(get_address, set_address)
    _address = None

    services = services.ServiceInfo()

    def __init__(self, hostname='localhost'):
        self.hostname = hostname

    def __mul__(self, val):
        """ Produces more hosts which exactly replicate this one. """

        if val < 0:
            raise ValueError(
                error_messages['signed_dup'].format(self.__class__.__name__)
            )

        result = []

        for i in xrange(val):
            result.append(copy.deepcopy(self))

        return result
