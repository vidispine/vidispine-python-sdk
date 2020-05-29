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

class ScheduledRequestTypeResponse(object):
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
        'has_body': 'bool',
        'content_type': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'has_body': 'hasBody',
        'content_type': 'contentType',
        'status_code': 'statusCode'
    }

    def __init__(self, has_body=None, content_type=None, status_code=None):  # noqa: E501
        """ScheduledRequestTypeResponse - a model defined in OpenAPI"""  # noqa: E501

        self._has_body = None
        self._content_type = None
        self._status_code = None
        self.discriminator = None

        self.has_body = has_body
        if content_type is not None:
            self.content_type = content_type
        self.status_code = status_code

    @property
    def has_body(self):
        """Gets the has_body of this ScheduledRequestTypeResponse.  # noqa: E501


        :return: The has_body of this ScheduledRequestTypeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_body

    @has_body.setter
    def has_body(self, has_body):
        """Sets the has_body of this ScheduledRequestTypeResponse.


        :param has_body: The has_body of this ScheduledRequestTypeResponse.  # noqa: E501
        :type: bool
        """
        if has_body is None:
            raise ValueError("Invalid value for `has_body`, must not be `None`")  # noqa: E501

        self._has_body = has_body

    @property
    def content_type(self):
        """Gets the content_type of this ScheduledRequestTypeResponse.  # noqa: E501


        :return: The content_type of this ScheduledRequestTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ScheduledRequestTypeResponse.


        :param content_type: The content_type of this ScheduledRequestTypeResponse.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def status_code(self):
        """Gets the status_code of this ScheduledRequestTypeResponse.  # noqa: E501


        :return: The status_code of this ScheduledRequestTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ScheduledRequestTypeResponse.


        :param status_code: The status_code of this ScheduledRequestTypeResponse.  # noqa: E501
        :type: int
        """
        if status_code is None:
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

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
        if not isinstance(other, ScheduledRequestTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other