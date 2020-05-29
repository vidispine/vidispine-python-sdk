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

class EidrType(object):
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
        'user_id': 'str',
        'password': 'str',
        'include': 'list[str]',
        'party_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'user_id': 'userId',
        'password': 'password',
        'include': 'include',
        'party_id': 'partyId'
    }

    def __init__(self, url=None, user_id=None, password=None, include=None, party_id=None):  # noqa: E501
        """EidrType - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._user_id = None
        self._password = None
        self._include = None
        self._party_id = None
        self.discriminator = None

        self.url = url
        if user_id is not None:
            self.user_id = user_id
        if password is not None:
            self.password = password
        if include is not None:
            self.include = include
        if party_id is not None:
            self.party_id = party_id

    @property
    def url(self):
        """Gets the url of this EidrType.  # noqa: E501


        :return: The url of this EidrType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EidrType.


        :param url: The url of this EidrType.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def user_id(self):
        """Gets the user_id of this EidrType.  # noqa: E501


        :return: The user_id of this EidrType.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EidrType.


        :param user_id: The user_id of this EidrType.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def password(self):
        """Gets the password of this EidrType.  # noqa: E501


        :return: The password of this EidrType.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this EidrType.


        :param password: The password of this EidrType.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def include(self):
        """Gets the include of this EidrType.  # noqa: E501


        :return: The include of this EidrType.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this EidrType.


        :param include: The include of this EidrType.  # noqa: E501
        :type: list[str]
        """

        self._include = include

    @property
    def party_id(self):
        """Gets the party_id of this EidrType.  # noqa: E501


        :return: The party_id of this EidrType.  # noqa: E501
        :rtype: str
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        """Sets the party_id of this EidrType.


        :param party_id: The party_id of this EidrType.  # noqa: E501
        :type: str
        """

        self._party_id = party_id

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
        if not isinstance(other, EidrType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other