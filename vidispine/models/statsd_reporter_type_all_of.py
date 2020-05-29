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

class StatsdReporterTypeAllOf(object):
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
        'host': 'str',
        'prefix': 'str',
        'port': 'int',
        'tags': 'bool'
    }

    attribute_map = {
        'host': 'host',
        'prefix': 'prefix',
        'port': 'port',
        'tags': 'tags'
    }

    def __init__(self, host=None, prefix=None, port=None, tags=None):  # noqa: E501
        """StatsdReporterTypeAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._host = None
        self._prefix = None
        self._port = None
        self._tags = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if prefix is not None:
            self.prefix = prefix
        if port is not None:
            self.port = port
        if tags is not None:
            self.tags = tags

    @property
    def host(self):
        """Gets the host of this StatsdReporterTypeAllOf.  # noqa: E501


        :return: The host of this StatsdReporterTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this StatsdReporterTypeAllOf.


        :param host: The host of this StatsdReporterTypeAllOf.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def prefix(self):
        """Gets the prefix of this StatsdReporterTypeAllOf.  # noqa: E501


        :return: The prefix of this StatsdReporterTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this StatsdReporterTypeAllOf.


        :param prefix: The prefix of this StatsdReporterTypeAllOf.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def port(self):
        """Gets the port of this StatsdReporterTypeAllOf.  # noqa: E501


        :return: The port of this StatsdReporterTypeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this StatsdReporterTypeAllOf.


        :param port: The port of this StatsdReporterTypeAllOf.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def tags(self):
        """Gets the tags of this StatsdReporterTypeAllOf.  # noqa: E501


        :return: The tags of this StatsdReporterTypeAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StatsdReporterTypeAllOf.


        :param tags: The tags of this StatsdReporterTypeAllOf.  # noqa: E501
        :type: bool
        """

        self._tags = tags

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
        if not isinstance(other, StatsdReporterTypeAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
