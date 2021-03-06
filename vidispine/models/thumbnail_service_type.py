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

class ThumbnailServiceType(object):
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
        'last_success': 'datetime',
        'failure_message': 'str',
        'state': 'str',
        'mode': 'str',
        'path': 'str',
        'last_failure': 'datetime'
    }

    attribute_map = {
        'last_success': 'lastSuccess',
        'failure_message': 'failureMessage',
        'state': 'state',
        'mode': 'mode',
        'path': 'path',
        'last_failure': 'lastFailure'
    }

    def __init__(self, last_success=None, failure_message=None, state=None, mode=None, path=None, last_failure=None):  # noqa: E501
        """ThumbnailServiceType - a model defined in OpenAPI"""  # noqa: E501

        self._last_success = None
        self._failure_message = None
        self._state = None
        self._mode = None
        self._path = None
        self._last_failure = None
        self.discriminator = None

        if last_success is not None:
            self.last_success = last_success
        if failure_message is not None:
            self.failure_message = failure_message
        self.state = state
        if mode is not None:
            self.mode = mode
        self.path = path
        if last_failure is not None:
            self.last_failure = last_failure

    @property
    def last_success(self):
        """Gets the last_success of this ThumbnailServiceType.  # noqa: E501


        :return: The last_success of this ThumbnailServiceType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_success

    @last_success.setter
    def last_success(self, last_success):
        """Sets the last_success of this ThumbnailServiceType.


        :param last_success: The last_success of this ThumbnailServiceType.  # noqa: E501
        :type: datetime
        """

        self._last_success = last_success

    @property
    def failure_message(self):
        """Gets the failure_message of this ThumbnailServiceType.  # noqa: E501


        :return: The failure_message of this ThumbnailServiceType.  # noqa: E501
        :rtype: str
        """
        return self._failure_message

    @failure_message.setter
    def failure_message(self, failure_message):
        """Sets the failure_message of this ThumbnailServiceType.


        :param failure_message: The failure_message of this ThumbnailServiceType.  # noqa: E501
        :type: str
        """

        self._failure_message = failure_message

    @property
    def state(self):
        """Gets the state of this ThumbnailServiceType.  # noqa: E501


        :return: The state of this ThumbnailServiceType.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ThumbnailServiceType.


        :param state: The state of this ThumbnailServiceType.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def mode(self):
        """Gets the mode of this ThumbnailServiceType.  # noqa: E501


        :return: The mode of this ThumbnailServiceType.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ThumbnailServiceType.


        :param mode: The mode of this ThumbnailServiceType.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this ThumbnailServiceType.  # noqa: E501


        :return: The path of this ThumbnailServiceType.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ThumbnailServiceType.


        :param path: The path of this ThumbnailServiceType.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def last_failure(self):
        """Gets the last_failure of this ThumbnailServiceType.  # noqa: E501


        :return: The last_failure of this ThumbnailServiceType.  # noqa: E501
        :rtype: datetime
        """
        return self._last_failure

    @last_failure.setter
    def last_failure(self, last_failure):
        """Sets the last_failure of this ThumbnailServiceType.


        :param last_failure: The last_failure of this ThumbnailServiceType.  # noqa: E501
        :type: datetime
        """

        self._last_failure = last_failure

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
        if not isinstance(other, ThumbnailServiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
