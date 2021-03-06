import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import WaterHeaterHeatPumpWrappedCondenser

log = logging.getLogger(__name__)

class TestWaterHeaterHeatPumpWrappedCondenser(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterheaterheatpumpwrappedcondenser(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterHeaterHeatPumpWrappedCondenser()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_compressor_setpoint_temperature_schedule_name = "object-list|Compressor Setpoint Temperature Schedule Name"
        obj.compressor_setpoint_temperature_schedule_name = var_compressor_setpoint_temperature_schedule_name
        # real
        var_dead_band_temperature_difference = 10.00005
        obj.dead_band_temperature_difference = var_dead_band_temperature_difference
        # real
        var_condenser_bottom_location = 0.0
        obj.condenser_bottom_location = var_condenser_bottom_location
        # real
        var_condenser_top_location = 0.0
        obj.condenser_top_location = var_condenser_top_location
        # real
        var_evaporator_air_flow_rate = 0.0001
        obj.evaporator_air_flow_rate = var_evaporator_air_flow_rate
        # alpha
        var_inlet_air_configuration = "Schedule"
        obj.inlet_air_configuration = var_inlet_air_configuration
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_outdoor_air_node_name = "node|Outdoor Air Node Name"
        obj.outdoor_air_node_name = var_outdoor_air_node_name
        # node
        var_exhaust_air_node_name = "node|Exhaust Air Node Name"
        obj.exhaust_air_node_name = var_exhaust_air_node_name
        # object-list
        var_inlet_air_temperature_schedule_name = "object-list|Inlet Air Temperature Schedule Name"
        obj.inlet_air_temperature_schedule_name = var_inlet_air_temperature_schedule_name
        # object-list
        var_inlet_air_humidity_schedule_name = "object-list|Inlet Air Humidity Schedule Name"
        obj.inlet_air_humidity_schedule_name = var_inlet_air_humidity_schedule_name
        # object-list
        var_inlet_air_zone_name = "object-list|Inlet Air Zone Name"
        obj.inlet_air_zone_name = var_inlet_air_zone_name
        # alpha
        var_tank_object_type = "WaterHeater:Stratified"
        obj.tank_object_type = var_tank_object_type
        # object-list
        var_tank_name = "object-list|Tank Name"
        obj.tank_name = var_tank_name
        # node
        var_tank_use_side_inlet_node_name = "node|Tank Use Side Inlet Node Name"
        obj.tank_use_side_inlet_node_name = var_tank_use_side_inlet_node_name
        # node
        var_tank_use_side_outlet_node_name = "node|Tank Use Side Outlet Node Name"
        obj.tank_use_side_outlet_node_name = var_tank_use_side_outlet_node_name
        # alpha
        var_dx_coil_object_type = "Coil:WaterHeating:AirToWaterHeatPump:Wrapped"
        obj.dx_coil_object_type = var_dx_coil_object_type
        # object-list
        var_dx_coil_name = "object-list|DX Coil Name"
        obj.dx_coil_name = var_dx_coil_name
        # real
        var_minimum_inlet_air_temperature_for_compressor_operation = -5.0
        obj.minimum_inlet_air_temperature_for_compressor_operation = var_minimum_inlet_air_temperature_for_compressor_operation
        # real
        var_maximum_inlet_air_temperature_for_compressor_operation = 60.0
        obj.maximum_inlet_air_temperature_for_compressor_operation = var_maximum_inlet_air_temperature_for_compressor_operation
        # alpha
        var_compressor_location = "Schedule"
        obj.compressor_location = var_compressor_location
        # object-list
        var_compressor_ambient_temperature_schedule_name = "object-list|Compressor Ambient Temperature Schedule Name"
        obj.compressor_ambient_temperature_schedule_name = var_compressor_ambient_temperature_schedule_name
        # alpha
        var_fan_object_type = "Fan:OnOff"
        obj.fan_object_type = var_fan_object_type
        # object-list
        var_fan_name = "object-list|Fan Name"
        obj.fan_name = var_fan_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # real
        var_on_cycle_parasitic_electric_load = 0.0
        obj.on_cycle_parasitic_electric_load = var_on_cycle_parasitic_electric_load
        # real
        var_off_cycle_parasitic_electric_load = 0.0
        obj.off_cycle_parasitic_electric_load = var_off_cycle_parasitic_electric_load
        # alpha
        var_parasitic_heat_rejection_location = "Zone"
        obj.parasitic_heat_rejection_location = var_parasitic_heat_rejection_location
        # node
        var_inlet_air_mixer_node_name = "node|Inlet Air Mixer Node Name"
        obj.inlet_air_mixer_node_name = var_inlet_air_mixer_node_name
        # node
        var_outlet_air_splitter_node_name = "node|Outlet Air Splitter Node Name"
        obj.outlet_air_splitter_node_name = var_outlet_air_splitter_node_name
        # object-list
        var_inlet_air_mixer_schedule_name = "object-list|Inlet Air Mixer Schedule Name"
        obj.inlet_air_mixer_schedule_name = var_inlet_air_mixer_schedule_name
        # alpha
        var_tank_element_control_logic = "MutuallyExlcusive"
        obj.tank_element_control_logic = var_tank_element_control_logic
        # real
        var_control_sensor_1_height_in_stratified_tank = 0.0
        obj.control_sensor_1_height_in_stratified_tank = var_control_sensor_1_height_in_stratified_tank
        # real
        var_control_sensor_1_weight = 0.5
        obj.control_sensor_1_weight = var_control_sensor_1_weight
        # real
        var_control_sensor_2_height_in_stratified_tank = 0.0
        obj.control_sensor_2_height_in_stratified_tank = var_control_sensor_2_height_in_stratified_tank

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].name, var_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].compressor_setpoint_temperature_schedule_name, var_compressor_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].dead_band_temperature_difference, var_dead_band_temperature_difference)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].condenser_bottom_location, var_condenser_bottom_location)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].condenser_top_location, var_condenser_top_location)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].evaporator_air_flow_rate, var_evaporator_air_flow_rate)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_configuration, var_inlet_air_configuration)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].outdoor_air_node_name, var_outdoor_air_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].exhaust_air_node_name, var_exhaust_air_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_temperature_schedule_name, var_inlet_air_temperature_schedule_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_humidity_schedule_name, var_inlet_air_humidity_schedule_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_zone_name, var_inlet_air_zone_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].tank_object_type, var_tank_object_type)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].tank_name, var_tank_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].tank_use_side_inlet_node_name, var_tank_use_side_inlet_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].tank_use_side_outlet_node_name, var_tank_use_side_outlet_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].dx_coil_object_type, var_dx_coil_object_type)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].dx_coil_name, var_dx_coil_name)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].minimum_inlet_air_temperature_for_compressor_operation, var_minimum_inlet_air_temperature_for_compressor_operation)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].maximum_inlet_air_temperature_for_compressor_operation, var_maximum_inlet_air_temperature_for_compressor_operation)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].compressor_location, var_compressor_location)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].compressor_ambient_temperature_schedule_name, var_compressor_ambient_temperature_schedule_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].fan_object_type, var_fan_object_type)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].fan_name, var_fan_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].fan_placement, var_fan_placement)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].on_cycle_parasitic_electric_load, var_on_cycle_parasitic_electric_load)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].off_cycle_parasitic_electric_load, var_off_cycle_parasitic_electric_load)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].parasitic_heat_rejection_location, var_parasitic_heat_rejection_location)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_mixer_node_name, var_inlet_air_mixer_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].outlet_air_splitter_node_name, var_outlet_air_splitter_node_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].inlet_air_mixer_schedule_name, var_inlet_air_mixer_schedule_name)
        self.assertEqual(idf2.waterheaterheatpumpwrappedcondensers[0].tank_element_control_logic, var_tank_element_control_logic)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].control_sensor_1_height_in_stratified_tank, var_control_sensor_1_height_in_stratified_tank)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].control_sensor_1_weight, var_control_sensor_1_weight)
        self.assertAlmostEqual(idf2.waterheaterheatpumpwrappedcondensers[0].control_sensor_2_height_in_stratified_tank, var_control_sensor_2_height_in_stratified_tank)