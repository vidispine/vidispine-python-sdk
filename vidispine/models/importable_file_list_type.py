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

class ImportableFileListType(object):
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
        'prefixes': 'FilePrefixType',
        'hits': 'int',
        'element': 'list[ImportableFileType]'
    }

    attribute_map = {
        'prefixes': 'prefixes',
        'hits': 'hits',
        'element': 'element'
    }

    def __init__(self, prefixes=None, hits=None, element=None):  # noqa: E501
        """ImportableFileListType - a model defined in OpenAPI"""  # noqa: E501

        self._prefixes = None
        self._hits = None
        self._element = None
        self.discriminator = None

        if prefixes is not None:
            self.prefixes = prefixes
        if hits is not None:
            self.hits = hits
        if element is not None:
            self.element = element

    @property
    def prefixes(self):
        """Gets the prefixes of this ImportableFileListType.  # noqa: E501


        :return: The prefixes of this ImportableFileListType.  # noqa: E501
        :rtype: FilePrefixType
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """Sets the prefixes of this ImportableFileListType.


        :param prefixes: The prefixes of this ImportableFileListType.  # noqa: E501
        :type: FilePrefixType
        """

        self._prefixes = prefixes

    @property
    def hits(self):
        """Gets the hits of this ImportableFileListType.  # noqa: E501


        :return: The hits of this ImportableFileListType.  # noqa: E501
        :rtype: int
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this ImportableFileListType.


        :param hits: The hits of this ImportableFileListType.  # noqa: E501
        :type: int
        """

        self._hits = hits

    @property
    def element(self):
        """Gets the element of this ImportableFileListType.  # noqa: E501


        :return: The element of this ImportableFileListType.  # noqa: E501
        :rtype: list[ImportableFileType]
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this ImportableFileListType.


        :param element: The element of this ImportableFileListType.  # noqa: E501
        :type: list[ImportableFileType]
        """

        self._element = element

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
        if not isinstance(other, ImportableFileListType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other