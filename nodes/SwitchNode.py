''' Circuit Nodejs Pool
    copyright© 2024 SJBailey© '''
import udi_interface
import json
import requests
import sys
import time
import urllib3

LOGGER = udi_interface.LOGGER


class SwitchNode(udi_interface.Node):

    def __init__(self, polyglot, primary, address, name, state, status1):

        super(SwitchNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)

        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)

        self.state = state
        self.status1 = status1
        self.address = address
        LOGGER.info(self.address)
        self.name = name
        LOGGER.info(name)
        id = address.strip('zone_')
        id1 = id
        LOGGER.info(id1)
        self.id1 = id1

    def start(self):
        ##### GET Devices ####
        # self.allData = requests.get(
        #    url='{}/api/devices'.format(self.apiBaseUrl))

        if self.state == 1:
            self.setDriver('ST', 1)
        else:
            self.setDriver('ST', 0)

        if self.status1 == 1:
            self.setDriver('GV1', 1)
        else:
            self.setDriver('GV1', 0)

        # self.http = urllib3.PoolManager()

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            LOGGER.debug('shortPoll (node)')
            self.reportDrivers()

    def cmd_on(self, command):
        json_data = {
            'value': '1',
        }

        response = requests.put(
            'http://localhost/api/' + self.id1 + '/set', data=json_data)

        # self.setDriver('GV1', 1)

    def cmd_off(self, command):

        json_data = {
            'value': '0',
        }

        response = requests.put(
            'http://localhost/api/' + self.id1 + '/set', data=json_data)

        # self.setDriver('GV1', 0)

    def query(self, command=None):
        self.reportDrivers()
        self.start()

    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 25, 'name': 'Online'},
        {'driver': 'GV1', 'value': 0, 'uom': 25, 'name': 'Enabled'}
    ]

    id = 'switchnodeid'

    commands = {
        'DON': cmd_on,
        'DOF': cmd_off,
        'QUERY': query
    }
