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

class MetadataType(object):
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
        'timespan': 'list[MetadataTypeTimespan]',
        'group': 'list[str]',
        'template': 'str',
        'revision': 'str'
    }

    attribute_map = {
        'timespan': 'timespan',
        'group': 'group',
        'template': 'template',
        'revision': 'revision'
    }

    def __init__(self, timespan=None, group=None, template=None, revision=None):  # noqa: E501
        """MetadataType - a model defined in OpenAPI"""  # noqa: E501

        self._timespan = None
        self._group = None
        self._template = None
        self._revision = None
        self.discriminator = None

        if timespan is not None:
            self.timespan = timespan
        if group is not None:
            self.group = group
        if template is not None:
            self.template = template
        if revision is not None:
            self.revision = revision

    @property
    def timespan(self):
        """Gets the timespan of this MetadataType.  # noqa: E501


        :return: The timespan of this MetadataType.  # noqa: E501
        :rtype: list[MetadataTypeTimespan]
        """
        return self._timespan

    @timespan.setter
    def timespan(self, timespan):
        """Sets the timespan of this MetadataType.


        :param timespan: The timespan of this MetadataType.  # noqa: E501
        :type: list[MetadataTypeTimespan]
        """

        self._timespan = timespan

    @property
    def group(self):
        """Gets the group of this MetadataType.  # noqa: E501


        :return: The group of this MetadataType.  # noqa: E501
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this MetadataType.


        :param group: The group of this MetadataType.  # noqa: E501
        :type: list[str]
        """

        self._group = group

    @property
    def template(self):
        """Gets the template of this MetadataType.  # noqa: E501


        :return: The template of this MetadataType.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this MetadataType.


        :param template: The template of this MetadataType.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def revision(self):
        """Gets the revision of this MetadataType.  # noqa: E501


        :return: The revision of this MetadataType.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this MetadataType.


        :param revision: The revision of this MetadataType.  # noqa: E501
        :type: str
        """

        self._revision = revision

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
        if not isinstance(other, MetadataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other