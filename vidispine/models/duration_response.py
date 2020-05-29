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

class DurationResponse(object):
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
        'duration': 'DurationType',
        'id': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'id': 'id',
        'uri': 'uri'
    }

    def __init__(self, duration=None, id=None, uri=None):  # noqa: E501
        """DurationResponse - a model defined in OpenAPI"""  # noqa: E501

        self._duration = None
        self._id = None
        self._uri = None
        self.discriminator = None

        self.duration = duration
        self.id = id
        self.uri = uri

    @property
    def duration(self):
        """Gets the duration of this DurationResponse.  # noqa: E501


        :return: The duration of this DurationResponse.  # noqa: E501
        :rtype: DurationType
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DurationResponse.


        :param duration: The duration of this DurationResponse.  # noqa: E501
        :type: DurationType
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def id(self):
        """Gets the id of this DurationResponse.  # noqa: E501


        :return: The id of this DurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DurationResponse.


        :param id: The id of this DurationResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this DurationResponse.  # noqa: E501


        :return: The uri of this DurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DurationResponse.


        :param uri: The uri of this DurationResponse.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, DurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
