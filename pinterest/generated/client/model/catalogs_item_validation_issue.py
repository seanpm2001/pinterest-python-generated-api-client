"""
    Pinterest REST API

    Pinterest's REST API  # noqa: E501

    The version of the OpenAPI document: 5.6.0
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



class CatalogsItemValidationIssue(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG': "ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG",
            'ADDITIONAL_IMAGE_LINK_WARNING': "ADDITIONAL_IMAGE_LINK_WARNING",
            'ADULT_INVALID': "ADULT_INVALID",
            'ADWORDS_FORMAT_INVALID': "ADWORDS_FORMAT_INVALID",
            'ADWORDS_FORMAT_WARNING': "ADWORDS_FORMAT_WARNING",
            'ADWORDS_SAME_AS_LINK': "ADWORDS_SAME_AS_LINK",
            'AGE_GROUP_INVALID': "AGE_GROUP_INVALID",
            'AGE_GROUP_NORMALIZED': "AGE_GROUP_NORMALIZED",
            'ANDROID_DEEP_LINK_INVALID': "ANDROID_DEEP_LINK_INVALID",
            'AVAILABILITY_DATE_INVALID': "AVAILABILITY_DATE_INVALID",
            'AVAILABILITY_INVALID': "AVAILABILITY_INVALID",
            'AVAILABILITY_NORMALIZED': "AVAILABILITY_NORMALIZED",
            'BLOCKLISTED_IMAGE_SIGNATURE': "BLOCKLISTED_IMAGE_SIGNATURE",
            'CONDITION_NORMALIZED': "CONDITION_NORMALIZED",
            'COUNTRY_DOES_NOT_MAP_TO_CURRENCY': "COUNTRY_DOES_NOT_MAP_TO_CURRENCY",
            'CUSTOM_LABEL_LENGTH_TOO_LONG': "CUSTOM_LABEL_LENGTH_TOO_LONG",
            'DESCRIPTION_LENGTH_TOO_LONG': "DESCRIPTION_LENGTH_TOO_LONG",
            'DESCRIPTION_MISSING': "DESCRIPTION_MISSING",
            'DUPLICATE_PRODUCTS': "DUPLICATE_PRODUCTS",
            'EXPIRATION_DATE_INVALID': "EXPIRATION_DATE_INVALID",
            'GENDER_INVALID': "GENDER_INVALID",
            'GENDER_NORMALIZED': "GENDER_NORMALIZED",
            'IMAGE_LINK_INVALID': "IMAGE_LINK_INVALID",
            'IMAGE_LINK_LENGTH_TOO_LONG': "IMAGE_LINK_LENGTH_TOO_LONG",
            'IMAGE_LINK_MISSING': "IMAGE_LINK_MISSING",
            'IMAGE_LINK_WARNING': "IMAGE_LINK_WARNING",
            'INVALID_DOMAIN': "INVALID_DOMAIN",
            'IOS_DEEP_LINK_INVALID': "IOS_DEEP_LINK_INVALID",
            'IS_BUNDLE_INVALID': "IS_BUNDLE_INVALID",
            'ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE': "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE",
            'ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE': "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE",
            'ITEMID_MISSING': "ITEMID_MISSING",
            'LINK_FORMAT_INVALID': "LINK_FORMAT_INVALID",
            'LINK_FORMAT_WARNING': "LINK_FORMAT_WARNING",
            'LINK_LENGTH_TOO_LONG': "LINK_LENGTH_TOO_LONG",
            'MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED': "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED",
            'MIN_AD_PRICE_INVALID': "MIN_AD_PRICE_INVALID",
            'MULTIPACK_INVALID': "MULTIPACK_INVALID",
            'OPTIONAL_CONDITION_INVALID': "OPTIONAL_CONDITION_INVALID",
            'OPTIONAL_CONDITION_MISSING': "OPTIONAL_CONDITION_MISSING",
            'OPTIONAL_PRODUCT_CATEGORY_INVALID': "OPTIONAL_PRODUCT_CATEGORY_INVALID",
            'OPTIONAL_PRODUCT_CATEGORY_MISSING': "OPTIONAL_PRODUCT_CATEGORY_MISSING",
            'PARSE_LINE_ERROR': "PARSE_LINE_ERROR",
            'PINJOIN_CONTENT_UNSAFE': "PINJOIN_CONTENT_UNSAFE",
            'PRICE_MISSING': "PRICE_MISSING",
            'PRODUCT_CATEGORY_DEPTH_WARNING': "PRODUCT_CATEGORY_DEPTH_WARNING",
            'PRODUCT_LINK_MISSING': "PRODUCT_LINK_MISSING",
            'PRODUCT_PRICE_INVALID': "PRODUCT_PRICE_INVALID",
            'PRODUCT_TYPE_LENGTH_TOO_LONG': "PRODUCT_TYPE_LENGTH_TOO_LONG",
            'SALE_DATE_INVALID': "SALE_DATE_INVALID",
            'SALES_PRICE_INVALID': "SALES_PRICE_INVALID",
            'SHIPPING_INVALID': "SHIPPING_INVALID",
            'SHIPPING_WEIGHT_INVALID': "SHIPPING_WEIGHT_INVALID",
            'SIZE_TYPE_INVALID': "SIZE_TYPE_INVALID",
            'SIZE_TYPE_NORMALIZED': "SIZE_TYPE_NORMALIZED",
            'TAX_INVALID': "TAX_INVALID",
            'TITLE_LENGTH_TOO_LONG': "TITLE_LENGTH_TOO_LONG",
            'TITLE_MISSING': "TITLE_MISSING",
            'TOO_MANY_ADDITIONAL_IMAGE_LINKS': "TOO_MANY_ADDITIONAL_IMAGE_LINKS",
            'UTM_SOURCE_AUTO_CORRECTED': "UTM_SOURCE_AUTO_CORRECTED",
            'WEIGHT_UNIT_INVALID': "WEIGHT_UNIT_INVALID",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """CatalogsItemValidationIssue - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG", "ADDITIONAL_IMAGE_LINK_WARNING", "ADULT_INVALID", "ADWORDS_FORMAT_INVALID", "ADWORDS_FORMAT_WARNING", "ADWORDS_SAME_AS_LINK", "AGE_GROUP_INVALID", "AGE_GROUP_NORMALIZED", "ANDROID_DEEP_LINK_INVALID", "AVAILABILITY_DATE_INVALID", "AVAILABILITY_INVALID", "AVAILABILITY_NORMALIZED", "BLOCKLISTED_IMAGE_SIGNATURE", "CONDITION_NORMALIZED", "COUNTRY_DOES_NOT_MAP_TO_CURRENCY", "CUSTOM_LABEL_LENGTH_TOO_LONG", "DESCRIPTION_LENGTH_TOO_LONG", "DESCRIPTION_MISSING", "DUPLICATE_PRODUCTS", "EXPIRATION_DATE_INVALID", "GENDER_INVALID", "GENDER_NORMALIZED", "IMAGE_LINK_INVALID", "IMAGE_LINK_LENGTH_TOO_LONG", "IMAGE_LINK_MISSING", "IMAGE_LINK_WARNING", "INVALID_DOMAIN", "IOS_DEEP_LINK_INVALID", "IS_BUNDLE_INVALID", "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE", "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE", "ITEMID_MISSING", "LINK_FORMAT_INVALID", "LINK_FORMAT_WARNING", "LINK_LENGTH_TOO_LONG", "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED", "MIN_AD_PRICE_INVALID", "MULTIPACK_INVALID", "OPTIONAL_CONDITION_INVALID", "OPTIONAL_CONDITION_MISSING", "OPTIONAL_PRODUCT_CATEGORY_INVALID", "OPTIONAL_PRODUCT_CATEGORY_MISSING", "PARSE_LINE_ERROR", "PINJOIN_CONTENT_UNSAFE", "PRICE_MISSING", "PRODUCT_CATEGORY_DEPTH_WARNING", "PRODUCT_LINK_MISSING", "PRODUCT_PRICE_INVALID", "PRODUCT_TYPE_LENGTH_TOO_LONG", "SALE_DATE_INVALID", "SALES_PRICE_INVALID", "SHIPPING_INVALID", "SHIPPING_WEIGHT_INVALID", "SIZE_TYPE_INVALID", "SIZE_TYPE_NORMALIZED", "TAX_INVALID", "TITLE_LENGTH_TOO_LONG", "TITLE_MISSING", "TOO_MANY_ADDITIONAL_IMAGE_LINKS", "UTM_SOURCE_AUTO_CORRECTED", "WEIGHT_UNIT_INVALID", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG", "ADDITIONAL_IMAGE_LINK_WARNING", "ADULT_INVALID", "ADWORDS_FORMAT_INVALID", "ADWORDS_FORMAT_WARNING", "ADWORDS_SAME_AS_LINK", "AGE_GROUP_INVALID", "AGE_GROUP_NORMALIZED", "ANDROID_DEEP_LINK_INVALID", "AVAILABILITY_DATE_INVALID", "AVAILABILITY_INVALID", "AVAILABILITY_NORMALIZED", "BLOCKLISTED_IMAGE_SIGNATURE", "CONDITION_NORMALIZED", "COUNTRY_DOES_NOT_MAP_TO_CURRENCY", "CUSTOM_LABEL_LENGTH_TOO_LONG", "DESCRIPTION_LENGTH_TOO_LONG", "DESCRIPTION_MISSING", "DUPLICATE_PRODUCTS", "EXPIRATION_DATE_INVALID", "GENDER_INVALID", "GENDER_NORMALIZED", "IMAGE_LINK_INVALID", "IMAGE_LINK_LENGTH_TOO_LONG", "IMAGE_LINK_MISSING", "IMAGE_LINK_WARNING", "INVALID_DOMAIN", "IOS_DEEP_LINK_INVALID", "IS_BUNDLE_INVALID", "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE", "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE", "ITEMID_MISSING", "LINK_FORMAT_INVALID", "LINK_FORMAT_WARNING", "LINK_LENGTH_TOO_LONG", "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED", "MIN_AD_PRICE_INVALID", "MULTIPACK_INVALID", "OPTIONAL_CONDITION_INVALID", "OPTIONAL_CONDITION_MISSING", "OPTIONAL_PRODUCT_CATEGORY_INVALID", "OPTIONAL_PRODUCT_CATEGORY_MISSING", "PARSE_LINE_ERROR", "PINJOIN_CONTENT_UNSAFE", "PRICE_MISSING", "PRODUCT_CATEGORY_DEPTH_WARNING", "PRODUCT_LINK_MISSING", "PRODUCT_PRICE_INVALID", "PRODUCT_TYPE_LENGTH_TOO_LONG", "SALE_DATE_INVALID", "SALES_PRICE_INVALID", "SHIPPING_INVALID", "SHIPPING_WEIGHT_INVALID", "SIZE_TYPE_INVALID", "SIZE_TYPE_NORMALIZED", "TAX_INVALID", "TITLE_LENGTH_TOO_LONG", "TITLE_MISSING", "TOO_MANY_ADDITIONAL_IMAGE_LINKS", "UTM_SOURCE_AUTO_CORRECTED", "WEIGHT_UNIT_INVALID", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """CatalogsItemValidationIssue - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG", "ADDITIONAL_IMAGE_LINK_WARNING", "ADULT_INVALID", "ADWORDS_FORMAT_INVALID", "ADWORDS_FORMAT_WARNING", "ADWORDS_SAME_AS_LINK", "AGE_GROUP_INVALID", "AGE_GROUP_NORMALIZED", "ANDROID_DEEP_LINK_INVALID", "AVAILABILITY_DATE_INVALID", "AVAILABILITY_INVALID", "AVAILABILITY_NORMALIZED", "BLOCKLISTED_IMAGE_SIGNATURE", "CONDITION_NORMALIZED", "COUNTRY_DOES_NOT_MAP_TO_CURRENCY", "CUSTOM_LABEL_LENGTH_TOO_LONG", "DESCRIPTION_LENGTH_TOO_LONG", "DESCRIPTION_MISSING", "DUPLICATE_PRODUCTS", "EXPIRATION_DATE_INVALID", "GENDER_INVALID", "GENDER_NORMALIZED", "IMAGE_LINK_INVALID", "IMAGE_LINK_LENGTH_TOO_LONG", "IMAGE_LINK_MISSING", "IMAGE_LINK_WARNING", "INVALID_DOMAIN", "IOS_DEEP_LINK_INVALID", "IS_BUNDLE_INVALID", "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE", "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE", "ITEMID_MISSING", "LINK_FORMAT_INVALID", "LINK_FORMAT_WARNING", "LINK_LENGTH_TOO_LONG", "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED", "MIN_AD_PRICE_INVALID", "MULTIPACK_INVALID", "OPTIONAL_CONDITION_INVALID", "OPTIONAL_CONDITION_MISSING", "OPTIONAL_PRODUCT_CATEGORY_INVALID", "OPTIONAL_PRODUCT_CATEGORY_MISSING", "PARSE_LINE_ERROR", "PINJOIN_CONTENT_UNSAFE", "PRICE_MISSING", "PRODUCT_CATEGORY_DEPTH_WARNING", "PRODUCT_LINK_MISSING", "PRODUCT_PRICE_INVALID", "PRODUCT_TYPE_LENGTH_TOO_LONG", "SALE_DATE_INVALID", "SALES_PRICE_INVALID", "SHIPPING_INVALID", "SHIPPING_WEIGHT_INVALID", "SIZE_TYPE_INVALID", "SIZE_TYPE_NORMALIZED", "TAX_INVALID", "TITLE_LENGTH_TOO_LONG", "TITLE_MISSING", "TOO_MANY_ADDITIONAL_IMAGE_LINKS", "UTM_SOURCE_AUTO_CORRECTED", "WEIGHT_UNIT_INVALID", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG", "ADDITIONAL_IMAGE_LINK_WARNING", "ADULT_INVALID", "ADWORDS_FORMAT_INVALID", "ADWORDS_FORMAT_WARNING", "ADWORDS_SAME_AS_LINK", "AGE_GROUP_INVALID", "AGE_GROUP_NORMALIZED", "ANDROID_DEEP_LINK_INVALID", "AVAILABILITY_DATE_INVALID", "AVAILABILITY_INVALID", "AVAILABILITY_NORMALIZED", "BLOCKLISTED_IMAGE_SIGNATURE", "CONDITION_NORMALIZED", "COUNTRY_DOES_NOT_MAP_TO_CURRENCY", "CUSTOM_LABEL_LENGTH_TOO_LONG", "DESCRIPTION_LENGTH_TOO_LONG", "DESCRIPTION_MISSING", "DUPLICATE_PRODUCTS", "EXPIRATION_DATE_INVALID", "GENDER_INVALID", "GENDER_NORMALIZED", "IMAGE_LINK_INVALID", "IMAGE_LINK_LENGTH_TOO_LONG", "IMAGE_LINK_MISSING", "IMAGE_LINK_WARNING", "INVALID_DOMAIN", "IOS_DEEP_LINK_INVALID", "IS_BUNDLE_INVALID", "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE", "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE", "ITEMID_MISSING", "LINK_FORMAT_INVALID", "LINK_FORMAT_WARNING", "LINK_LENGTH_TOO_LONG", "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED", "MIN_AD_PRICE_INVALID", "MULTIPACK_INVALID", "OPTIONAL_CONDITION_INVALID", "OPTIONAL_CONDITION_MISSING", "OPTIONAL_PRODUCT_CATEGORY_INVALID", "OPTIONAL_PRODUCT_CATEGORY_MISSING", "PARSE_LINE_ERROR", "PINJOIN_CONTENT_UNSAFE", "PRICE_MISSING", "PRODUCT_CATEGORY_DEPTH_WARNING", "PRODUCT_LINK_MISSING", "PRODUCT_PRICE_INVALID", "PRODUCT_TYPE_LENGTH_TOO_LONG", "SALE_DATE_INVALID", "SALES_PRICE_INVALID", "SHIPPING_INVALID", "SHIPPING_WEIGHT_INVALID", "SIZE_TYPE_INVALID", "SIZE_TYPE_NORMALIZED", "TAX_INVALID", "TITLE_LENGTH_TOO_LONG", "TITLE_MISSING", "TOO_MANY_ADDITIONAL_IMAGE_LINKS", "UTM_SOURCE_AUTO_CORRECTED", "WEIGHT_UNIT_INVALID", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
