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
        self.allData = requests.get(
            url='{}/api/status'.format(self.apiBaseUrl))

        if self.allData.status_code == 200:
            self.setDriver('ST', 1)
        else:
            self.setDriver('ST', 0)

        self.allDataJson = self.allData.json()
        # LOGGER.info(self.allDataJson)

        LOGGER.info("Pool Running  {}".format(
            self.allDataJson["leds"]["Filter_Pump"]))

        isON = self.allDataJson["leds"]["Filter_Pump"]
        LOGGER.info(isON)
        if isON == 'on':
            self.setDriver('GV0', 1)
        if isON == 'off':
            self.setDriver('GV0', 0)

        LOGGER.info("Air Temp  {}".format(self.allDataJson["air_temp"]))
        self.setDriver('GV1', self.allDataJson["air_temp"])

        LOGGER.info("Freeze Setpoint  {}".format(
            self.allDataJson["frz_protect_set_pnt"]))
        self.setDriver(
            'GV2', self.allDataJson["frz_protect_set_pnt"])

        LOGGER.info("Pool Temp  {}".format(
            self.allDataJson["pool_temp"]))
        self.setDriver('GV3', self.allDataJson["pool_temp"])

        LOGGER.info("Pump Status  {}".format(
            self.allDataJson["leds"]["Filter_Pump"]))
        pisOn = self.allDataJson["leds"]["Filter_Pump"]
        if pisOn == 'on':
            self.setDriver('GV4', 1)
        if pisOn == 'off':
            self.setDriver('GV4', 0)

        LOGGER.info("Pump Watts  {}".format(
            self.allDataJson["Pump_1"]["Watts"]))
        self.setDriver('GV5', self.allDataJson["Pump_1"]["Watts"])

        LOGGER.info("Pump RPM  {}".format(
            self.allDataJson["Pump_1"]["RPM"]))
        self.setDriver('GV6', self.allDataJson["Pump_1"]["RPM"])

        LOGGER.info("Pump GPM  {}".format(
            self.allDataJson["Pump_1"]["GPM"]))
        self.setDriver('GV7', self.allDataJson["Pump_1"]["GPM"])

        LOGGER.info("Salt Water Gen  {}".format(
            self.allDataJson["leds"]["SWG"]))
        self.setDriver('GV8', self.allDataJson["leds"]["SWG"])
        
        LOGGER.info("Salt Water Boost  {}".format(
            self.allDataJson["leds"]["SWG/Boost"]))
        self.setDriver('GV9', self.allDataJson["leds"]["SWG/Boost"])
        
        LOGGER.info("Pool Heat Setpoint  {}".format(
            self.allDataJson["pool_htr_set_pnt"]))
        self.setDriver('GV10', self.allDataJson["pool_htr_set_pnt"])
        
        LOGGER.info("SPA Heat Setpoint  {}".format(
            self.allDataJson["spa_htr_set_pnt"]))
        self.setDriver('GV11', self.allDataJson["spa_htr_set_pnt"])
        
        LOGGER.info("Solar Heat  {}".format(
            self.allDataJson["leds"]["Solar_Heater"]))
        pisOn = self.allDataJson["leds"]["Solar_Heater"]
        if pisOn == 'on':
            self.setDriver('GV12', 1)
        if pisOn == 'off':
            self.setDriver('GV12', 0)
            
        LOGGER.info("SPA Heat  {}".format(
            self.allDataJson["leds"]["Spa_Heater"]))
        pisOn = self.allDataJson["leds"]["Spa_Heater"]
        if pisOn == 'on':
            self.setDriver('GV13', 1)
        if pisOn == 'off':
            self.setDriver('GV13', 0)
            
        LOGGER.info("SPA Mode  {}".format(
            self.allDataJson["leds"]["Spa_Mode"]))
        pisOn = self.allDataJson["leds"]["Spa_Mode"]
        if pisOn == 'on':
            self.setDriver('GV14', 1)
        if pisOn == 'off':
            self.setDriver('GV14', 0)
        
        
        
        
        
        
        
        
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
        json_data = {"id": 6, "state": True}  # True-Start False-Stop

        response = requests.put(
            self.api_url + '/state/circuit/setState', json=json_data)

    def cmd_off(self, command):
        json_data = {"id": 6, "state": False}  # True-Start False-Stop

        response = requests.put(
            self.api_url + '/state/circuit/setState', json=json_data)

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
        
        
        
        {'driver': 'CLISPH', 'value': 45, 'uom': 17, 'name': "Setpoint adj"},
        {'driver': 'ST', 'value': 0, 'uom': 25, 'name': "Online"},
    ]

    id = 'poolnode'

    commands = {
        'DON': cmd_on,
        'DOF': cmd_off,
        'SET_TEMP': cmd_set_temp,
        'QUERY': query
    }
