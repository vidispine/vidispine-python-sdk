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

class MXFTimestampType(object):
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
        'hour': 'int',
        'min': 'int',
        'month': 'int',
        'sec': 'int',
        'year': 'int',
        'qmsec': 'int',
        'day': 'int'
    }

    attribute_map = {
        'hour': 'hour',
        'min': 'min',
        'month': 'month',
        'sec': 'sec',
        'year': 'year',
        'qmsec': 'qmsec',
        'day': 'day'
    }

    def __init__(self, hour=None, min=None, month=None, sec=None, year=None, qmsec=None, day=None):  # noqa: E501
        """MXFTimestampType - a model defined in OpenAPI"""  # noqa: E501

        self._hour = None
        self._min = None
        self._month = None
        self._sec = None
        self._year = None
        self._qmsec = None
        self._day = None
        self.discriminator = None

        self.hour = hour
        self.min = min
        self.month = month
        self.sec = sec
        self.year = year
        self.qmsec = qmsec
        self.day = day

    @property
    def hour(self):
        """Gets the hour of this MXFTimestampType.  # noqa: E501


        :return: The hour of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this MXFTimestampType.


        :param hour: The hour of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if hour is None:
            raise ValueError("Invalid value for `hour`, must not be `None`")  # noqa: E501

        self._hour = hour

    @property
    def min(self):
        """Gets the min of this MXFTimestampType.  # noqa: E501


        :return: The min of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this MXFTimestampType.


        :param min: The min of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def month(self):
        """Gets the month of this MXFTimestampType.  # noqa: E501


        :return: The month of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this MXFTimestampType.


        :param month: The month of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if month is None:
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def sec(self):
        """Gets the sec of this MXFTimestampType.  # noqa: E501


        :return: The sec of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._sec

    @sec.setter
    def sec(self, sec):
        """Sets the sec of this MXFTimestampType.


        :param sec: The sec of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if sec is None:
            raise ValueError("Invalid value for `sec`, must not be `None`")  # noqa: E501

        self._sec = sec

    @property
    def year(self):
        """Gets the year of this MXFTimestampType.  # noqa: E501


        :return: The year of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this MXFTimestampType.


        :param year: The year of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def qmsec(self):
        """Gets the qmsec of this MXFTimestampType.  # noqa: E501


        :return: The qmsec of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._qmsec

    @qmsec.setter
    def qmsec(self, qmsec):
        """Sets the qmsec of this MXFTimestampType.


        :param qmsec: The qmsec of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if qmsec is None:
            raise ValueError("Invalid value for `qmsec`, must not be `None`")  # noqa: E501

        self._qmsec = qmsec

    @property
    def day(self):
        """Gets the day of this MXFTimestampType.  # noqa: E501


        :return: The day of this MXFTimestampType.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this MXFTimestampType.


        :param day: The day of this MXFTimestampType.  # noqa: E501
        :type: int
        """
        if day is None:
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

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
        if not isinstance(other, MXFTimestampType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other