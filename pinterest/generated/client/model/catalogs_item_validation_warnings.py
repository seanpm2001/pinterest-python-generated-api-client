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
    from pinterest.generated.client.model.catalogs_item_validation_details import CatalogsItemValidationDetails
    globals()['CatalogsItemValidationDetails'] = CatalogsItemValidationDetails


class CatalogsItemValidationWarnings(ModelNormal):
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
    }

    validations = {
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
            'additional_image_link_length_too_long': (CatalogsItemValidationDetails,),  # noqa: E501
            'additional_image_link_warning': (CatalogsItemValidationDetails,),  # noqa: E501
            'adwords_format_warning': (CatalogsItemValidationDetails,),  # noqa: E501
            'adwords_same_as_link': (CatalogsItemValidationDetails,),  # noqa: E501
            'age_group_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'age_group_normalized': (CatalogsItemValidationDetails,),  # noqa: E501
            'android_deep_link_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'availability_date_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'availability_normalized': (CatalogsItemValidationDetails,),  # noqa: E501
            'condition_normalized': (CatalogsItemValidationDetails,),  # noqa: E501
            'country_does_not_map_to_currency': (CatalogsItemValidationDetails,),  # noqa: E501
            'custom_label_length_too_long': (CatalogsItemValidationDetails,),  # noqa: E501
            'description_length_too_long': (CatalogsItemValidationDetails,),  # noqa: E501
            'duplicate_products': (CatalogsItemValidationDetails,),  # noqa: E501
            'expiration_date_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'gender_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'gender_normalized': (CatalogsItemValidationDetails,),  # noqa: E501
            'image_link_warning': (CatalogsItemValidationDetails,),  # noqa: E501
            'ios_deep_link_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'is_bundle_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'item_additional_image_download_failure': (CatalogsItemValidationDetails,),  # noqa: E501
            'link_format_warning': (CatalogsItemValidationDetails,),  # noqa: E501
            'min_ad_price_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'multipack_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'optional_condition_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'optional_condition_missing': (CatalogsItemValidationDetails,),  # noqa: E501
            'optional_product_category_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'optional_product_category_missing': (CatalogsItemValidationDetails,),  # noqa: E501
            'product_category_depth_warning': (CatalogsItemValidationDetails,),  # noqa: E501
            'product_type_length_too_long': (CatalogsItemValidationDetails,),  # noqa: E501
            'sales_price_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'sale_date_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'shipping_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'shipping_weight_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'size_type_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'size_type_normalized': (CatalogsItemValidationDetails,),  # noqa: E501
            'tax_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
            'title_length_too_long': (CatalogsItemValidationDetails,),  # noqa: E501
            'too_many_additional_image_links': (CatalogsItemValidationDetails,),  # noqa: E501
            'utm_source_auto_corrected': (CatalogsItemValidationDetails,),  # noqa: E501
            'weight_unit_invalid': (CatalogsItemValidationDetails,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_image_link_length_too_long': 'ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG',  # noqa: E501
        'additional_image_link_warning': 'ADDITIONAL_IMAGE_LINK_WARNING',  # noqa: E501
        'adwords_format_warning': 'ADWORDS_FORMAT_WARNING',  # noqa: E501
        'adwords_same_as_link': 'ADWORDS_SAME_AS_LINK',  # noqa: E501
        'age_group_invalid': 'AGE_GROUP_INVALID',  # noqa: E501
        'age_group_normalized': 'AGE_GROUP_NORMALIZED',  # noqa: E501
        'android_deep_link_invalid': 'ANDROID_DEEP_LINK_INVALID',  # noqa: E501
        'availability_date_invalid': 'AVAILABILITY_DATE_INVALID',  # noqa: E501
        'availability_normalized': 'AVAILABILITY_NORMALIZED',  # noqa: E501
        'condition_normalized': 'CONDITION_NORMALIZED',  # noqa: E501
        'country_does_not_map_to_currency': 'COUNTRY_DOES_NOT_MAP_TO_CURRENCY',  # noqa: E501
        'custom_label_length_too_long': 'CUSTOM_LABEL_LENGTH_TOO_LONG',  # noqa: E501
        'description_length_too_long': 'DESCRIPTION_LENGTH_TOO_LONG',  # noqa: E501
        'duplicate_products': 'DUPLICATE_PRODUCTS',  # noqa: E501
        'expiration_date_invalid': 'EXPIRATION_DATE_INVALID',  # noqa: E501
        'gender_invalid': 'GENDER_INVALID',  # noqa: E501
        'gender_normalized': 'GENDER_NORMALIZED',  # noqa: E501
        'image_link_warning': 'IMAGE_LINK_WARNING',  # noqa: E501
        'ios_deep_link_invalid': 'IOS_DEEP_LINK_INVALID',  # noqa: E501
        'is_bundle_invalid': 'IS_BUNDLE_INVALID',  # noqa: E501
        'item_additional_image_download_failure': 'ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE',  # noqa: E501
        'link_format_warning': 'LINK_FORMAT_WARNING',  # noqa: E501
        'min_ad_price_invalid': 'MIN_AD_PRICE_INVALID',  # noqa: E501
        'multipack_invalid': 'MULTIPACK_INVALID',  # noqa: E501
        'optional_condition_invalid': 'OPTIONAL_CONDITION_INVALID',  # noqa: E501
        'optional_condition_missing': 'OPTIONAL_CONDITION_MISSING',  # noqa: E501
        'optional_product_category_invalid': 'OPTIONAL_PRODUCT_CATEGORY_INVALID',  # noqa: E501
        'optional_product_category_missing': 'OPTIONAL_PRODUCT_CATEGORY_MISSING',  # noqa: E501
        'product_category_depth_warning': 'PRODUCT_CATEGORY_DEPTH_WARNING',  # noqa: E501
        'product_type_length_too_long': 'PRODUCT_TYPE_LENGTH_TOO_LONG',  # noqa: E501
        'sales_price_invalid': 'SALES_PRICE_INVALID',  # noqa: E501
        'sale_date_invalid': 'SALE_DATE_INVALID',  # noqa: E501
        'shipping_invalid': 'SHIPPING_INVALID',  # noqa: E501
        'shipping_weight_invalid': 'SHIPPING_WEIGHT_INVALID',  # noqa: E501
        'size_type_invalid': 'SIZE_TYPE_INVALID',  # noqa: E501
        'size_type_normalized': 'SIZE_TYPE_NORMALIZED',  # noqa: E501
        'tax_invalid': 'TAX_INVALID',  # noqa: E501
        'title_length_too_long': 'TITLE_LENGTH_TOO_LONG',  # noqa: E501
        'too_many_additional_image_links': 'TOO_MANY_ADDITIONAL_IMAGE_LINKS',  # noqa: E501
        'utm_source_auto_corrected': 'UTM_SOURCE_AUTO_CORRECTED',  # noqa: E501
        'weight_unit_invalid': 'WEIGHT_UNIT_INVALID',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CatalogsItemValidationWarnings - a model defined in OpenAPI

        Keyword Args:
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
            additional_image_link_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            additional_image_link_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            adwords_format_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            adwords_same_as_link (CatalogsItemValidationDetails): [optional]  # noqa: E501
            age_group_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            age_group_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            android_deep_link_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            availability_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            availability_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            condition_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            country_does_not_map_to_currency (CatalogsItemValidationDetails): [optional]  # noqa: E501
            custom_label_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            description_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            duplicate_products (CatalogsItemValidationDetails): [optional]  # noqa: E501
            expiration_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            gender_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            gender_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            image_link_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            ios_deep_link_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            is_bundle_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            item_additional_image_download_failure (CatalogsItemValidationDetails): [optional]  # noqa: E501
            link_format_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            min_ad_price_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            multipack_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_condition_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_condition_missing (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_product_category_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_product_category_missing (CatalogsItemValidationDetails): [optional]  # noqa: E501
            product_category_depth_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            product_type_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            sales_price_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            sale_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            shipping_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            shipping_weight_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            size_type_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            size_type_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            tax_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            title_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            too_many_additional_image_links (CatalogsItemValidationDetails): [optional]  # noqa: E501
            utm_source_auto_corrected (CatalogsItemValidationDetails): [optional]  # noqa: E501
            weight_unit_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
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
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CatalogsItemValidationWarnings - a model defined in OpenAPI

        Keyword Args:
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
            additional_image_link_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            additional_image_link_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            adwords_format_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            adwords_same_as_link (CatalogsItemValidationDetails): [optional]  # noqa: E501
            age_group_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            age_group_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            android_deep_link_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            availability_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            availability_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            condition_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            country_does_not_map_to_currency (CatalogsItemValidationDetails): [optional]  # noqa: E501
            custom_label_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            description_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            duplicate_products (CatalogsItemValidationDetails): [optional]  # noqa: E501
            expiration_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            gender_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            gender_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            image_link_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            ios_deep_link_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            is_bundle_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            item_additional_image_download_failure (CatalogsItemValidationDetails): [optional]  # noqa: E501
            link_format_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            min_ad_price_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            multipack_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_condition_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_condition_missing (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_product_category_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            optional_product_category_missing (CatalogsItemValidationDetails): [optional]  # noqa: E501
            product_category_depth_warning (CatalogsItemValidationDetails): [optional]  # noqa: E501
            product_type_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            sales_price_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            sale_date_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            shipping_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            shipping_weight_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            size_type_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            size_type_normalized (CatalogsItemValidationDetails): [optional]  # noqa: E501
            tax_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
            title_length_too_long (CatalogsItemValidationDetails): [optional]  # noqa: E501
            too_many_additional_image_links (CatalogsItemValidationDetails): [optional]  # noqa: E501
            utm_source_auto_corrected (CatalogsItemValidationDetails): [optional]  # noqa: E501
            weight_unit_invalid (CatalogsItemValidationDetails): [optional]  # noqa: E501
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

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
