"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.5.0
    Contact: pinterest-api@pinterest.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pinterest.generated.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from pinterest.generated.client.exceptions import ApiAttributeError


def lazy_import():
    from pinterest.generated.client.model.action_type import ActionType
    from pinterest.generated.client.model.ad_group_common import AdGroupCommon
    from pinterest.generated.client.model.ad_group_create_request_all_of import AdGroupCreateRequestAllOf
    from pinterest.generated.client.model.budget_type import BudgetType
    from pinterest.generated.client.model.entity_status import EntityStatus
    from pinterest.generated.client.model.pacing_delivery_type import PacingDeliveryType
    from pinterest.generated.client.model.placement_group_type import PlacementGroupType
    from pinterest.generated.client.model.targeting_spec import TargetingSpec
    from pinterest.generated.client.model.tracking_urls import TrackingUrls
    globals()['ActionType'] = ActionType
    globals()['AdGroupCommon'] = AdGroupCommon
    globals()['AdGroupCreateRequestAllOf'] = AdGroupCreateRequestAllOf
    globals()['BudgetType'] = BudgetType
    globals()['EntityStatus'] = EntityStatus
    globals()['PacingDeliveryType'] = PacingDeliveryType
    globals()['PlacementGroupType'] = PlacementGroupType
    globals()['TargetingSpec'] = TargetingSpec
    globals()['TrackingUrls'] = TrackingUrls


