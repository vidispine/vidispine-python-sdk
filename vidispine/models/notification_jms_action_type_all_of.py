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

class NotificationJmsActionTypeAllOf(object):
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
        'queue': 'str',
        'username': 'str',
        'password': 'str',
        'content_type': 'str',
        'queue_factory': 'str'
    }

    attribute_map = {
        'queue': 'queue',
        'username': 'username',
        'password': 'password',
        'content_type': 'contentType',
        'queue_factory': 'queueFactory'
    }

    def __init__(self, queue=None, username=None, password=None, content_type=None, queue_factory=None):  # noqa: E501
        """NotificationJmsActionTypeAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._queue = None
        self._username = None
        self._password = None
        self._content_type = None
        self._queue_factory = None
        self.discriminator = None

        self.queue = queue
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if content_type is not None:
            self.content_type = content_type
        self.queue_factory = queue_factory

    @property
    def queue(self):
        """Gets the queue of this NotificationJmsActionTypeAllOf.  # noqa: E501


        :return: The queue of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this NotificationJmsActionTypeAllOf.


        :param queue: The queue of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :type: str
        """
        if queue is None:
            raise ValueError("Invalid value for `queue`, must not be `None`")  # noqa: E501

        self._queue = queue

    @property
    def username(self):
        """Gets the username of this NotificationJmsActionTypeAllOf.  # noqa: E501


        :return: The username of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NotificationJmsActionTypeAllOf.


        :param username: The username of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this NotificationJmsActionTypeAllOf.  # noqa: E501


        :return: The password of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NotificationJmsActionTypeAllOf.


        :param password: The password of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def content_type(self):
        """Gets the content_type of this NotificationJmsActionTypeAllOf.  # noqa: E501


        :return: The content_type of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this NotificationJmsActionTypeAllOf.


        :param content_type: The content_type of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def queue_factory(self):
        """Gets the queue_factory of this NotificationJmsActionTypeAllOf.  # noqa: E501


        :return: The queue_factory of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._queue_factory

    @queue_factory.setter
    def queue_factory(self, queue_factory):
        """Sets the queue_factory of this NotificationJmsActionTypeAllOf.


        :param queue_factory: The queue_factory of this NotificationJmsActionTypeAllOf.  # noqa: E501
        :type: str
        """
        if queue_factory is None:
            raise ValueError("Invalid value for `queue_factory`, must not be `None`")  # noqa: E501

        self._queue_factory = queue_factory

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
        if not isinstance(other, NotificationJmsActionTypeAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
