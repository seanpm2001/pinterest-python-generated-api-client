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


def lazy_import():
    from pinterest.generated.client.model.item_attributes_all_of import ItemAttributesAllOf
    from pinterest.generated.client.model.updatable_item_attributes import UpdatableItemAttributes
    globals()['ItemAttributesAllOf'] = ItemAttributesAllOf
    globals()['UpdatableItemAttributes'] = UpdatableItemAttributes


class ItemAttributes(ModelComposed):
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
        ('image_link',): {
            'min_items': 1,
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
            'additional_image_link': ([str], none_type,),  # noqa: E501
            'image_link': ([str],),  # noqa: E501
            'ad_link': (str, none_type,),  # noqa: E501
            'adult': (bool, none_type,),  # noqa: E501
            'age_group': (str, none_type,),  # noqa: E501
            'availability': (str,),  # noqa: E501
            'average_review_rating': (float, none_type,),  # noqa: E501
            'brand': (str, none_type,),  # noqa: E501
            'checkout_enabled': (bool, none_type,),  # noqa: E501
            'color': (str, none_type,),  # noqa: E501
            'condition': (str, none_type,),  # noqa: E501
            'custom_label_0': (str, none_type,),  # noqa: E501
            'custom_label_1': (str, none_type,),  # noqa: E501
            'custom_label_2': (str, none_type,),  # noqa: E501
            'custom_label_3': (str, none_type,),  # noqa: E501
            'custom_label_4': (str, none_type,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'free_shipping_label': (bool, none_type,),  # noqa: E501
            'free_shipping_limit': (str, none_type,),  # noqa: E501
            'gender': (str, none_type,),  # noqa: E501
            'google_product_category': (str, none_type,),  # noqa: E501
            'gtin': (int, none_type,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'item_group_id': (str, none_type,),  # noqa: E501
            'last_updated_time': (int, none_type,),  # noqa: E501
            'link': (str,),  # noqa: E501
            'material': (str, none_type,),  # noqa: E501
            'min_ad_price': (str, none_type,),  # noqa: E501
            'mobile_link': (str, none_type,),  # noqa: E501
            'mpn': (str, none_type,),  # noqa: E501
            'number_of_ratings': (int, none_type,),  # noqa: E501
            'number_of_reviews': (int, none_type,),  # noqa: E501
            'pattern': (str, none_type,),  # noqa: E501
            'price': (str,),  # noqa: E501
            'product_type': (str, none_type,),  # noqa: E501
            'sale_price': (str, none_type,),  # noqa: E501
            'shipping': (str, none_type,),  # noqa: E501
            'shipping_height': (str, none_type,),  # noqa: E501
            'shipping_weight': (str, none_type,),  # noqa: E501
            'shipping_width': (str, none_type,),  # noqa: E501
            'size': (str, none_type,),  # noqa: E501
            'size_system': (str, none_type,),  # noqa: E501
            'size_type': (str, none_type,),  # noqa: E501
            'tax': (str, none_type,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'variant_names': ([str], none_type,),  # noqa: E501
            'variant_values': ([str], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_image_link': 'additional_image_link',  # noqa: E501
        'image_link': 'image_link',  # noqa: E501
        'ad_link': 'ad_link',  # noqa: E501
        'adult': 'adult',  # noqa: E501
        'age_group': 'age_group',  # noqa: E501
        'availability': 'availability',  # noqa: E501
        'average_review_rating': 'average_review_rating',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'checkout_enabled': 'checkout_enabled',  # noqa: E501
        'color': 'color',  # noqa: E501
        'condition': 'condition',  # noqa: E501
        'custom_label_0': 'custom_label_0',  # noqa: E501
        'custom_label_1': 'custom_label_1',  # noqa: E501
        'custom_label_2': 'custom_label_2',  # noqa: E501
        'custom_label_3': 'custom_label_3',  # noqa: E501
        'custom_label_4': 'custom_label_4',  # noqa: E501
        'description': 'description',  # noqa: E501
        'free_shipping_label': 'free_shipping_label',  # noqa: E501
        'free_shipping_limit': 'free_shipping_limit',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'google_product_category': 'google_product_category',  # noqa: E501
        'gtin': 'gtin',  # noqa: E501
        'id': 'id',  # noqa: E501
        'item_group_id': 'item_group_id',  # noqa: E501
        'last_updated_time': 'last_updated_time',  # noqa: E501
        'link': 'link',  # noqa: E501
        'material': 'material',  # noqa: E501
        'min_ad_price': 'min_ad_price',  # noqa: E501
        'mobile_link': 'mobile_link',  # noqa: E501
        'mpn': 'mpn',  # noqa: E501
        'number_of_ratings': 'number_of_ratings',  # noqa: E501
        'number_of_reviews': 'number_of_reviews',  # noqa: E501
        'pattern': 'pattern',  # noqa: E501
        'price': 'price',  # noqa: E501
        'product_type': 'product_type',  # noqa: E501
        'sale_price': 'sale_price',  # noqa: E501
        'shipping': 'shipping',  # noqa: E501
        'shipping_height': 'shipping_height',  # noqa: E501
        'shipping_weight': 'shipping_weight',  # noqa: E501
        'shipping_width': 'shipping_width',  # noqa: E501
        'size': 'size',  # noqa: E501
        'size_system': 'size_system',  # noqa: E501
        'size_type': 'size_type',  # noqa: E501
        'tax': 'tax',  # noqa: E501
        'title': 'title',  # noqa: E501
        'variant_names': 'variant_names',  # noqa: E501
        'variant_values': 'variant_values',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ItemAttributes - a model defined in OpenAPI

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
            additional_image_link ([str], none_type): <p><= 2000 characters</p> <p>The links to additional images for your product. Up to ten additional images can be used to show a product from different angles or to show different stages. Must begin with http:// or https://.</p>. [optional]  # noqa: E501
            image_link ([str]): <p><= 2000 characters</p> <p>The link to the main product images. Images should be at least 75x75 pixels to avoid errors. Use the additional_image_link field to add more images of your product. The URL of your image_link must be accessible by the Pinterest user-agent, and send the accurate images. Please make sure there are no template or placeholder images at the link. Must start with http:// or https://.</p>. [optional]  # noqa: E501
            ad_link (str, none_type): Allows advertisers to specify a separate URL that can be used to track traffic coming from Pinterest shopping ads. Must send full URL including tracking—do not send tracking parameters only. At this time we do not support impression tracking. Must begin with http:// or https://.. [optional]  # noqa: E501
            adult (bool, none_type): Set this attribute to TRUE if you're submitting items that are considered “adult”. These will not be shown on Pinterest.. [optional]  # noqa: E501
            age_group (str, none_type): The age group to apply a demographic range to the product. Must be one of the following values (upper or lowercased): ‘newborn’, ‘infant’, ‘toddler’, ‘kids’, or ‘adult’.. [optional]  # noqa: E501
            availability (str): The availability of the product. Must be one of the following values (upper or lowercased): ‘in stock’, ‘out of stock’, ‘preorder’.. [optional]  # noqa: E501
            average_review_rating (float, none_type): Average reviews for the item. Can be a number from 1-5.. [optional]  # noqa: E501
            brand (str, none_type): The brand of the product.. [optional]  # noqa: E501
            checkout_enabled (bool, none_type): Set this attribute to FALSE to indicate items that should be excluded from the Pinterest Checkout program. Note, this product is currently being tested and your account must be enrolled. Please contact your Account Manager or contact us for more information.. [optional]  # noqa: E501
            color (str, none_type): The primary color of the product.. [optional]  # noqa: E501
            condition (str, none_type): The condition of the product. Must be one of the following values (upper or lowercased): ‘new’, ‘used’, or ‘refurbished’.. [optional]  # noqa: E501
            custom_label_0 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_1 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_2 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_3 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_4 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            description (str): <p><= 10000 characters</p> <p>The description of the product.</p>. [optional]  # noqa: E501
            free_shipping_label (bool, none_type): The item is free to ship.. [optional]  # noqa: E501
            free_shipping_limit (str, none_type): The minimum order purchase necessary for the customer to get free shipping. Only relevant if free shipping is offered.. [optional]  # noqa: E501
            gender (str, none_type): The gender associated with the product. Must be one of the following values (upper or lowercased): ‘male’, ‘female’, or ‘unisex’.. [optional]  # noqa: E501
            google_product_category (str, none_type): The categorization of the product based on the standardized Google Product Taxonomy. This is a set taxonomy. Both the text values and numeric codes are accepted.. [optional]  # noqa: E501
            gtin (int, none_type): The unique universal product identifier.. [optional]  # noqa: E501
            id (str): <p><= 127 characters</p> <p>The user-created unique ID that represents the product. Only Unicode characters are accepted.</p>. [optional]  # noqa: E501
            item_group_id (str, none_type): <p><= 127 characters</p> <p>The parent ID of the product.</p>. [optional]  # noqa: E501
            last_updated_time (int, none_type): The millisecond timestamp when the item was lastly modified by the merchant.. [optional]  # noqa: E501
            link (str): <p><= 511 characters</p> <p>The landing page for the product.</p>. [optional]  # noqa: E501
            material (str, none_type): The material used to make the product.. [optional]  # noqa: E501
            min_ad_price (str, none_type): The minimum advertised price of the product. It supports the following formats, \"19.99 USD\", \"19.99USD\" and \"19.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            mobile_link (str, none_type): The mobile-optimized version of your landing page. Must begin with http:// or https://.. [optional]  # noqa: E501
            mpn (str, none_type): Manufacturer Part Number are alpha-numeric codes created by the manufacturer of a product to uniquely identify it among all products from the same manufacturer.. [optional]  # noqa: E501
            number_of_ratings (int, none_type): The number of ratings for the item.. [optional]  # noqa: E501
            number_of_reviews (int, none_type): The number of reviews available for the item.. [optional]  # noqa: E501
            pattern (str, none_type): The description of the pattern used for the product.. [optional]  # noqa: E501
            price (str): The price of the product. It supports the following formats, \"24.99 USD\", \"24.99USD\" and \"24.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            product_type (str, none_type): <p><= 1000 characters</p> <p>The categorization of your product based on your custom product taxonomy. Subcategories must be sent separated by “ > “. The > must be wrapped by spaces. We do not recognize any other delimiters such as comma or pipe.</p>. [optional]  # noqa: E501
            sale_price (str, none_type): The discounted price of the product. The sale_price must be lower than the price. It supports the following formats, \"14.99 USD\", \"14.99USD\" and \"14.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            shipping (str, none_type): Shipping consists of one group of up to four elements, country, region, service (all optional) and price (required). All colons, even for blank values, are required.. [optional]  # noqa: E501
            shipping_height (str, none_type): The height of the package needed to ship the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            shipping_weight (str, none_type): The weight of the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            shipping_width (str, none_type): The width of the package needed to ship the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            size (str, none_type): The size of the product.. [optional]  # noqa: E501
            size_system (str, none_type): Indicates the country’s sizing system in which you are submitting your product. Must be one of the following values (upper or lowercased): ‘US’, ‘UK’, ‘EU’, ‘DE’, ‘FR’, ‘JP’, ‘CN’, ‘IT’, ‘BR’, ‘MEX’, or ‘AU’.. [optional]  # noqa: E501
            size_type (str, none_type): Additional description for the size. Must be one of the following values (upper or lowercased): ‘regular’, ‘petite’, ‘plus’, ‘big_and_tall’, or ‘maternity’.. [optional]  # noqa: E501
            tax (str, none_type): Tax consists of one group of up to four elements, country, region, rate (all required) and tax_ship (optional). All colons, even for blank values, are required.. [optional]  # noqa: E501
            title (str): <p><= 500 characters</p> <p>The name of the product.</p>. [optional]  # noqa: E501
            variant_names ([str], none_type): Options for this variant. People will see these options next to your Pin and can select the one they want. List them in the order you want them displayed.. [optional]  # noqa: E501
            variant_values ([str], none_type): Option values for this variant. People will see these options next to your Pin and can select the one they want. List them in the order you want them displayed. The order of the variant values must be consistent with the order of the variant names.. [optional]  # noqa: E501
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
        """ItemAttributes - a model defined in OpenAPI

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
            additional_image_link ([str], none_type): <p><= 2000 characters</p> <p>The links to additional images for your product. Up to ten additional images can be used to show a product from different angles or to show different stages. Must begin with http:// or https://.</p>. [optional]  # noqa: E501
            image_link ([str]): <p><= 2000 characters</p> <p>The link to the main product images. Images should be at least 75x75 pixels to avoid errors. Use the additional_image_link field to add more images of your product. The URL of your image_link must be accessible by the Pinterest user-agent, and send the accurate images. Please make sure there are no template or placeholder images at the link. Must start with http:// or https://.</p>. [optional]  # noqa: E501
            ad_link (str, none_type): Allows advertisers to specify a separate URL that can be used to track traffic coming from Pinterest shopping ads. Must send full URL including tracking—do not send tracking parameters only. At this time we do not support impression tracking. Must begin with http:// or https://.. [optional]  # noqa: E501
            adult (bool, none_type): Set this attribute to TRUE if you're submitting items that are considered “adult”. These will not be shown on Pinterest.. [optional]  # noqa: E501
            age_group (str, none_type): The age group to apply a demographic range to the product. Must be one of the following values (upper or lowercased): ‘newborn’, ‘infant’, ‘toddler’, ‘kids’, or ‘adult’.. [optional]  # noqa: E501
            availability (str): The availability of the product. Must be one of the following values (upper or lowercased): ‘in stock’, ‘out of stock’, ‘preorder’.. [optional]  # noqa: E501
            average_review_rating (float, none_type): Average reviews for the item. Can be a number from 1-5.. [optional]  # noqa: E501
            brand (str, none_type): The brand of the product.. [optional]  # noqa: E501
            checkout_enabled (bool, none_type): Set this attribute to FALSE to indicate items that should be excluded from the Pinterest Checkout program. Note, this product is currently being tested and your account must be enrolled. Please contact your Account Manager or contact us for more information.. [optional]  # noqa: E501
            color (str, none_type): The primary color of the product.. [optional]  # noqa: E501
            condition (str, none_type): The condition of the product. Must be one of the following values (upper or lowercased): ‘new’, ‘used’, or ‘refurbished’.. [optional]  # noqa: E501
            custom_label_0 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_1 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_2 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_3 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            custom_label_4 (str, none_type): <p><= 1000 characters</p> <p>Custom grouping of products.</p>. [optional]  # noqa: E501
            description (str): <p><= 10000 characters</p> <p>The description of the product.</p>. [optional]  # noqa: E501
            free_shipping_label (bool, none_type): The item is free to ship.. [optional]  # noqa: E501
            free_shipping_limit (str, none_type): The minimum order purchase necessary for the customer to get free shipping. Only relevant if free shipping is offered.. [optional]  # noqa: E501
            gender (str, none_type): The gender associated with the product. Must be one of the following values (upper or lowercased): ‘male’, ‘female’, or ‘unisex’.. [optional]  # noqa: E501
            google_product_category (str, none_type): The categorization of the product based on the standardized Google Product Taxonomy. This is a set taxonomy. Both the text values and numeric codes are accepted.. [optional]  # noqa: E501
            gtin (int, none_type): The unique universal product identifier.. [optional]  # noqa: E501
            id (str): <p><= 127 characters</p> <p>The user-created unique ID that represents the product. Only Unicode characters are accepted.</p>. [optional]  # noqa: E501
            item_group_id (str, none_type): <p><= 127 characters</p> <p>The parent ID of the product.</p>. [optional]  # noqa: E501
            last_updated_time (int, none_type): The millisecond timestamp when the item was lastly modified by the merchant.. [optional]  # noqa: E501
            link (str): <p><= 511 characters</p> <p>The landing page for the product.</p>. [optional]  # noqa: E501
            material (str, none_type): The material used to make the product.. [optional]  # noqa: E501
            min_ad_price (str, none_type): The minimum advertised price of the product. It supports the following formats, \"19.99 USD\", \"19.99USD\" and \"19.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            mobile_link (str, none_type): The mobile-optimized version of your landing page. Must begin with http:// or https://.. [optional]  # noqa: E501
            mpn (str, none_type): Manufacturer Part Number are alpha-numeric codes created by the manufacturer of a product to uniquely identify it among all products from the same manufacturer.. [optional]  # noqa: E501
            number_of_ratings (int, none_type): The number of ratings for the item.. [optional]  # noqa: E501
            number_of_reviews (int, none_type): The number of reviews available for the item.. [optional]  # noqa: E501
            pattern (str, none_type): The description of the pattern used for the product.. [optional]  # noqa: E501
            price (str): The price of the product. It supports the following formats, \"24.99 USD\", \"24.99USD\" and \"24.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            product_type (str, none_type): <p><= 1000 characters</p> <p>The categorization of your product based on your custom product taxonomy. Subcategories must be sent separated by “ > “. The > must be wrapped by spaces. We do not recognize any other delimiters such as comma or pipe.</p>. [optional]  # noqa: E501
            sale_price (str, none_type): The discounted price of the product. The sale_price must be lower than the price. It supports the following formats, \"14.99 USD\", \"14.99USD\" and \"14.99\". If the currency is not included, we default to US dollars.. [optional]  # noqa: E501
            shipping (str, none_type): Shipping consists of one group of up to four elements, country, region, service (all optional) and price (required). All colons, even for blank values, are required.. [optional]  # noqa: E501
            shipping_height (str, none_type): The height of the package needed to ship the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            shipping_weight (str, none_type): The weight of the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            shipping_width (str, none_type): The width of the package needed to ship the product. Ensure there is a space between the numeric string and the metric.. [optional]  # noqa: E501
            size (str, none_type): The size of the product.. [optional]  # noqa: E501
            size_system (str, none_type): Indicates the country’s sizing system in which you are submitting your product. Must be one of the following values (upper or lowercased): ‘US’, ‘UK’, ‘EU’, ‘DE’, ‘FR’, ‘JP’, ‘CN’, ‘IT’, ‘BR’, ‘MEX’, or ‘AU’.. [optional]  # noqa: E501
            size_type (str, none_type): Additional description for the size. Must be one of the following values (upper or lowercased): ‘regular’, ‘petite’, ‘plus’, ‘big_and_tall’, or ‘maternity’.. [optional]  # noqa: E501
            tax (str, none_type): Tax consists of one group of up to four elements, country, region, rate (all required) and tax_ship (optional). All colons, even for blank values, are required.. [optional]  # noqa: E501
            title (str): <p><= 500 characters</p> <p>The name of the product.</p>. [optional]  # noqa: E501
            variant_names ([str], none_type): Options for this variant. People will see these options next to your Pin and can select the one they want. List them in the order you want them displayed.. [optional]  # noqa: E501
            variant_values ([str], none_type): Option values for this variant. People will see these options next to your Pin and can select the one they want. List them in the order you want them displayed. The order of the variant values must be consistent with the order of the variant names.. [optional]  # noqa: E501
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
