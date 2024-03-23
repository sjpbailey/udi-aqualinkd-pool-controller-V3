''' Pool Body
    copyright© 2024 SJBailey© '''
import udi_interface
import sys
import time
import requests
import urllib3

LOGGER = udi_interface.LOGGER


class PoolNode(udi_interface.Node):

    def __init__(self, polyglot, primary, address, name, allData, apiBaseUrl, api_url):

        super(PoolNode, self).__init__(polyglot, primary, address, name)
        self.poly = polyglot
        self.lpfx = '%s:%s' % (address, name)

        self.poly.subscribe(self.poly.START, self.start, address)
        self.poly.subscribe(self.poly.POLL, self.poll)

        self.allData = allData
        self.apiBaseUrl = apiBaseUrl
        self.api_url = api_url

    def start(self):
        ##### GET Status ####
        self.allData = requests.get(
            url='{}/api/status'.format(self.apiBaseUrl))

        if self.allData.status_code == 200:
            self.setDriver('ST', 1)
        else:
            self.setDriver('ST', 0)

        self.allStatusJson = self.allData.json()
        # LOGGER.info(self.allStatusJson)

        LOGGER.info("Pool Running  {}".format(
            self.allStatusJson["leds"]["Filter_Pump"]))

        isON = self.allStatusJson["leds"]["Filter_Pump"]
        LOGGER.info(isON)
        if isON == 'on':
            self.setDriver('GV0', 1)
        if isON == 'off':
            self.setDriver('GV0', 0)

        LOGGER.info("Air Temp  {}".format(self.allStatusJson["air_temp"]))
        self.setDriver('GV1', self.allStatusJson["air_temp"])

        LOGGER.info("Freeze Setpoint  {}".format(
            self.allStatusJson["frz_protect_set_pnt"]))
        self.setDriver(
            'GV2', self.allStatusJson["frz_protect_set_pnt"])

        LOGGER.info("Pool Temp  {}".format(
            self.allStatusJson["pool_temp"]))
        self.setDriver('GV3', self.allStatusJson["pool_temp"])

        LOGGER.info("Pump Status  {}".format(
            self.allStatusJson["leds"]["Filter_Pump"]))
        pisOn = self.allStatusJson["leds"]["Filter_Pump"]
        if pisOn == 'on':
            self.setDriver('GV4', 1)
        if pisOn == 'off':
            self.setDriver('GV4', 0)

        LOGGER.info("Pump Watts  {}".format(
            self.allStatusJson["Pump_1"]["Watts"]))
        self.setDriver('GV5', self.allStatusJson["Pump_1"]["Watts"])

        LOGGER.info("Pump RPM  {}".format(
            self.allStatusJson["Pump_1"]["RPM"]))
        self.setDriver('GV6', self.allStatusJson["Pump_1"]["RPM"])

        LOGGER.info("Pump GPM  {}".format(
            self.allStatusJson["Pump_1"]["GPM"]))
        self.setDriver('GV7', self.allStatusJson["Pump_1"]["GPM"])

        LOGGER.info("Salt Water Gen  {}".format(
            self.allStatusJson["swg_percent"]))
        self.setDriver('GV8', self.allStatusJson["swg_percent"])

        LOGGER.info("Salt Water Boost  {}".format(
            self.allStatusJson["swg_ppm"]))
        self.setDriver('GV9', self.allStatusJson["swg_ppm"])

        LOGGER.info("Pool Heat Setpoint  {}".format(
            self.allStatusJson["pool_htr_set_pnt"]))
        self.setDriver('GV10', self.allStatusJson["pool_htr_set_pnt"])

        LOGGER.info("SPA Heat Setpoint  {}".format(
            self.allStatusJson["spa_htr_set_pnt"]))
        self.setDriver('GV11', self.allStatusJson["spa_htr_set_pnt"])

        LOGGER.info("Solar Heat  {}".format(
            self.allStatusJson["leds"]["Solar_Heater"]))
        pisOn = self.allStatusJson["leds"]["Solar_Heater"]
        if pisOn == 'on':
            self.setDriver('GV12', 1)
        if pisOn == 'off':
            self.setDriver('GV12', 0)

        LOGGER.info("SPA Heat  {}".format(
            self.allStatusJson["leds"]["Spa_Heater"]))
        pisOn = self.allStatusJson["leds"]["Spa_Heater"]
        if pisOn == 'on':
            self.setDriver('GV13', 1)
        if pisOn == 'off':
            self.setDriver('GV13', 0)

        LOGGER.info("SPA Mode  {}".format(
            self.allStatusJson["leds"]["Spa_Mode"]))
        pisOn = self.allStatusJson["leds"]["Spa_Mode"]
        if pisOn == 'on':
            self.setDriver('GV14', 1)
        if pisOn == 'off':
            self.setDriver('GV14', 0)

