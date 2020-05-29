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

class NotificationJobTriggerTypeAllOfContentFilters(object):
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
        'content_filter': 'list[str]'
    }

    attribute_map = {
        'content_filter': 'contentFilter'
    }

    def __init__(self, content_filter=None):  # noqa: E501
        """NotificationJobTriggerTypeAllOfContentFilters - a model defined in OpenAPI"""  # noqa: E501

        self._content_filter = None
        self.discriminator = None

        if content_filter is not None:
            self.content_filter = content_filter

    @property
    def content_filter(self):
        """Gets the content_filter of this NotificationJobTriggerTypeAllOfContentFilters.  # noqa: E501


        :return: The content_filter of this NotificationJobTriggerTypeAllOfContentFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._content_filter

    @content_filter.setter
    def content_filter(self, content_filter):
        """Sets the content_filter of this NotificationJobTriggerTypeAllOfContentFilters.


        :param content_filter: The content_filter of this NotificationJobTriggerTypeAllOfContentFilters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["jobId", "jobState", "user", "startTime", "jobType", "jobData", "errorMessage", "itemId", "totalSteps", "currentStep"]  # noqa: E501
        if not set(content_filter).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `content_filter` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(content_filter) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._content_filter = content_filter

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
        if not isinstance(other, NotificationJobTriggerTypeAllOfContentFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other