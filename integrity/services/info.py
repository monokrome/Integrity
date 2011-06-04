class ServiceInfo(object):
    services = []

    def add(self, service):
        """ Add a new service to this object's service info. """

        self.services.append(service)

    def remove(self, service):
        """ Removes a specific service instance or type from this services list.

        """

        for iter in self.services:
            if iter is service or iter.__class__ is service:
                self.services.remove(iter)
