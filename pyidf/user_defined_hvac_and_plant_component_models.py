from collections import OrderedDict

class ZoneHvacForcedAirUserDefined(object):
    """ Corresponds to IDD object `ZoneHVAC:ForcedAir:UserDefined`
        Defines a generic zone air unit for custom modeling
        using Energy Management System or External Interface
    """
    internal_name = "ZoneHVAC:ForcedAir:UserDefined"
    field_count = 17

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:ForcedAir:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Overall Model Simulation Program Calling Manager Name"] = None
        self._data["Model Setup and Sizing Program Calling Manager Name"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Secondary Air Outlet Node Name"] = None
        self._data["Number of Plant Loop Connections"] = None
        self._data["Plant Connection 1 Inlet Node Name"] = None
        self._data["Plant Connection 1 Outlet Node Name"] = None
        self._data["Plant Connection 2 Inlet Node Name"] = None
        self._data["Plant Connection 2 Outlet Node Name"] = None
        self._data["Plant Connection 3 Inlet Node Name"] = None
        self._data["Plant Connection 3 Outlet Node Name"] = None
        self._data["Supply Inlet Water Storage Tank Name"] = None
        self._data["Collection Outlet Water Storage Tank Name"] = None
        self._data["Ambient Zone Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.overall_model_simulation_program_calling_manager_name = None
        else:
            self.overall_model_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.model_setup_and_sizing_program_calling_manager_name = None
        else:
            self.model_setup_and_sizing_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_outlet_node_name = None
        else:
            self.secondary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_plant_loop_connections = None
        else:
            self.number_of_plant_loop_connections = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_inlet_node_name = None
        else:
            self.plant_connection_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_outlet_node_name = None
        else:
            self.plant_connection_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_inlet_node_name = None
        else:
            self.plant_connection_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_outlet_node_name = None
        else:
            self.plant_connection_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_inlet_node_name = None
        else:
            self.plant_connection_3_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_outlet_node_name = None
        else:
            self.plant_connection_3_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_inlet_water_storage_tank_name = None
        else:
            self.supply_inlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collection_outlet_water_storage_tank_name = None
        else:
            self.collection_outlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_zone_name = None
        else:
            self.ambient_zone_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the zone unit

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def overall_model_simulation_program_calling_manager_name(self):
        """Get overall_model_simulation_program_calling_manager_name

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `overall_model_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `overall_model_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `overall_model_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overall_model_simulation_program_calling_manager_name`')

        self._data["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """Get model_setup_and_sizing_program_calling_manager_name

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set
        """
        return self._data["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `model_setup_and_sizing_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `model_setup_and_sizing_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`')

        self._data["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_inlet_node_name`
        Air inlet node for the unit must be a zone air exhaust Node.

        Args:
            value (str): value for IDD Field `primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_inlet_node_name`')

        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        Air outlet node for the unit must be a zone air inlet node.

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_inlet_node_name`
        Inlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_inlet_node_name`')

        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """Get secondary_air_outlet_node_name

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set
        """
        return self._data["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_outlet_node_name`
        Outlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `secondary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_outlet_node_name`')

        self._data["Secondary Air Outlet Node Name"] = value

    @property
    def number_of_plant_loop_connections(self):
        """Get number_of_plant_loop_connections

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set
        """
        return self._data["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """  Corresponds to IDD Field `number_of_plant_loop_connections`

        Args:
            value (int): value for IDD Field `number_of_plant_loop_connections`
                value >= 0
                value <= 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_plant_loop_connections`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_plant_loop_connections`')
            if value > 3:
                raise ValueError('value need to be smaller 3 '
                                 'for field `number_of_plant_loop_connections`')

        self._data["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """Get plant_connection_1_inlet_node_name

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_inlet_node_name`')

        self._data["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """Get plant_connection_1_outlet_node_name

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_outlet_node_name`')

        self._data["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """Get plant_connection_2_inlet_node_name

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_inlet_node_name`')

        self._data["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """Get plant_connection_2_outlet_node_name

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_outlet_node_name`')

        self._data["Plant Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_3_inlet_node_name(self):
        """Get plant_connection_3_inlet_node_name

        Returns:
            str: the value of `plant_connection_3_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Inlet Node Name"]

    @plant_connection_3_inlet_node_name.setter
    def plant_connection_3_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_inlet_node_name`')

        self._data["Plant Connection 3 Inlet Node Name"] = value

    @property
    def plant_connection_3_outlet_node_name(self):
        """Get plant_connection_3_outlet_node_name

        Returns:
            str: the value of `plant_connection_3_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Outlet Node Name"]

    @plant_connection_3_outlet_node_name.setter
    def plant_connection_3_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_outlet_node_name`')

        self._data["Plant Connection 3 Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """Get supply_inlet_water_storage_tank_name

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_inlet_water_storage_tank_name`
        Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `supply_inlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_inlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_inlet_water_storage_tank_name`')

        self._data["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """Get collection_outlet_water_storage_tank_name

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set
        """
        return self._data["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `collection_outlet_water_storage_tank_name`
        Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `collection_outlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `collection_outlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_outlet_water_storage_tank_name`')

        self._data["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """Get ambient_zone_name

        Returns:
            str: the value of `ambient_zone_name` or None if not set
        """
        return self._data["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_zone_name`
        Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `ambient_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_zone_name`')

        self._data["Ambient Zone Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.overall_model_simulation_program_calling_manager_name))
        out.append(self._to_str(self.model_setup_and_sizing_program_calling_manager_name))
        out.append(self._to_str(self.primary_air_inlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.secondary_air_inlet_node_name))
        out.append(self._to_str(self.secondary_air_outlet_node_name))
        out.append(self._to_str(self.number_of_plant_loop_connections))
        out.append(self._to_str(self.plant_connection_1_inlet_node_name))
        out.append(self._to_str(self.plant_connection_1_outlet_node_name))
        out.append(self._to_str(self.plant_connection_2_inlet_node_name))
        out.append(self._to_str(self.plant_connection_2_outlet_node_name))
        out.append(self._to_str(self.plant_connection_3_inlet_node_name))
        out.append(self._to_str(self.plant_connection_3_outlet_node_name))
        out.append(self._to_str(self.supply_inlet_water_storage_tank_name))
        out.append(self._to_str(self.collection_outlet_water_storage_tank_name))
        out.append(self._to_str(self.ambient_zone_name))
        return ",".join(out)

class AirTerminalSingleDuctUserDefined(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:UserDefined`
        Defines a generic single duct air terminal unit for custom modeling
        using Energy Management System or External Interface
    """
    internal_name = "AirTerminal:SingleDuct:UserDefined"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Overall Model Simulation Program Calling Manager Name"] = None
        self._data["Model Setup and Sizing Program Calling Manager Name"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Secondary Air Outlet Node Name"] = None
        self._data["Number of Plant Loop Connections"] = None
        self._data["Plant Connection 1 Inlet Node Name"] = None
        self._data["Plant Connection 1 Outlet Node Name"] = None
        self._data["Plant Connection 2 Inlet Node Name"] = None
        self._data["Plant Connection 2 Outlet Node Name"] = None
        self._data["Supply Inlet Water Storage Tank Name"] = None
        self._data["Collection Outlet Water Storage Tank Name"] = None
        self._data["Ambient Zone Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.overall_model_simulation_program_calling_manager_name = None
        else:
            self.overall_model_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.model_setup_and_sizing_program_calling_manager_name = None
        else:
            self.model_setup_and_sizing_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.secondary_air_outlet_node_name = None
        else:
            self.secondary_air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_plant_loop_connections = None
        else:
            self.number_of_plant_loop_connections = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_inlet_node_name = None
        else:
            self.plant_connection_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_outlet_node_name = None
        else:
            self.plant_connection_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_inlet_node_name = None
        else:
            self.plant_connection_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_outlet_node_name = None
        else:
            self.plant_connection_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_inlet_water_storage_tank_name = None
        else:
            self.supply_inlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collection_outlet_water_storage_tank_name = None
        else:
            self.collection_outlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_zone_name = None
        else:
            self.ambient_zone_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the air terminal

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def overall_model_simulation_program_calling_manager_name(self):
        """Get overall_model_simulation_program_calling_manager_name

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `overall_model_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `overall_model_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `overall_model_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overall_model_simulation_program_calling_manager_name`')

        self._data["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """Get model_setup_and_sizing_program_calling_manager_name

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set
        """
        return self._data["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `model_setup_and_sizing_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `model_setup_and_sizing_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`')

        self._data["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_inlet_node_name`
        Air inlet node for the unit must be a zone splitter outlet.

        Args:
            value (str): value for IDD Field `primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_inlet_node_name`')

        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `primary_air_outlet_node_name`
        Air outlet node for the unit must be a zone air inlet node.

        Args:
            value (str): value for IDD Field `primary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `primary_air_outlet_node_name`')

        self._data["Primary Air Outlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_inlet_node_name`
        Inlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_inlet_node_name`')

        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """Get secondary_air_outlet_node_name

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set
        """
        return self._data["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `secondary_air_outlet_node_name`
        Outlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `secondary_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_outlet_node_name`')

        self._data["Secondary Air Outlet Node Name"] = value

    @property
    def number_of_plant_loop_connections(self):
        """Get number_of_plant_loop_connections

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set
        """
        return self._data["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """  Corresponds to IDD Field `number_of_plant_loop_connections`

        Args:
            value (int): value for IDD Field `number_of_plant_loop_connections`
                value >= 0
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_plant_loop_connections`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_plant_loop_connections`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `number_of_plant_loop_connections`')

        self._data["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """Get plant_connection_1_inlet_node_name

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_inlet_node_name`')

        self._data["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """Get plant_connection_1_outlet_node_name

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_outlet_node_name`')

        self._data["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """Get plant_connection_2_inlet_node_name

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_inlet_node_name`')

        self._data["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """Get plant_connection_2_outlet_node_name

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_outlet_node_name`')

        self._data["Plant Connection 2 Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """Get supply_inlet_water_storage_tank_name

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_inlet_water_storage_tank_name`
        Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `supply_inlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_inlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_inlet_water_storage_tank_name`')

        self._data["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """Get collection_outlet_water_storage_tank_name

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set
        """
        return self._data["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `collection_outlet_water_storage_tank_name`
        Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `collection_outlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `collection_outlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_outlet_water_storage_tank_name`')

        self._data["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """Get ambient_zone_name

        Returns:
            str: the value of `ambient_zone_name` or None if not set
        """
        return self._data["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_zone_name`
        Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `ambient_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_zone_name`')

        self._data["Ambient Zone Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.overall_model_simulation_program_calling_manager_name))
        out.append(self._to_str(self.model_setup_and_sizing_program_calling_manager_name))
        out.append(self._to_str(self.primary_air_inlet_node_name))
        out.append(self._to_str(self.primary_air_outlet_node_name))
        out.append(self._to_str(self.secondary_air_inlet_node_name))
        out.append(self._to_str(self.secondary_air_outlet_node_name))
        out.append(self._to_str(self.number_of_plant_loop_connections))
        out.append(self._to_str(self.plant_connection_1_inlet_node_name))
        out.append(self._to_str(self.plant_connection_1_outlet_node_name))
        out.append(self._to_str(self.plant_connection_2_inlet_node_name))
        out.append(self._to_str(self.plant_connection_2_outlet_node_name))
        out.append(self._to_str(self.supply_inlet_water_storage_tank_name))
        out.append(self._to_str(self.collection_outlet_water_storage_tank_name))
        out.append(self._to_str(self.ambient_zone_name))
        return ",".join(out)

class CoilUserDefined(object):
    """ Corresponds to IDD object `Coil:UserDefined`
        Defines a generic air system component for custom modeling
        using Energy Management System or External Interface
    """
    internal_name = "Coil:UserDefined"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for IDD  `Coil:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Overall Model Simulation Program Calling Manager Name"] = None
        self._data["Model Setup and Sizing Program Calling Manager Name"] = None
        self._data["Number of Air Connections"] = None
        self._data["Air Connection 1 Inlet Node Name"] = None
        self._data["Air Connection 1 Outlet Node Name"] = None
        self._data["Air Connection 2 Inlet Node Name"] = None
        self._data["Air Connection 2 Outlet Node Name"] = None
        self._data["Plant Connection is Used"] = None
        self._data["Plant Connection Inlet Node Name"] = None
        self._data["Plant Connection Outlet Node Name"] = None
        self._data["Supply Inlet Water Storage Tank Name"] = None
        self._data["Collection Outlet Water Storage Tank Name"] = None
        self._data["Ambient Zone Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.overall_model_simulation_program_calling_manager_name = None
        else:
            self.overall_model_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.model_setup_and_sizing_program_calling_manager_name = None
        else:
            self.model_setup_and_sizing_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_air_connections = None
        else:
            self.number_of_air_connections = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_1_inlet_node_name = None
        else:
            self.air_connection_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_1_outlet_node_name = None
        else:
            self.air_connection_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_2_inlet_node_name = None
        else:
            self.air_connection_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_2_outlet_node_name = None
        else:
            self.air_connection_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_is_used = None
        else:
            self.plant_connection_is_used = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_inlet_node_name = None
        else:
            self.plant_connection_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_outlet_node_name = None
        else:
            self.plant_connection_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_inlet_water_storage_tank_name = None
        else:
            self.supply_inlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collection_outlet_water_storage_tank_name = None
        else:
            self.collection_outlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_zone_name = None
        else:
            self.ambient_zone_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the coil

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def overall_model_simulation_program_calling_manager_name(self):
        """Get overall_model_simulation_program_calling_manager_name

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `overall_model_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `overall_model_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `overall_model_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overall_model_simulation_program_calling_manager_name`')

        self._data["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """Get model_setup_and_sizing_program_calling_manager_name

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set
        """
        return self._data["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `model_setup_and_sizing_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `model_setup_and_sizing_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `model_setup_and_sizing_program_calling_manager_name`')

        self._data["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def number_of_air_connections(self):
        """Get number_of_air_connections

        Returns:
            int: the value of `number_of_air_connections` or None if not set
        """
        return self._data["Number of Air Connections"]

    @number_of_air_connections.setter
    def number_of_air_connections(self, value=None):
        """  Corresponds to IDD Field `number_of_air_connections`

        Args:
            value (int): value for IDD Field `number_of_air_connections`
                value >= 1
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_air_connections`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_air_connections`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `number_of_air_connections`')

        self._data["Number of Air Connections"] = value

    @property
    def air_connection_1_inlet_node_name(self):
        """Get air_connection_1_inlet_node_name

        Returns:
            str: the value of `air_connection_1_inlet_node_name` or None if not set
        """
        return self._data["Air Connection 1 Inlet Node Name"]

    @air_connection_1_inlet_node_name.setter
    def air_connection_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_1_inlet_node_name`
        Inlet air for primary air stream

        Args:
            value (str): value for IDD Field `air_connection_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_1_inlet_node_name`')

        self._data["Air Connection 1 Inlet Node Name"] = value

    @property
    def air_connection_1_outlet_node_name(self):
        """Get air_connection_1_outlet_node_name

        Returns:
            str: the value of `air_connection_1_outlet_node_name` or None if not set
        """
        return self._data["Air Connection 1 Outlet Node Name"]

    @air_connection_1_outlet_node_name.setter
    def air_connection_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_1_outlet_node_name`
        Outlet air for primary air stream

        Args:
            value (str): value for IDD Field `air_connection_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_1_outlet_node_name`')

        self._data["Air Connection 1 Outlet Node Name"] = value

    @property
    def air_connection_2_inlet_node_name(self):
        """Get air_connection_2_inlet_node_name

        Returns:
            str: the value of `air_connection_2_inlet_node_name` or None if not set
        """
        return self._data["Air Connection 2 Inlet Node Name"]

    @air_connection_2_inlet_node_name.setter
    def air_connection_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_2_inlet_node_name`
        Inlet air for secondary air stream

        Args:
            value (str): value for IDD Field `air_connection_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_2_inlet_node_name`')

        self._data["Air Connection 2 Inlet Node Name"] = value

    @property
    def air_connection_2_outlet_node_name(self):
        """Get air_connection_2_outlet_node_name

        Returns:
            str: the value of `air_connection_2_outlet_node_name` or None if not set
        """
        return self._data["Air Connection 2 Outlet Node Name"]

    @air_connection_2_outlet_node_name.setter
    def air_connection_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_2_outlet_node_name`
        Outlet air for secondary air stream

        Args:
            value (str): value for IDD Field `air_connection_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_2_outlet_node_name`')

        self._data["Air Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_is_used(self):
        """Get plant_connection_is_used

        Returns:
            str: the value of `plant_connection_is_used` or None if not set
        """
        return self._data["Plant Connection is Used"]

    @plant_connection_is_used.setter
    def plant_connection_is_used(self, value=None):
        """  Corresponds to IDD Field `plant_connection_is_used`

        Args:
            value (str): value for IDD Field `plant_connection_is_used`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_is_used`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_is_used`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_is_used`'.format(value))

        self._data["Plant Connection is Used"] = value

    @property
    def plant_connection_inlet_node_name(self):
        """Get plant_connection_inlet_node_name

        Returns:
            str: the value of `plant_connection_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection Inlet Node Name"]

    @plant_connection_inlet_node_name.setter
    def plant_connection_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_inlet_node_name`')

        self._data["Plant Connection Inlet Node Name"] = value

    @property
    def plant_connection_outlet_node_name(self):
        """Get plant_connection_outlet_node_name

        Returns:
            str: the value of `plant_connection_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection Outlet Node Name"]

    @plant_connection_outlet_node_name.setter
    def plant_connection_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_outlet_node_name`')

        self._data["Plant Connection Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """Get supply_inlet_water_storage_tank_name

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_inlet_water_storage_tank_name`
        Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `supply_inlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_inlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_inlet_water_storage_tank_name`')

        self._data["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """Get collection_outlet_water_storage_tank_name

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set
        """
        return self._data["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `collection_outlet_water_storage_tank_name`
        Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `collection_outlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `collection_outlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_outlet_water_storage_tank_name`')

        self._data["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """Get ambient_zone_name

        Returns:
            str: the value of `ambient_zone_name` or None if not set
        """
        return self._data["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_zone_name`
        Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `ambient_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_zone_name`')

        self._data["Ambient Zone Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.overall_model_simulation_program_calling_manager_name))
        out.append(self._to_str(self.model_setup_and_sizing_program_calling_manager_name))
        out.append(self._to_str(self.number_of_air_connections))
        out.append(self._to_str(self.air_connection_1_inlet_node_name))
        out.append(self._to_str(self.air_connection_1_outlet_node_name))
        out.append(self._to_str(self.air_connection_2_inlet_node_name))
        out.append(self._to_str(self.air_connection_2_outlet_node_name))
        out.append(self._to_str(self.plant_connection_is_used))
        out.append(self._to_str(self.plant_connection_inlet_node_name))
        out.append(self._to_str(self.plant_connection_outlet_node_name))
        out.append(self._to_str(self.supply_inlet_water_storage_tank_name))
        out.append(self._to_str(self.collection_outlet_water_storage_tank_name))
        out.append(self._to_str(self.ambient_zone_name))
        return ",".join(out)

class PlantComponentUserDefined(object):
    """ Corresponds to IDD object `PlantComponent:UserDefined`
        Defines a generic plant component for custom modeling
        using Energy Management System or External Interface
    """
    internal_name = "PlantComponent:UserDefined"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantComponent:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Main Model Program Calling Manager Name"] = None
        self._data["Number of Plant Loop Connections"] = None
        self._data["Plant Connection 1 Inlet Node Name"] = None
        self._data["Plant Connection 1 Outlet Node Name"] = None
        self._data["Plant Connection 1 Loading Mode"] = None
        self._data["Plant Connection 1 Loop Flow Request Mode"] = None
        self._data["Plant Connection 1 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 1 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 2 Inlet Node Name"] = None
        self._data["Plant Connection 2 Outlet Node Name"] = None
        self._data["Plant Connection 2 Loading Mode"] = None
        self._data["Plant Connection 2 Loop Flow Request Mode"] = None
        self._data["Plant Connection 2 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 2 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 3 Inlet Node Name"] = None
        self._data["Plant Connection 3 Outlet Node Name"] = None
        self._data["Plant Connection 3 Loading Mode"] = None
        self._data["Plant Connection 3 Loop Flow Request Mode"] = None
        self._data["Plant Connection 3 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 3 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 4 Inlet Node Name"] = None
        self._data["Plant Connection 4 Outlet Node Name"] = None
        self._data["Plant Connection 4 Loading Mode"] = None
        self._data["Plant Connection 4 Loop Flow Request Mode"] = None
        self._data["Plant Connection 4 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 4 Simulation Program Calling Manager Name"] = None
        self._data["Air Connection Inlet Node Name"] = None
        self._data["Air Connection Outlet Node Name"] = None
        self._data["Supply Inlet Water Storage Tank Name"] = None
        self._data["Collection Outlet Water Storage Tank Name"] = None
        self._data["Ambient Zone Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.main_model_program_calling_manager_name = None
        else:
            self.main_model_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_plant_loop_connections = None
        else:
            self.number_of_plant_loop_connections = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_inlet_node_name = None
        else:
            self.plant_connection_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_outlet_node_name = None
        else:
            self.plant_connection_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_loading_mode = None
        else:
            self.plant_connection_1_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_loop_flow_request_mode = None
        else:
            self.plant_connection_1_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_1_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_1_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_inlet_node_name = None
        else:
            self.plant_connection_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_outlet_node_name = None
        else:
            self.plant_connection_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_loading_mode = None
        else:
            self.plant_connection_2_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_loop_flow_request_mode = None
        else:
            self.plant_connection_2_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_2_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_2_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_inlet_node_name = None
        else:
            self.plant_connection_3_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_outlet_node_name = None
        else:
            self.plant_connection_3_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_loading_mode = None
        else:
            self.plant_connection_3_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_loop_flow_request_mode = None
        else:
            self.plant_connection_3_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_3_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_3_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_inlet_node_name = None
        else:
            self.plant_connection_4_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_outlet_node_name = None
        else:
            self.plant_connection_4_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_loading_mode = None
        else:
            self.plant_connection_4_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_loop_flow_request_mode = None
        else:
            self.plant_connection_4_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_4_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_4_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_inlet_node_name = None
        else:
            self.air_connection_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_outlet_node_name = None
        else:
            self.air_connection_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_inlet_water_storage_tank_name = None
        else:
            self.supply_inlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collection_outlet_water_storage_tank_name = None
        else:
            self.collection_outlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_zone_name = None
        else:
            self.ambient_zone_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the plant component

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def main_model_program_calling_manager_name(self):
        """Get main_model_program_calling_manager_name

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set
        """
        return self._data["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `main_model_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `main_model_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `main_model_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `main_model_program_calling_manager_name`')

        self._data["Main Model Program Calling Manager Name"] = value

    @property
    def number_of_plant_loop_connections(self):
        """Get number_of_plant_loop_connections

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set
        """
        return self._data["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """  Corresponds to IDD Field `number_of_plant_loop_connections`

        Args:
            value (int): value for IDD Field `number_of_plant_loop_connections`
                value >= 1
                value <= 4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_plant_loop_connections`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_plant_loop_connections`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_plant_loop_connections`')

        self._data["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """Get plant_connection_1_inlet_node_name

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_inlet_node_name`')

        self._data["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """Get plant_connection_1_outlet_node_name

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_outlet_node_name`')

        self._data["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_1_loading_mode(self):
        """Get plant_connection_1_loading_mode

        Returns:
            str: the value of `plant_connection_1_loading_mode` or None if not set
        """
        return self._data["Plant Connection 1 Loading Mode"]

    @plant_connection_1_loading_mode.setter
    def plant_connection_1_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_1_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetsLoadWithPassiveCapacity
                      - MeetsLoadWithNominalCapacity
                      - MeetsLoadWithNominalCapacityLowOutLimit
                      - MeetsLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetsLoadWithPassiveCapacity")
            vals.add("MeetsLoadWithNominalCapacity")
            vals.add("MeetsLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetsLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_1_loading_mode`'.format(value))

        self._data["Plant Connection 1 Loading Mode"] = value

    @property
    def plant_connection_1_loop_flow_request_mode(self):
        """Get plant_connection_1_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_1_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 1 Loop Flow Request Mode"]

    @plant_connection_1_loop_flow_request_mode.setter
    def plant_connection_1_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_1_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_loop_flow_request_mode`')

        self._data["Plant Connection 1 Loop Flow Request Mode"] = value

    @property
    def plant_connection_1_initialization_program_calling_manager_name(self):
        """Get plant_connection_1_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_1_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 1 Initialization Program Calling Manager Name"]

    @plant_connection_1_initialization_program_calling_manager_name.setter
    def plant_connection_1_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_initialization_program_calling_manager_name`')

        self._data["Plant Connection 1 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_1_simulation_program_calling_manager_name(self):
        """Get plant_connection_1_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_1_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 1 Simulation Program Calling Manager Name"]

    @plant_connection_1_simulation_program_calling_manager_name.setter
    def plant_connection_1_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_simulation_program_calling_manager_name`')

        self._data["Plant Connection 1 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """Get plant_connection_2_inlet_node_name

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_inlet_node_name`')

        self._data["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """Get plant_connection_2_outlet_node_name

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_outlet_node_name`')

        self._data["Plant Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_2_loading_mode(self):
        """Get plant_connection_2_loading_mode

        Returns:
            str: the value of `plant_connection_2_loading_mode` or None if not set
        """
        return self._data["Plant Connection 2 Loading Mode"]

    @plant_connection_2_loading_mode.setter
    def plant_connection_2_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_2_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_2_loading_mode`'.format(value))

        self._data["Plant Connection 2 Loading Mode"] = value

    @property
    def plant_connection_2_loop_flow_request_mode(self):
        """Get plant_connection_2_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_2_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 2 Loop Flow Request Mode"]

    @plant_connection_2_loop_flow_request_mode.setter
    def plant_connection_2_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_2_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_loop_flow_request_mode`')

        self._data["Plant Connection 2 Loop Flow Request Mode"] = value

    @property
    def plant_connection_2_initialization_program_calling_manager_name(self):
        """Get plant_connection_2_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_2_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 2 Initialization Program Calling Manager Name"]

    @plant_connection_2_initialization_program_calling_manager_name.setter
    def plant_connection_2_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_initialization_program_calling_manager_name`')

        self._data["Plant Connection 2 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_2_simulation_program_calling_manager_name(self):
        """Get plant_connection_2_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_2_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 2 Simulation Program Calling Manager Name"]

    @plant_connection_2_simulation_program_calling_manager_name.setter
    def plant_connection_2_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_simulation_program_calling_manager_name`')

        self._data["Plant Connection 2 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_3_inlet_node_name(self):
        """Get plant_connection_3_inlet_node_name

        Returns:
            str: the value of `plant_connection_3_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Inlet Node Name"]

    @plant_connection_3_inlet_node_name.setter
    def plant_connection_3_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_inlet_node_name`')

        self._data["Plant Connection 3 Inlet Node Name"] = value

    @property
    def plant_connection_3_outlet_node_name(self):
        """Get plant_connection_3_outlet_node_name

        Returns:
            str: the value of `plant_connection_3_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Outlet Node Name"]

    @plant_connection_3_outlet_node_name.setter
    def plant_connection_3_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_outlet_node_name`')

        self._data["Plant Connection 3 Outlet Node Name"] = value

    @property
    def plant_connection_3_loading_mode(self):
        """Get plant_connection_3_loading_mode

        Returns:
            str: the value of `plant_connection_3_loading_mode` or None if not set
        """
        return self._data["Plant Connection 3 Loading Mode"]

    @plant_connection_3_loading_mode.setter
    def plant_connection_3_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_3_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_3_loading_mode`'.format(value))

        self._data["Plant Connection 3 Loading Mode"] = value

    @property
    def plant_connection_3_loop_flow_request_mode(self):
        """Get plant_connection_3_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_3_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 3 Loop Flow Request Mode"]

    @plant_connection_3_loop_flow_request_mode.setter
    def plant_connection_3_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_3_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_loop_flow_request_mode`')

        self._data["Plant Connection 3 Loop Flow Request Mode"] = value

    @property
    def plant_connection_3_initialization_program_calling_manager_name(self):
        """Get plant_connection_3_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_3_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 3 Initialization Program Calling Manager Name"]

    @plant_connection_3_initialization_program_calling_manager_name.setter
    def plant_connection_3_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_initialization_program_calling_manager_name`')

        self._data["Plant Connection 3 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_3_simulation_program_calling_manager_name(self):
        """Get plant_connection_3_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_3_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 3 Simulation Program Calling Manager Name"]

    @plant_connection_3_simulation_program_calling_manager_name.setter
    def plant_connection_3_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_simulation_program_calling_manager_name`')

        self._data["Plant Connection 3 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_4_inlet_node_name(self):
        """Get plant_connection_4_inlet_node_name

        Returns:
            str: the value of `plant_connection_4_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 4 Inlet Node Name"]

    @plant_connection_4_inlet_node_name.setter
    def plant_connection_4_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_inlet_node_name`')

        self._data["Plant Connection 4 Inlet Node Name"] = value

    @property
    def plant_connection_4_outlet_node_name(self):
        """Get plant_connection_4_outlet_node_name

        Returns:
            str: the value of `plant_connection_4_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 4 Outlet Node Name"]

    @plant_connection_4_outlet_node_name.setter
    def plant_connection_4_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_outlet_node_name`')

        self._data["Plant Connection 4 Outlet Node Name"] = value

    @property
    def plant_connection_4_loading_mode(self):
        """Get plant_connection_4_loading_mode

        Returns:
            str: the value of `plant_connection_4_loading_mode` or None if not set
        """
        return self._data["Plant Connection 4 Loading Mode"]

    @plant_connection_4_loading_mode.setter
    def plant_connection_4_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_4_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_4_loading_mode`'.format(value))

        self._data["Plant Connection 4 Loading Mode"] = value

    @property
    def plant_connection_4_loop_flow_request_mode(self):
        """Get plant_connection_4_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_4_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 4 Loop Flow Request Mode"]

    @plant_connection_4_loop_flow_request_mode.setter
    def plant_connection_4_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_4_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_loop_flow_request_mode`')

        self._data["Plant Connection 4 Loop Flow Request Mode"] = value

    @property
    def plant_connection_4_initialization_program_calling_manager_name(self):
        """Get plant_connection_4_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_4_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 4 Initialization Program Calling Manager Name"]

    @plant_connection_4_initialization_program_calling_manager_name.setter
    def plant_connection_4_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_initialization_program_calling_manager_name`')

        self._data["Plant Connection 4 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_4_simulation_program_calling_manager_name(self):
        """Get plant_connection_4_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_4_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 4 Simulation Program Calling Manager Name"]

    @plant_connection_4_simulation_program_calling_manager_name.setter
    def plant_connection_4_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_simulation_program_calling_manager_name`')

        self._data["Plant Connection 4 Simulation Program Calling Manager Name"] = value

    @property
    def air_connection_inlet_node_name(self):
        """Get air_connection_inlet_node_name

        Returns:
            str: the value of `air_connection_inlet_node_name` or None if not set
        """
        return self._data["Air Connection Inlet Node Name"]

    @air_connection_inlet_node_name.setter
    def air_connection_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_inlet_node_name`
        Inlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `air_connection_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_inlet_node_name`')

        self._data["Air Connection Inlet Node Name"] = value

    @property
    def air_connection_outlet_node_name(self):
        """Get air_connection_outlet_node_name

        Returns:
            str: the value of `air_connection_outlet_node_name` or None if not set
        """
        return self._data["Air Connection Outlet Node Name"]

    @air_connection_outlet_node_name.setter
    def air_connection_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_outlet_node_name`
        Outlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `air_connection_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_outlet_node_name`')

        self._data["Air Connection Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """Get supply_inlet_water_storage_tank_name

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_inlet_water_storage_tank_name`
        Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `supply_inlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_inlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_inlet_water_storage_tank_name`')

        self._data["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """Get collection_outlet_water_storage_tank_name

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set
        """
        return self._data["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `collection_outlet_water_storage_tank_name`
        Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `collection_outlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `collection_outlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_outlet_water_storage_tank_name`')

        self._data["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """Get ambient_zone_name

        Returns:
            str: the value of `ambient_zone_name` or None if not set
        """
        return self._data["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_zone_name`
        Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `ambient_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_zone_name`')

        self._data["Ambient Zone Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.main_model_program_calling_manager_name))
        out.append(self._to_str(self.number_of_plant_loop_connections))
        out.append(self._to_str(self.plant_connection_1_inlet_node_name))
        out.append(self._to_str(self.plant_connection_1_outlet_node_name))
        out.append(self._to_str(self.plant_connection_1_loading_mode))
        out.append(self._to_str(self.plant_connection_1_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_1_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_1_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_2_inlet_node_name))
        out.append(self._to_str(self.plant_connection_2_outlet_node_name))
        out.append(self._to_str(self.plant_connection_2_loading_mode))
        out.append(self._to_str(self.plant_connection_2_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_2_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_2_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_3_inlet_node_name))
        out.append(self._to_str(self.plant_connection_3_outlet_node_name))
        out.append(self._to_str(self.plant_connection_3_loading_mode))
        out.append(self._to_str(self.plant_connection_3_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_3_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_3_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_4_inlet_node_name))
        out.append(self._to_str(self.plant_connection_4_outlet_node_name))
        out.append(self._to_str(self.plant_connection_4_loading_mode))
        out.append(self._to_str(self.plant_connection_4_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_4_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_4_simulation_program_calling_manager_name))
        out.append(self._to_str(self.air_connection_inlet_node_name))
        out.append(self._to_str(self.air_connection_outlet_node_name))
        out.append(self._to_str(self.supply_inlet_water_storage_tank_name))
        out.append(self._to_str(self.collection_outlet_water_storage_tank_name))
        out.append(self._to_str(self.ambient_zone_name))
        return ",".join(out)

class PlantEquipmentOperationUserDefined(object):
    """ Corresponds to IDD object `PlantEquipmentOperation:UserDefined`
        Defines a generic plant operation scheme for custom supervisory control
        using Energy Management System or External Interface to dispatch loads
    """
    internal_name = "PlantEquipmentOperation:UserDefined"
    field_count = 23

    def __init__(self):
        """ Init data dictionary object for IDD  `PlantEquipmentOperation:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Main Model Program Calling Manager Name"] = None
        self._data["Initialization Program Calling Manager Name"] = None
        self._data["Equipment 1 Object Type"] = None
        self._data["Equipment 1 Name"] = None
        self._data["Equipment 2 Object Type"] = None
        self._data["Equipment 2 Name"] = None
        self._data["Equipment 3 Object Type"] = None
        self._data["Equipment 3 Name"] = None
        self._data["Equipment 4 Object Type"] = None
        self._data["Equipment 4 Name"] = None
        self._data["Equipment 5 Object Type"] = None
        self._data["Equipment 5 Name"] = None
        self._data["Equipment 6 Object Type"] = None
        self._data["Equipment 6 Name"] = None
        self._data["Equipment 7 Object Type"] = None
        self._data["Equipment 7 Name"] = None
        self._data["Equipment 8 Object Type"] = None
        self._data["Equipment 8 Name"] = None
        self._data["Equipment 9 Object Type"] = None
        self._data["Equipment 9 Name"] = None
        self._data["Equipment 10 Object Type"] = None
        self._data["Equipment 10 Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.main_model_program_calling_manager_name = None
        else:
            self.main_model_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initialization_program_calling_manager_name = None
        else:
            self.initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_1_object_type = None
        else:
            self.equipment_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_1_name = None
        else:
            self.equipment_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_2_object_type = None
        else:
            self.equipment_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_2_name = None
        else:
            self.equipment_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_3_object_type = None
        else:
            self.equipment_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_3_name = None
        else:
            self.equipment_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_4_object_type = None
        else:
            self.equipment_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_4_name = None
        else:
            self.equipment_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_5_object_type = None
        else:
            self.equipment_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_5_name = None
        else:
            self.equipment_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_6_object_type = None
        else:
            self.equipment_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_6_name = None
        else:
            self.equipment_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_7_object_type = None
        else:
            self.equipment_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_7_name = None
        else:
            self.equipment_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_8_object_type = None
        else:
            self.equipment_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_8_name = None
        else:
            self.equipment_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_9_object_type = None
        else:
            self.equipment_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_9_name = None
        else:
            self.equipment_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_10_object_type = None
        else:
            self.equipment_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.equipment_10_name = None
        else:
            self.equipment_10_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the plant operation scheme

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def main_model_program_calling_manager_name(self):
        """Get main_model_program_calling_manager_name

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set
        """
        return self._data["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `main_model_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `main_model_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `main_model_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `main_model_program_calling_manager_name`')

        self._data["Main Model Program Calling Manager Name"] = value

    @property
    def initialization_program_calling_manager_name(self):
        """Get initialization_program_calling_manager_name

        Returns:
            str: the value of `initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Initialization Program Calling Manager Name"]

    @initialization_program_calling_manager_name.setter
    def initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `initialization_program_calling_manager_name`')

        self._data["Initialization Program Calling Manager Name"] = value

    @property
    def equipment_1_object_type(self):
        """Get equipment_1_object_type

        Returns:
            str: the value of `equipment_1_object_type` or None if not set
        """
        return self._data["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_1_object_type`

        Args:
            value (str): value for IDD Field `equipment_1_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_object_type`')

        self._data["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """Get equipment_1_name

        Returns:
            str: the value of `equipment_1_name` or None if not set
        """
        return self._data["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `equipment_1_name`

        Args:
            value (str): value for IDD Field `equipment_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_1_name`')

        self._data["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """Get equipment_2_object_type

        Returns:
            str: the value of `equipment_2_object_type` or None if not set
        """
        return self._data["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_2_object_type`

        Args:
            value (str): value for IDD Field `equipment_2_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_object_type`')

        self._data["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """Get equipment_2_name

        Returns:
            str: the value of `equipment_2_name` or None if not set
        """
        return self._data["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `equipment_2_name`

        Args:
            value (str): value for IDD Field `equipment_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_2_name`')

        self._data["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """Get equipment_3_object_type

        Returns:
            str: the value of `equipment_3_object_type` or None if not set
        """
        return self._data["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_3_object_type`

        Args:
            value (str): value for IDD Field `equipment_3_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_object_type`')

        self._data["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """Get equipment_3_name

        Returns:
            str: the value of `equipment_3_name` or None if not set
        """
        return self._data["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `equipment_3_name`

        Args:
            value (str): value for IDD Field `equipment_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_3_name`')

        self._data["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """Get equipment_4_object_type

        Returns:
            str: the value of `equipment_4_object_type` or None if not set
        """
        return self._data["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_4_object_type`

        Args:
            value (str): value for IDD Field `equipment_4_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_object_type`')

        self._data["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """Get equipment_4_name

        Returns:
            str: the value of `equipment_4_name` or None if not set
        """
        return self._data["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `equipment_4_name`

        Args:
            value (str): value for IDD Field `equipment_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_4_name`')

        self._data["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """Get equipment_5_object_type

        Returns:
            str: the value of `equipment_5_object_type` or None if not set
        """
        return self._data["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_5_object_type`

        Args:
            value (str): value for IDD Field `equipment_5_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_object_type`')

        self._data["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """Get equipment_5_name

        Returns:
            str: the value of `equipment_5_name` or None if not set
        """
        return self._data["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `equipment_5_name`

        Args:
            value (str): value for IDD Field `equipment_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_5_name`')

        self._data["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """Get equipment_6_object_type

        Returns:
            str: the value of `equipment_6_object_type` or None if not set
        """
        return self._data["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_6_object_type`

        Args:
            value (str): value for IDD Field `equipment_6_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_object_type`')

        self._data["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """Get equipment_6_name

        Returns:
            str: the value of `equipment_6_name` or None if not set
        """
        return self._data["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `equipment_6_name`

        Args:
            value (str): value for IDD Field `equipment_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_6_name`')

        self._data["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """Get equipment_7_object_type

        Returns:
            str: the value of `equipment_7_object_type` or None if not set
        """
        return self._data["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_7_object_type`

        Args:
            value (str): value for IDD Field `equipment_7_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_object_type`')

        self._data["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """Get equipment_7_name

        Returns:
            str: the value of `equipment_7_name` or None if not set
        """
        return self._data["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `equipment_7_name`

        Args:
            value (str): value for IDD Field `equipment_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_7_name`')

        self._data["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """Get equipment_8_object_type

        Returns:
            str: the value of `equipment_8_object_type` or None if not set
        """
        return self._data["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_8_object_type`

        Args:
            value (str): value for IDD Field `equipment_8_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_object_type`')

        self._data["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """Get equipment_8_name

        Returns:
            str: the value of `equipment_8_name` or None if not set
        """
        return self._data["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `equipment_8_name`

        Args:
            value (str): value for IDD Field `equipment_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_8_name`')

        self._data["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """Get equipment_9_object_type

        Returns:
            str: the value of `equipment_9_object_type` or None if not set
        """
        return self._data["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_9_object_type`

        Args:
            value (str): value for IDD Field `equipment_9_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_object_type`')

        self._data["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """Get equipment_9_name

        Returns:
            str: the value of `equipment_9_name` or None if not set
        """
        return self._data["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `equipment_9_name`

        Args:
            value (str): value for IDD Field `equipment_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_9_name`')

        self._data["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """Get equipment_10_object_type

        Returns:
            str: the value of `equipment_10_object_type` or None if not set
        """
        return self._data["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `equipment_10_object_type`

        Args:
            value (str): value for IDD Field `equipment_10_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_object_type`')

        self._data["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """Get equipment_10_name

        Returns:
            str: the value of `equipment_10_name` or None if not set
        """
        return self._data["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `equipment_10_name`

        Args:
            value (str): value for IDD Field `equipment_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `equipment_10_name`')

        self._data["Equipment 10 Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.main_model_program_calling_manager_name))
        out.append(self._to_str(self.initialization_program_calling_manager_name))
        out.append(self._to_str(self.equipment_1_object_type))
        out.append(self._to_str(self.equipment_1_name))
        out.append(self._to_str(self.equipment_2_object_type))
        out.append(self._to_str(self.equipment_2_name))
        out.append(self._to_str(self.equipment_3_object_type))
        out.append(self._to_str(self.equipment_3_name))
        out.append(self._to_str(self.equipment_4_object_type))
        out.append(self._to_str(self.equipment_4_name))
        out.append(self._to_str(self.equipment_5_object_type))
        out.append(self._to_str(self.equipment_5_name))
        out.append(self._to_str(self.equipment_6_object_type))
        out.append(self._to_str(self.equipment_6_name))
        out.append(self._to_str(self.equipment_7_object_type))
        out.append(self._to_str(self.equipment_7_name))
        out.append(self._to_str(self.equipment_8_object_type))
        out.append(self._to_str(self.equipment_8_name))
        out.append(self._to_str(self.equipment_9_object_type))
        out.append(self._to_str(self.equipment_9_name))
        out.append(self._to_str(self.equipment_10_object_type))
        out.append(self._to_str(self.equipment_10_name))
        return ",".join(out)