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

class NotificationType(object):
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
        'action': 'NotificationTypeAction',
        'trigger': 'NotificationTypeTrigger'
    }

    attribute_map = {
        'action': 'action',
        'trigger': 'trigger'
    }

    def __init__(self, action=None, trigger=None):  # noqa: E501
        """NotificationType - a model defined in OpenAPI"""  # noqa: E501

        self._action = None
        self._trigger = None
        self.discriminator = None

        self.action = action
        self.trigger = trigger

    @property
    def action(self):
        """Gets the action of this NotificationType.  # noqa: E501


        :return: The action of this NotificationType.  # noqa: E501
        :rtype: NotificationTypeAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NotificationType.


        :param action: The action of this NotificationType.  # noqa: E501
        :type: NotificationTypeAction
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def trigger(self):
        """Gets the trigger of this NotificationType.  # noqa: E501


        :return: The trigger of this NotificationType.  # noqa: E501
        :rtype: NotificationTypeTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this NotificationType.


        :param trigger: The trigger of this NotificationType.  # noqa: E501
        :type: NotificationTypeTrigger
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger

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
        if not isinstance(other, NotificationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
