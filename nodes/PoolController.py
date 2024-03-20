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
            self.query()

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

            self.poly.addNode(PoolNode(self.poly, self.address, 'pooladdr',
                              'Status', allData, self.apiBaseUrl, self.api_url))
        else:
            pass

            # LOGGER.info("Air Temp  {}".format(self.allDataJson["air_temp"]))
            # self.setDriver('GV0', self.allDataJson["air_temp"])

        # Grab data from a new call to devices to get names

        ##### GET Devices ####
        if self.api_url:
            self.apiBaseUrl = self.api_url
            # Get all data from nodejs pool controller api
            self.allData = requests.get(
                url='{}/api/devices'.format(self.apiBaseUrl))

            self.allDevicesJson = self.allData.json()

            for i in self.allDevicesJson["devices"]:
                try:
                    if i["type_ext"] == "switch_program" or "switch_timer":
                        LOGGER.info("Switch_EXT")
                        LOGGER.info(print("ID: {}".format(i["id"])))
                        id = i["id"]
                        LOGGER.info("Status int: {}".format(i["int_status"]))
                        LOGGER.info(print("Name: {}".format(i["name"])))
                        name = i["name"]
                        LOGGER.info(print("State: {}".format(i["state"])))
                        state = i["state"]
                        LOGGER.info(print("Status: {}".format(i["status"])))
                        status1 = i["status"]
                        LOGGER.info("Type External: {}".format(i["type_ext"]))
                        address = 'zone_{}'.format(id)

                        self.poly.addNode(SwitchNode(
                            self.poly, self.address, address, name, state, status1))
                    # LOGGER.info('Found {} Circuits'.format(len(self.circuits)))
                    LOGGER.info("Auxillary Installation Complete")

                except KeyError:
                    LOGGER.info(f"Item not found! ")

        '''for i in self.allDataJson["circuits"]:
            name = i["name"]
            id = i["id"]
            # isOn = i["isOn"]
            LOGGER.info(i["name"])  # , i["id"], i['isOn'])
            LOGGER.info(i["id"])
            # LOGGER.info(i["isOn"])
            self.allDataJson = self.allDataJson
            address = 'zone_{}'.format(id)
            LOGGER.info(address)
            self.poly.addNode(SwitchNode(
                self.poly, self.address, address, name, self.apiBaseUrl, self.api_url))
            # LOGGER.info('Found {} Circuits'.format(len(self.circuits)))
            LOGGER.info("Circuit Installation Complete")
        else:
            LOGGER.info("Circuit Not Found")

        for i in self.allDataJson["pumps"]:
            self.allDataJson = self.allDataJson
            self.api_url = self.api_url
            name = i["name"]
            LOGGER.info(i["name"])
            address = i["address"]
            LOGGER.info(i["address"])
            LOGGER.info(i["type"]['desc'])
            address = 'pump_{}'.format(address)
            LOGGER.info("ID:  {}".format(i["id"]))
            pid = i["id"]
            if i["type"]['desc'] == "Intelliflo VSF":
                LOGGER.info("Install Intelliflo VSF")
                self.poly.addNode(PumpNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Intelliflo VS":
                LOGGER.info("Install Intelliflo VS")
                self.poly.addNode(PumpIVSNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Intelliflo VF":
                LOGGER.info("Install Intelliflo VF")
                self.poly.addNode(PumpIVFNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "SuperFlo VS":
                LOGGER.info("Install SuperFlo VS")
                self.poly.addNode(PumpISVSNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Two Speed":
                LOGGER.info("Install Two Speed")
                self.poly.addNode(Pump2SPDNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Single Speed":
                LOGGER.info("Install Single Speed")
                self.poly.addNode(Pump1SPDNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Hayward Eco/TriStar VS":
                LOGGER.info("Install Hayward Eco/TriStar VS")
                self.poly.addNode(PumpTriStarNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            elif i["type"]['desc'] == "Hayward Relay VS":
                LOGGER.info("Install Hayward Relay VS")
                self.poly.addNode(PumpHSVSNode(
                    self.poly, self.address, address, name, allData, self.apiBaseUrl, self.api_url, pid))
            else:
                LOGGER.info("Pump Not Found")

        for i in self.allDataJson["heaters"]:
            LOGGER.info(i['name'])
            LOGGER.info(i['id'])
            LOGGER.info(i['type']['desc'])
            LOGGER.info(i['isOn'])
            LOGGER.info("Heater Discovery Complete")

        else:
            LOGGER.info("No Heaters Found")

        for i in self.allDataJson["virtualCircuits"]:
            LOGGER.info(i['name'])
            LOGGER.info(i['id'])
            LOGGER.info(i['isOn'])
            LOGGER.info("Virtual Circuit Discovery Complete")
        else:
            LOGGER.info("No Virtual Circuits Found")'''

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
