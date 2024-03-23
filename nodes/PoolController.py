'''copyright© 2024 SJBailey©'''
import udi_interface
import requests
import logging
import json

# My Template Node
from nodes import PoolNode
from nodes import SwitchNode
from nodes import PumpNode
from nodes import PumpIVSNode
from nodes import PumpIVFNode
from nodes import PumpISVSNode
from nodes import Pump2SPDNode
from nodes import Pump1SPDNode
from nodes import PumpTriStarNode
from nodes import PumpHSVSNode
from nodes import TemplateNode

LOGGER = udi_interface.LOGGER
LOG_HANDLER = udi_interface.LOG_HANDLER
Custom = udi_interface.Custom
ISY = udi_interface.ISY

# IF you want a different log format than the current default
LOG_HANDLER.set_log_format(
    '%(asctime)s %(threadName)-10s %(name)-18s %(levelname)-8s %(module)s:%(funcName)s: %(message)s')


class PoolController(udi_interface.Node):

    def __init__(self, polyglot, primary, address, name):

        super(PoolController, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.name = 'Pool Controller'  # override what was passed in
        self.hb = 0

        self.Parameters = Custom(polyglot, 'customparams')
        self.Notices = Custom(polyglot, 'notices')
        self.TypedParameters = Custom(polyglot, 'customtypedparams')
        self.TypedData = Custom(polyglot, 'customtypeddata')

        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.CUSTOMPARAMS, self.parameterHandler)
        self.poly.subscribe(self.poly.POLL, self.poll)
        self.poly.ready()
        self.poly.addNode(self)

    def start(self):
        self.poly.updateProfile()
        self.poly.setCustomParamsDoc()
        self.discover()

    def parameterHandler(self, params):
        self.Parameters.load(params)
        LOGGER.debug('Loading parameters now')
        self.check_params()

    def poll(self, flag):
        if 'longPoll' in flag:
            LOGGER.debug('longPoll (controller)')
        else:
            LOGGER.debug('shortPoll (controller)')
            self.reportDrivers()

    def query(self, command=None):
        nodes = self.poly.getNodes()
        for node in nodes:
            nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        LOGGER.info('Starting Pool Controller')

        if self.api_url:
            self.apiBaseUrl = self.api_url
            # Get all data from nodejs pool controller api
            allData = requests.get(
                url='{}/api/status'.format(self.apiBaseUrl))

            if allData.status_code == 200:
                self.setDriver('ST', 1)
            else:
                self.setDriver('ST', 0)

            self.allDataJson = allData.json()
            # LOGGER.info(self.allDataJson)

            # self.poly.addNode(PoolNode(self.poly, self.address, 'pooladdr', 'Status',
            #                           allData, self.apiBaseUrl, self.api_url))
            LOGGER.info("Statuses Installed")
            self.go()

    def go(self):
        ##### GET Devices ####
        # Get all data from nodejs pool controller api
        self.allData = requests.get(url='{}/api/devices'.format(self.api_url))
        self.allDevicesJson = self.allData.json()

        for i in self.allDevicesJson["devices"]:
            try:
                if i["type_ext"] == "switch_program" or "switch_timer":
                    name = i["name"]
                    id = i["id"]
                    state = i["state"]
                    status1 = i["status"]
                    address = '{}'.format(id)
                    LOGGER.info("Switch_EXT")
                    LOGGER.info(print("ID: {}".format(i["id"])))
                    LOGGER.info("Status int: {}".format(i["int_status"]))
                    LOGGER.info(print("Name: {}".format(i["name"])))
                    LOGGER.info(print("State: {}".format(i["state"])))
                    LOGGER.info(print("Status: {}".format(i["status"])))
                    LOGGER.info("Type External: {}".format(i["type_ext"]))

                    # self.poly.addNode(TemplateNode(
                    #    self.poly, self.address, address, name))  # state, status1, self.apiBaseUrl, self.api_url))

                    self.poly.addNode(SwitchNode(
                        self.poly, self.address, address, name, state, status1, self.apiBaseUrl, self.api_url))
                    # LOGGER.info('Found {} Circuits'.format(len(self.circuits)))
                    LOGGER.info("Auxillary Installation Complete")

            except KeyError:
                LOGGER.info(f"Item not found! ")

    def delete(self):
        LOGGER.info('Being deleted')

    def stop(self):
        LOGGER.debug('NodeServer stopped.')

    def set_module_logs(self, level):
        logging.getLogger('urllib3').setLevel(level)

    def check_params(self):
        self.Notices.clear()
        default_api_url = "http://localhost:80"

        self.api_url = self.Parameters.api_url
        if self.api_url is None:
            self.api_url = default_api_url
            LOGGER.error(
                'check_params: user not defined in customParams, please add it.  Using {}'.format(default_api_url))
            self.api_url = default_api_url

        # Add a notice if they need to change the user/circuits from the default.
        if self.api_url == default_api_url:
            self.Notices['auth'] = 'Please set proper api_url and circuits in configuration page'

    id = 'controller'
    commands = {
        'QUERY': query,

    }
    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 25, 'name': "Online"},
        # {'driver': 'GV0', 'value': 0, 'uom': 17, 'name': "Air Temp"},
    ]
