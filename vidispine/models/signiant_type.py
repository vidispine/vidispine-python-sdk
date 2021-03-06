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

class SigniantType(object):
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
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'tag': 'str',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'tag': 'tag',
        'description': 'description'
    }

    def __init__(self, url=None, username=None, password=None, tag=None, description=None):  # noqa: E501
        """SigniantType - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._username = None
        self._password = None
        self._tag = None
        self._description = None
        self.discriminator = None

        self.url = url
        self.username = username
        self.password = password
        self.tag = tag
        if description is not None:
            self.description = description

    @property
    def url(self):
        """Gets the url of this SigniantType.  # noqa: E501


        :return: The url of this SigniantType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SigniantType.


        :param url: The url of this SigniantType.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def username(self):
        """Gets the username of this SigniantType.  # noqa: E501


        :return: The username of this SigniantType.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SigniantType.


        :param username: The username of this SigniantType.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this SigniantType.  # noqa: E501


        :return: The password of this SigniantType.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SigniantType.


        :param password: The password of this SigniantType.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def tag(self):
        """Gets the tag of this SigniantType.  # noqa: E501


        :return: The tag of this SigniantType.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SigniantType.


        :param tag: The tag of this SigniantType.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def description(self):
        """Gets the description of this SigniantType.  # noqa: E501


        :return: The description of this SigniantType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SigniantType.


        :param description: The description of this SigniantType.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, SigniantType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