# Grab data from a new call to devices to get names

        ##### GET Devices ####
        self.allData = requests.get(
            url='{}/api/devices'.format(self.apiBaseUrl))

        self.allDevicesJson = self.allData.json()

        LOGGER.info("AUX-1 Name {}".format(
            self.allDevicesJson["devices"][2]["name"]))
        self.setDriver('GV22', self.allDevicesJson["devices"][2]["name"])
        LOGGER.info("AUX-1  {}".format(
            self.allDevicesJson["devices"][2]["status"]))
        pisOn = self.allDevicesJson["devices"][2]["status"]
        if pisOn == 'on':
            self.setDriver('GV15', 1)
        if pisOn == 'off':
            self.setDriver('GV15', 0)

        LOGGER.info("AUX-2 Name {}".format(
            self.allDevicesJson["devices"][3]["name"]))

        LOGGER.info("AUX-2  {}".format(
            self.allDevicesJson["devices"][3]["status"]))
        pisOn = self.allDevicesJson["devices"][3]["status"]
        if pisOn == 'on':
            self.setDriver('GV16', 1)
        if pisOn == 'off':
            self.setDriver('GV16', 0)

        LOGGER.info("AUX-3 Name  {}".format(
            self.allDevicesJson["devices"][4]["name"]))

        LOGGER.info("AUX-3  {}".format(
            self.allDevicesJson["devices"][4]["status"]))
        pisOn = self.allDevicesJson["devices"][4]["status"]
        if pisOn == 'on':
            self.setDriver('GV17', 1)
        if pisOn == 'off':
            self.setDriver('GV17', 0)

        LOGGER.info("AUX-4 Name  {}".format(
            self.allDevicesJson["devices"][5]["name"]))

        LOGGER.info("AUX-4  {}".format(
            self.allDevicesJson["devices"][5]["status"]))
        pisOn = self.allDevicesJson["devices"][5]["status"]
        if pisOn == 'on':
            self.setDriver('GV18', 1)
        if pisOn == 'off':
            self.setDriver('GV18', 0)

        LOGGER.info("AUX-5  {}".format(
            self.allDevicesJson["devices"][6]["name"]))

        LOGGER.info("AUX-5  {}".format(
            self.allDevicesJson["devices"][6]["status"]))
        pisOn = self.allDevicesJson["devices"][6]["status"]
        if pisOn == 'on':
            self.setDriver('GV19', 1)
        if pisOn == 'off':
            self.setDriver('GV19', 0)

        LOGGER.info("AUX-6 Name {}".format(
            self.allDevicesJson["devices"][7]["name"]))

        LOGGER.info("AUX-6  {}".format(
            self.allDevicesJson["devices"][7]["status"]))
        pisOn = self.allDevicesJson["devices"][7]["status"]
        if pisOn == 'on':
            self.setDriver('GV20', 1)
        if pisOn == 'off':
            self.setDriver('GV20', 0)

        LOGGER.info("AUX-7 Name  {}".format(
            self.allDevicesJson["devices"][8]["name"]))

        LOGGER.info("AUX-7  {}".format(
            self.allDevicesJson["devices"][8]["status"]))
        pisOn = self.allDevicesJson["devices"][8]["status"]
        if pisOn == 'on':
            self.setDriver('GV21', 1)
        if pisOn == 'off':
            self.setDriver('GV21', 0)

        self.http = urllib3.PoolManager()

    def poll(self, polltype):
        if 'longPoll' in polltype:
            LOGGER.debug('longPoll (node)')
        else:
            LOGGER.debug('shortPoll (node)')
            self.start()
            self.query()

            LOGGER.debug('%s: get ST=%s', self.lpfx, self.getDriver('ST'))

    def cmd_on(self, command):
        json_data = {'value': '1', }

        response = requests.put(
            self.api_url + '/api/Filter_Pump/set', data=json_data)

    def cmd_off(self, command):
        json_data = {'value': '0', }

        response = requests.put(
            self.api_url + '/api/Filter_Pump/set', data=json_data)

    def query(self, command=None):
        self.reportDrivers()

    def cmd_set_temp(self, command):
        value = int(command.get('value'))
        json_data = {
            "id": 1,
            # "name": "Pool",
            "heatSetpoint": value,
        }

        response = requests.put(
            self.api_url + '/state/body/setPoint', json=json_data)

    '''def cmd_set_sped(self, command):
        value = int(command.get('value'))
        json_data = {"id": 50, "circuits": [
            {"speed": value, "units": {"val": 0}, "id": 1, "circuit": 6}]}

        response = requests.put(
            self.api_url + '/config/pump', json=json_data)'''

    drivers = [
        {'driver': 'GV0', 'value': 0, 'uom': 25, 'name': "Pool Running"},
        {'driver': 'GV1', 'value': None, 'uom': 17, 'name': "Air Temp"},
        {'driver': 'GV2', 'value': None, 'uom': 17, 'name': "Freeze Setpoint"},
        {'driver': 'GV3', 'value': None, 'uom': 17, 'name': "Pool Temp"},
        {'driver': 'GV4', 'value': None, 'uom': 25, 'name': "Pump Status"},
        {'driver': 'GV5', 'value': None, 'uom': 73, 'name': "Pump Watts"},
        {'driver': 'GV6', 'value': None, 'uom': 89, 'name': "Pump RPM"},
        {'driver': 'GV7', 'value': None, 'uom': 69, 'name': "Pump GPM"},
        {'driver': 'GV8', 'value': None, 'uom': 52, 'name': "SWG"},
        {'driver': 'GV9', 'value': None, 'uom': 54, 'name': "SWG/Boost"},
        {'driver': 'GV10', 'value': None, 'uom': 17, 'name': "Pool Setpoint"},
        {'driver': 'GV11', 'value': None, 'uom': 17, 'name': "Spa Setpoint"},
        {'driver': 'GV12', 'value': None, 'uom': 25, 'name': "Solar Heat"},
        {'driver': 'GV13', 'value': None, 'uom': 25, 'name': "SPA Heat"},
        {'driver': 'GV14', 'value': None, 'uom': 25, 'name': "SPA Mode"},
        {'driver': 'GV15', 'value': None, 'uom': 25, 'name': "Aux-1"},
        {'driver': 'GV16', 'value': None, 'uom': 25, 'name': "Aux-2"},
        {'driver': 'GV17', 'value': None, 'uom': 25, 'name': "Aux-3"},
        {'driver': 'GV18', 'value': None, 'uom': 25, 'name': "Aux-4"},
        {'driver': 'GV19', 'value': None, 'uom': 25, 'name': "Aux-5"},
        {'driver': 'GV20', 'value': None, 'uom': 25, 'name': "Aux-6"},
        {'driver': 'GV21', 'value': None, 'uom': 25, 'name': "Aux-7"},
        {'driver': 'CLISPH', 'value': 45, 'uom': 17, 'name': "Setpoint adj"},
        {'driver': 'GV22', 'value': None, 'uom': 56, 'name': "Aux-1 Name"},
        {'driver': 'ST', 'value': 0, 'uom': 25, 'name': "Online"},
    ]

    id = 'poolnode'

    commands = {
        'DON': cmd_on,
        'DOF': cmd_off,
        'SET_TEMP': cmd_set_temp,
        'QUERY': query
    }