class AdGroupCreateRequest(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('bid_strategy_type',): {
            'AUTOMATIC_BID': "AUTOMATIC_BID",
            'MAX_BID': "MAX_BID",
            'TARGET_AVG': "TARGET_AVG",
        },
    }

    validations = {
        ('campaign_id',): {
            'regex': {
                'pattern': r'^[C]?\d+$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'campaign_id': (str,),  # noqa: E501
            'billable_event': (ActionType,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'budget_in_micro_currency': (int, none_type,),  # noqa: E501
            'bid_in_micro_currency': (int, none_type,),  # noqa: E501
            'bid_strategy_type': (str,),  # noqa: E501
            'budget_type': (BudgetType,),  # noqa: E501
            'start_time': (int, none_type,),  # noqa: E501
            'end_time': (int, none_type,),  # noqa: E501
            'targeting_spec': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'lifetime_frequency_cap': (int,),  # noqa: E501
            'tracking_urls': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'auto_targeting_enabled': (bool, none_type,),  # noqa: E501
            'placement_group': (str,),  # noqa: E501
            'pacing_delivery_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'campaign_id': 'campaign_id',  # noqa: E501
        'billable_event': 'billable_event',  # noqa: E501
        'status': 'status',  # noqa: E501
        'budget_in_micro_currency': 'budget_in_micro_currency',  # noqa: E501
        'bid_in_micro_currency': 'bid_in_micro_currency',  # noqa: E501
        'bid_strategy_type': 'bid_strategy_type',  # noqa: E501
        'budget_type': 'budget_type',  # noqa: E501
        'start_time': 'start_time',  # noqa: E501
        'end_time': 'end_time',  # noqa: E501
        'targeting_spec': 'targeting_spec',  # noqa: E501
        'lifetime_frequency_cap': 'lifetime_frequency_cap',  # noqa: E501
        'tracking_urls': 'tracking_urls',  # noqa: E501
        'auto_targeting_enabled': 'auto_targeting_enabled',  # noqa: E501
        'placement_group': 'placement_group',  # noqa: E501
        'pacing_delivery_type': 'pacing_delivery_type',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AdGroupCreateRequest - a model defined in OpenAPI

        Keyword Args:
            name (str): Ad group name.
            campaign_id (str): Campaign ID of the ad group.
            billable_event (ActionType):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (str): Ad group/entity status.. [optional]  # noqa: E501
            budget_in_micro_currency (int, none_type): Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns.  A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups.. [optional]  # noqa: E501
            bid_in_micro_currency (int, none_type): Bid price in micro currency. This field is **REQUIRED** for the following campaign objective_type/billable_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG_SALES/CLICKTHROUGH, VIDEO_VIEW/VIDEO_V_50_MRC.. [optional]  # noqa: E501
            bid_strategy_type (str): [optional]  # noqa: E501
            budget_type (BudgetType): [optional]  # noqa: E501
            start_time (int, none_type): Ad group start time. Unix timestamp in seconds. Defaults to current time.. [optional]  # noqa: E501
            end_time (int, none_type): Ad group end time. Unix timestamp in seconds.. [optional]  # noqa: E501
            targeting_spec ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            lifetime_frequency_cap (int): Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions))  ad groups. A CPM ad group has an IMPRESSION <a href=\"https://developers.pinterest.com/docs/redoc/#section/Billable-event\">billable_event</a> value. This field **REQUIRES** the `end_time` field.. [optional]  # noqa: E501
            tracking_urls ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Third-party tracking URLs.<br> JSON object with the format: {\"<a href=\"https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event\">Tracking event enum</a>\":[URL string array],...}<br> For example: {\"impression\": [\"URL1\", \"URL2\"], \"click\": [\"URL1\", \"URL2\", \"URL3\"]}.<br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs.<br><br> For more information, see <a href=\"https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking\" target=\"_blank\">Third-party and dynamic tracking</a>.. [optional]  # noqa: E501
            auto_targeting_enabled (bool, none_type): Enable auto-targeting for ad group. Also known as <a href=\"https://help.pinterest.com/en/business/article/expanded-targeting\" target=\"_blank\">\"expanded targeting\"</a>.. [optional]  # noqa: E501
            placement_group (str): <a href=\"https://developers.pinterest.com/docs/redoc/#section/Placement-group\">Placement group</a>.. [optional]  # noqa: E501
            pacing_delivery_type (str): Pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AdGroupCreateRequest - a model defined in OpenAPI

        Keyword Args:
            name (str): Ad group name.
            campaign_id (str): Campaign ID of the ad group.
            billable_event (ActionType):
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            status (str): Ad group/entity status.. [optional]  # noqa: E501
            budget_in_micro_currency (int, none_type): Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns.  A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups.. [optional]  # noqa: E501
            bid_in_micro_currency (int, none_type): Bid price in micro currency. This field is **REQUIRED** for the following campaign objective_type/billable_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG_SALES/CLICKTHROUGH, VIDEO_VIEW/VIDEO_V_50_MRC.. [optional]  # noqa: E501
            bid_strategy_type (str): [optional]  # noqa: E501
            budget_type (BudgetType): [optional]  # noqa: E501
            start_time (int, none_type): Ad group start time. Unix timestamp in seconds. Defaults to current time.. [optional]  # noqa: E501
            end_time (int, none_type): Ad group end time. Unix timestamp in seconds.. [optional]  # noqa: E501
            targeting_spec ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            lifetime_frequency_cap (int): Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions))  ad groups. A CPM ad group has an IMPRESSION <a href=\"https://developers.pinterest.com/docs/redoc/#section/Billable-event\">billable_event</a> value. This field **REQUIRES** the `end_time` field.. [optional]  # noqa: E501
            tracking_urls ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Third-party tracking URLs.<br> JSON object with the format: {\"<a href=\"https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event\">Tracking event enum</a>\":[URL string array],...}<br> For example: {\"impression\": [\"URL1\", \"URL2\"], \"click\": [\"URL1\", \"URL2\", \"URL3\"]}.<br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs.<br><br> For more information, see <a href=\"https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking\" target=\"_blank\">Third-party and dynamic tracking</a>.. [optional]  # noqa: E501
            auto_targeting_enabled (bool, none_type): Enable auto-targeting for ad group. Also known as <a href=\"https://help.pinterest.com/en/business/article/expanded-targeting\" target=\"_blank\">\"expanded targeting\"</a>.. [optional]  # noqa: E501
            placement_group (str): <a href=\"https://developers.pinterest.com/docs/redoc/#section/Placement-group\">Placement group</a>.. [optional]  # noqa: E501
            pacing_delivery_type (str): Pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [

          ],
          'oneOf': [
          ],
        }
