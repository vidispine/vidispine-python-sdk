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

class SlaveType(object):
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
        'request_source_ip': 'str',
        'slave_instance_name': 'str',
        'slave_ip': 'str',
        'slave_mac': 'str',
        'hostname': 'str',
        'last_updated': 'datetime',
        'slave_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'request_source_ip': 'requestSourceIp',
        'slave_instance_name': 'slaveInstanceName',
        'slave_ip': 'slaveIp',
        'slave_mac': 'slaveMac',
        'hostname': 'hostname',
        'last_updated': 'lastUpdated',
        'slave_id': 'slaveId',
        'id': 'Id'
    }

    def __init__(self, request_source_ip=None, slave_instance_name=None, slave_ip=None, slave_mac=None, hostname=None, last_updated=None, slave_id=None, id=None):  # noqa: E501
        """SlaveType - a model defined in OpenAPI"""  # noqa: E501

        self._request_source_ip = None
        self._slave_instance_name = None
        self._slave_ip = None
        self._slave_mac = None
        self._hostname = None
        self._last_updated = None
        self._slave_id = None
        self._id = None
        self.discriminator = None

        if request_source_ip is not None:
            self.request_source_ip = request_source_ip
        if slave_instance_name is not None:
            self.slave_instance_name = slave_instance_name
        self.slave_ip = slave_ip
        self.slave_mac = slave_mac
        if hostname is not None:
            self.hostname = hostname
        self.last_updated = last_updated
        self.slave_id = slave_id
        self.id = id

    @property
    def request_source_ip(self):
        """Gets the request_source_ip of this SlaveType.  # noqa: E501


        :return: The request_source_ip of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._request_source_ip

    @request_source_ip.setter
    def request_source_ip(self, request_source_ip):
        """Sets the request_source_ip of this SlaveType.


        :param request_source_ip: The request_source_ip of this SlaveType.  # noqa: E501
        :type: str
        """

        self._request_source_ip = request_source_ip

    @property
    def slave_instance_name(self):
        """Gets the slave_instance_name of this SlaveType.  # noqa: E501


        :return: The slave_instance_name of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._slave_instance_name

    @slave_instance_name.setter
    def slave_instance_name(self, slave_instance_name):
        """Sets the slave_instance_name of this SlaveType.


        :param slave_instance_name: The slave_instance_name of this SlaveType.  # noqa: E501
        :type: str
        """

        self._slave_instance_name = slave_instance_name

    @property
    def slave_ip(self):
        """Gets the slave_ip of this SlaveType.  # noqa: E501


        :return: The slave_ip of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._slave_ip

    @slave_ip.setter
    def slave_ip(self, slave_ip):
        """Sets the slave_ip of this SlaveType.


        :param slave_ip: The slave_ip of this SlaveType.  # noqa: E501
        :type: str
        """
        if slave_ip is None:
            raise ValueError("Invalid value for `slave_ip`, must not be `None`")  # noqa: E501

        self._slave_ip = slave_ip

    @property
    def slave_mac(self):
        """Gets the slave_mac of this SlaveType.  # noqa: E501


        :return: The slave_mac of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._slave_mac

    @slave_mac.setter
    def slave_mac(self, slave_mac):
        """Sets the slave_mac of this SlaveType.


        :param slave_mac: The slave_mac of this SlaveType.  # noqa: E501
        :type: str
        """
        if slave_mac is None:
            raise ValueError("Invalid value for `slave_mac`, must not be `None`")  # noqa: E501

        self._slave_mac = slave_mac

    @property
    def hostname(self):
        """Gets the hostname of this SlaveType.  # noqa: E501


        :return: The hostname of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SlaveType.


        :param hostname: The hostname of this SlaveType.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def last_updated(self):
        """Gets the last_updated of this SlaveType.  # noqa: E501


        :return: The last_updated of this SlaveType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this SlaveType.


        :param last_updated: The last_updated of this SlaveType.  # noqa: E501
        :type: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def slave_id(self):
        """Gets the slave_id of this SlaveType.  # noqa: E501


        :return: The slave_id of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._slave_id

    @slave_id.setter
    def slave_id(self, slave_id):
        """Sets the slave_id of this SlaveType.


        :param slave_id: The slave_id of this SlaveType.  # noqa: E501
        :type: str
        """
        if slave_id is None:
            raise ValueError("Invalid value for `slave_id`, must not be `None`")  # noqa: E501

        self._slave_id = slave_id

    @property
    def id(self):
        """Gets the id of this SlaveType.  # noqa: E501


        :return: The id of this SlaveType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlaveType.


        :param id: The id of this SlaveType.  # noqa: E501
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
        if not isinstance(other, SlaveType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
