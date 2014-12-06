import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_templates import HvactemplateZoneVav

log = logging.getLogger(__name__)

class TestHvactemplateZoneVav(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_hvactemplatezonevav(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HvactemplateZoneVav()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_template_vav_system_name = "object-list|Template VAV System Name"
        obj.template_vav_system_name = var_template_vav_system_name
        # object-list
        var_template_thermostat_name = "object-list|Template Thermostat Name"
        obj.template_thermostat_name = var_template_thermostat_name
        # real
        var_supply_air_maximum_flow_rate = 4.4
        obj.supply_air_maximum_flow_rate = var_supply_air_maximum_flow_rate
        # real
        var_zone_heating_sizing_factor = 0.0
        obj.zone_heating_sizing_factor = var_zone_heating_sizing_factor
        # real
        var_zone_cooling_sizing_factor = 0.0
        obj.zone_cooling_sizing_factor = var_zone_cooling_sizing_factor
        # alpha
        var_zone_minimum_air_flow_input_method = "Constant"
        obj.zone_minimum_air_flow_input_method = var_zone_minimum_air_flow_input_method
        # real
        var_constant_minimum_air_flow_fraction = 0.5
        obj.constant_minimum_air_flow_fraction = var_constant_minimum_air_flow_fraction
        # real
        var_fixed_minimum_air_flow_rate = 9.9
        obj.fixed_minimum_air_flow_rate = var_fixed_minimum_air_flow_rate
        # object-list
        var_minimum_air_flow_fraction_schedule_name = "object-list|Minimum Air Flow Fraction Schedule Name"
        obj.minimum_air_flow_fraction_schedule_name = var_minimum_air_flow_fraction_schedule_name
        # alpha
        var_outdoor_air_method = "Flow/Person"
        obj.outdoor_air_method = var_outdoor_air_method
        # real
        var_outdoor_air_flow_rate_per_person = 12.12
        obj.outdoor_air_flow_rate_per_person = var_outdoor_air_flow_rate_per_person
        # real
        var_outdoor_air_flow_rate_per_zone_floor_area = 13.13
        obj.outdoor_air_flow_rate_per_zone_floor_area = var_outdoor_air_flow_rate_per_zone_floor_area
        # real
        var_outdoor_air_flow_rate_per_zone = 14.14
        obj.outdoor_air_flow_rate_per_zone = var_outdoor_air_flow_rate_per_zone
        # alpha
        var_reheat_coil_type = "HotWater"
        obj.reheat_coil_type = var_reheat_coil_type
        # object-list
        var_reheat_coil_availability_schedule_name = "object-list|Reheat Coil Availability Schedule Name"
        obj.reheat_coil_availability_schedule_name = var_reheat_coil_availability_schedule_name
        # alpha
        var_damper_heating_action = "Normal"
        obj.damper_heating_action = var_damper_heating_action
        # real
        var_maximum_flow_per_zone_floor_area_during_reheat = 18.18
        obj.maximum_flow_per_zone_floor_area_during_reheat = var_maximum_flow_per_zone_floor_area_during_reheat
        # real
        var_maximum_flow_fraction_during_reheat = 19.19
        obj.maximum_flow_fraction_during_reheat = var_maximum_flow_fraction_during_reheat
        # real
        var_maximum_reheat_air_temperature = 0.0001
        obj.maximum_reheat_air_temperature = var_maximum_reheat_air_temperature
        # object-list
        var_design_specification_outdoor_air_object_name_for_control = "object-list|Design Specification Outdoor Air Object Name for Control"
        obj.design_specification_outdoor_air_object_name_for_control = var_design_specification_outdoor_air_object_name_for_control
        # object-list
        var_supply_plenum_name = "object-list|Supply Plenum Name"
        obj.supply_plenum_name = var_supply_plenum_name
        # object-list
        var_return_plenum_name = "object-list|Return Plenum Name"
        obj.return_plenum_name = var_return_plenum_name
        # alpha
        var_baseboard_heating_type = "HotWater"
        obj.baseboard_heating_type = var_baseboard_heating_type
        # object-list
        var_baseboard_heating_availability_schedule_name = "object-list|Baseboard Heating Availability Schedule Name"
        obj.baseboard_heating_availability_schedule_name = var_baseboard_heating_availability_schedule_name
        # real
        var_baseboard_heating_capacity = 26.26
        obj.baseboard_heating_capacity = var_baseboard_heating_capacity
        # alpha
        var_zone_cooling_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_cooling_design_supply_air_temperature_input_method = var_zone_cooling_design_supply_air_temperature_input_method
        # real
        var_zone_cooling_design_supply_air_temperature = 28.28
        obj.zone_cooling_design_supply_air_temperature = var_zone_cooling_design_supply_air_temperature
        # real
        var_zone_cooling_design_supply_air_temperature_difference = 29.29
        obj.zone_cooling_design_supply_air_temperature_difference = var_zone_cooling_design_supply_air_temperature_difference
        # alpha
        var_zone_heating_design_supply_air_temperature_input_method = "SupplyAirTemperature"
        obj.zone_heating_design_supply_air_temperature_input_method = var_zone_heating_design_supply_air_temperature_input_method
        # real
        var_zone_heating_design_supply_air_temperature = 31.31
        obj.zone_heating_design_supply_air_temperature = var_zone_heating_design_supply_air_temperature
        # real
        var_zone_heating_design_supply_air_temperature_difference = 32.32
        obj.zone_heating_design_supply_air_temperature_difference = var_zone_heating_design_supply_air_temperature_difference
        # object-list
        var_design_specification_outdoor_air_object_name_for_sizing = "object-list|Design Specification Outdoor Air Object Name for Sizing"
        obj.design_specification_outdoor_air_object_name_for_sizing = var_design_specification_outdoor_air_object_name_for_sizing
        # object-list
        var_design_specification_zone_air_distribution_object_name = "object-list|Design Specification Zone Air Distribution Object Name"
        obj.design_specification_zone_air_distribution_object_name = var_design_specification_zone_air_distribution_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.hvactemplatezonevavs[0].zone_name, var_zone_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].template_vav_system_name, var_template_vav_system_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].template_thermostat_name, var_template_thermostat_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].supply_air_maximum_flow_rate, var_supply_air_maximum_flow_rate)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_heating_sizing_factor, var_zone_heating_sizing_factor)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_cooling_sizing_factor, var_zone_cooling_sizing_factor)
        self.assertEqual(idf2.hvactemplatezonevavs[0].zone_minimum_air_flow_input_method, var_zone_minimum_air_flow_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].constant_minimum_air_flow_fraction, var_constant_minimum_air_flow_fraction)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].fixed_minimum_air_flow_rate, var_fixed_minimum_air_flow_rate)
        self.assertEqual(idf2.hvactemplatezonevavs[0].minimum_air_flow_fraction_schedule_name, var_minimum_air_flow_fraction_schedule_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].outdoor_air_method, var_outdoor_air_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].outdoor_air_flow_rate_per_person, var_outdoor_air_flow_rate_per_person)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].outdoor_air_flow_rate_per_zone_floor_area, var_outdoor_air_flow_rate_per_zone_floor_area)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].outdoor_air_flow_rate_per_zone, var_outdoor_air_flow_rate_per_zone)
        self.assertEqual(idf2.hvactemplatezonevavs[0].reheat_coil_type, var_reheat_coil_type)
        self.assertEqual(idf2.hvactemplatezonevavs[0].reheat_coil_availability_schedule_name, var_reheat_coil_availability_schedule_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].damper_heating_action, var_damper_heating_action)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].maximum_flow_per_zone_floor_area_during_reheat, var_maximum_flow_per_zone_floor_area_during_reheat)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].maximum_flow_fraction_during_reheat, var_maximum_flow_fraction_during_reheat)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].maximum_reheat_air_temperature, var_maximum_reheat_air_temperature)
        self.assertEqual(idf2.hvactemplatezonevavs[0].design_specification_outdoor_air_object_name_for_control, var_design_specification_outdoor_air_object_name_for_control)
        self.assertEqual(idf2.hvactemplatezonevavs[0].supply_plenum_name, var_supply_plenum_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].return_plenum_name, var_return_plenum_name)
        self.assertEqual(idf2.hvactemplatezonevavs[0].baseboard_heating_type, var_baseboard_heating_type)
        self.assertEqual(idf2.hvactemplatezonevavs[0].baseboard_heating_availability_schedule_name, var_baseboard_heating_availability_schedule_name)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].baseboard_heating_capacity, var_baseboard_heating_capacity)
        self.assertEqual(idf2.hvactemplatezonevavs[0].zone_cooling_design_supply_air_temperature_input_method, var_zone_cooling_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_cooling_design_supply_air_temperature, var_zone_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_cooling_design_supply_air_temperature_difference, var_zone_cooling_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevavs[0].zone_heating_design_supply_air_temperature_input_method, var_zone_heating_design_supply_air_temperature_input_method)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_heating_design_supply_air_temperature, var_zone_heating_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.hvactemplatezonevavs[0].zone_heating_design_supply_air_temperature_difference, var_zone_heating_design_supply_air_temperature_difference)
        self.assertEqual(idf2.hvactemplatezonevavs[0].design_specification_outdoor_air_object_name_for_sizing, var_design_specification_outdoor_air_object_name_for_sizing)
        self.assertEqual(idf2.hvactemplatezonevavs[0].design_specification_zone_air_distribution_object_name, var_design_specification_zone_air_distribution_object_name)