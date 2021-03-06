# coding: utf-8

"""
    Vidispine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.x
    Contact: info@vidispine.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from . import *

class VXAStorageType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'path': 'str',
        'create_proxies_storage': 'str',
        'is_collection_storage': 'str',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'path': 'path',
        'create_proxies_storage': 'createProxiesStorage',
        'is_collection_storage': 'isCollectionStorage',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, path=None, create_proxies_storage=None, is_collection_storage=None, name=None, id=None):  # noqa: E501
        """VXAStorageType - a model defined in OpenAPI"""  # noqa: E501

        self._path = None
        self._create_proxies_storage = None
        self._is_collection_storage = None
        self._name = None
        self._id = None
        self.discriminator = None

        self.path = path
        if create_proxies_storage is not None:
            self.create_proxies_storage = create_proxies_storage
        if is_collection_storage is not None:
            self.is_collection_storage = is_collection_storage
        self.name = name
        self.id = id

    @property
    def path(self):
        """Gets the path of this VXAStorageType.  # noqa: E501


        :return: The path of this VXAStorageType.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this VXAStorageType.


        :param path: The path of this VXAStorageType.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def create_proxies_storage(self):
        """Gets the create_proxies_storage of this VXAStorageType.  # noqa: E501


        :return: The create_proxies_storage of this VXAStorageType.  # noqa: E501
        :rtype: str
        """
        return self._create_proxies_storage

    @create_proxies_storage.setter
    def create_proxies_storage(self, create_proxies_storage):
        """Sets the create_proxies_storage of this VXAStorageType.


        :param create_proxies_storage: The create_proxies_storage of this VXAStorageType.  # noqa: E501
        :type: str
        """

        self._create_proxies_storage = create_proxies_storage

    @property
    def is_collection_storage(self):
        """Gets the is_collection_storage of this VXAStorageType.  # noqa: E501


        :return: The is_collection_storage of this VXAStorageType.  # noqa: E501
        :rtype: str
        """
        return self._is_collection_storage

    @is_collection_storage.setter
    def is_collection_storage(self, is_collection_storage):
        """Sets the is_collection_storage of this VXAStorageType.


        :param is_collection_storage: The is_collection_storage of this VXAStorageType.  # noqa: E501
        :type: str
        """

        self._is_collection_storage = is_collection_storage

    @property
    def name(self):
        """Gets the name of this VXAStorageType.  # noqa: E501


        :return: The name of this VXAStorageType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VXAStorageType.


        :param name: The name of this VXAStorageType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this VXAStorageType.  # noqa: E501


        :return: The id of this VXAStorageType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VXAStorageType.


        :param id: The id of this VXAStorageType.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VXAStorageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
