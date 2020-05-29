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

class VXAVSInstanceType(object):
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
        'status': 'str',
        'vs_cluster_address': 'str',
        'uri': 'str',
        'last_seen': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'vs_cluster_address': 'vsClusterAddress',
        'uri': 'uri',
        'last_seen': 'lastSeen'
    }

    def __init__(self, status=None, vs_cluster_address=None, uri=None, last_seen=None):  # noqa: E501
        """VXAVSInstanceType - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._vs_cluster_address = None
        self._uri = None
        self._last_seen = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if vs_cluster_address is not None:
            self.vs_cluster_address = vs_cluster_address
        if uri is not None:
            self.uri = uri
        if last_seen is not None:
            self.last_seen = last_seen

    @property
    def status(self):
        """Gets the status of this VXAVSInstanceType.  # noqa: E501


        :return: The status of this VXAVSInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VXAVSInstanceType.


        :param status: The status of this VXAVSInstanceType.  # noqa: E501
        :type: str
        """
        allowed_values = ["OFFLINE", "ONLINE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def vs_cluster_address(self):
        """Gets the vs_cluster_address of this VXAVSInstanceType.  # noqa: E501


        :return: The vs_cluster_address of this VXAVSInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._vs_cluster_address

    @vs_cluster_address.setter
    def vs_cluster_address(self, vs_cluster_address):
        """Sets the vs_cluster_address of this VXAVSInstanceType.


        :param vs_cluster_address: The vs_cluster_address of this VXAVSInstanceType.  # noqa: E501
        :type: str
        """

        self._vs_cluster_address = vs_cluster_address

    @property
    def uri(self):
        """Gets the uri of this VXAVSInstanceType.  # noqa: E501


        :return: The uri of this VXAVSInstanceType.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this VXAVSInstanceType.


        :param uri: The uri of this VXAVSInstanceType.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def last_seen(self):
        """Gets the last_seen of this VXAVSInstanceType.  # noqa: E501


        :return: The last_seen of this VXAVSInstanceType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this VXAVSInstanceType.


        :param last_seen: The last_seen of this VXAVSInstanceType.  # noqa: E501
        :type: datetime
        """

        self._last_seen = last_seen

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
        if not isinstance(other, VXAVSInstanceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other