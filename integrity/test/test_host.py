import unittest
from .. import hosts

error_messages = {
    'dup_type': 'The result of duplicating a host {0} times was not a list.',
    'dup_length': 'Duplication result has length {0} instead of {1}.',
    'dns_resolution': '"{0}" resolved to address "{1}" instead of "{2}".',
}

class TestHost(unittest.TestCase):
    localhost = hosts.Host()

#   TODO: Figure out how to test DNS appropriately. If someone doesn't have
#         localhost in their hosts file - then this example would fail.

#    def test_dns_resolution(self):
#        """ Tests whether or not hosts are resolving DNS addresses. """

#        expected_address = '127.0.0.1'

#        self.assertEqual(self.localhost.address, '127.0.0.1',
#            error_messages['dns_resolution'].format(self.localhost.hostname,
#                                                    self.localhost.address,
#                                                    expected_address))


    def test_duplication(self):
        """ Tests whether or not host duplication is functioning properly. """

        # Verifies the result of multiplying by zero, one, and two.
        for host_count in xrange(3):
            hosts = self.localhost * host_count

            self.assertIs(hosts.__class__, list,
                          error_messages['dup_type'].format(host_count))

            self.assertEqual(len(hosts), host_count,
                error_messages['dup_length'].format(len(hosts), host_count))

        # Verifies that negative duplication throws a ValueError.
        def negative_duplicator():
            self.localhost * -1

        self.assertRaises(ValueError, negative_duplicator)
