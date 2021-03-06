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

class NotificationJobTriggerType(object):
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
        'type': 'str',
        'create': 'str',
        'stop': 'str',
        'update': 'str',
        'filter': 'NotificationJobTriggerTypeAllOfFilter',
        'finished': 'str',
        'fail': 'str',
        'content_filters': 'NotificationJobTriggerTypeAllOfContentFilters',
        'placeholder': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'create': 'create',
        'stop': 'stop',
        'update': 'update',
        'filter': 'filter',
        'finished': 'finished',
        'fail': 'fail',
        'content_filters': 'contentFilters',
        'placeholder': 'placeholder'
    }

    def __init__(self, type=None, create=None, stop=None, update=None, filter=None, finished=None, fail=None, content_filters=None, placeholder=None):  # noqa: E501
        """NotificationJobTriggerType - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._create = None
        self._stop = None
        self._update = None
        self._filter = None
        self._finished = None
        self._fail = None
        self._content_filters = None
        self._placeholder = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if create is not None:
            self.create = create
        if stop is not None:
            self.stop = stop
        if update is not None:
            self.update = update
        if filter is not None:
            self.filter = filter
        if finished is not None:
            self.finished = finished
        if fail is not None:
            self.fail = fail
        if content_filters is not None:
            self.content_filters = content_filters
        if placeholder is not None:
            self.placeholder = placeholder

    @property
    def type(self):
        """Gets the type of this NotificationJobTriggerType.  # noqa: E501


        :return: The type of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationJobTriggerType.


        :param type: The type of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def create(self):
        """Gets the create of this NotificationJobTriggerType.  # noqa: E501


        :return: The create of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this NotificationJobTriggerType.


        :param create: The create of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._create = create

    @property
    def stop(self):
        """Gets the stop of this NotificationJobTriggerType.  # noqa: E501


        :return: The stop of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this NotificationJobTriggerType.


        :param stop: The stop of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._stop = stop

    @property
    def update(self):
        """Gets the update of this NotificationJobTriggerType.  # noqa: E501


        :return: The update of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this NotificationJobTriggerType.


        :param update: The update of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._update = update

    @property
    def filter(self):
        """Gets the filter of this NotificationJobTriggerType.  # noqa: E501


        :return: The filter of this NotificationJobTriggerType.  # noqa: E501
        :rtype: NotificationJobTriggerTypeAllOfFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NotificationJobTriggerType.


        :param filter: The filter of this NotificationJobTriggerType.  # noqa: E501
        :type: NotificationJobTriggerTypeAllOfFilter
        """

        self._filter = filter

    @property
    def finished(self):
        """Gets the finished of this NotificationJobTriggerType.  # noqa: E501


        :return: The finished of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this NotificationJobTriggerType.


        :param finished: The finished of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._finished = finished

    @property
    def fail(self):
        """Gets the fail of this NotificationJobTriggerType.  # noqa: E501


        :return: The fail of this NotificationJobTriggerType.  # noqa: E501
        :rtype: str
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this NotificationJobTriggerType.


        :param fail: The fail of this NotificationJobTriggerType.  # noqa: E501
        :type: str
        """

        self._fail = fail

    @property
    def content_filters(self):
        """Gets the content_filters of this NotificationJobTriggerType.  # noqa: E501


        :return: The content_filters of this NotificationJobTriggerType.  # noqa: E501
        :rtype: NotificationJobTriggerTypeAllOfContentFilters
        """
        return self._content_filters

    @content_filters.setter
    def content_filters(self, content_filters):
        """Sets the content_filters of this NotificationJobTriggerType.


        :param content_filters: The content_filters of this NotificationJobTriggerType.  # noqa: E501
        :type: NotificationJobTriggerTypeAllOfContentFilters
        """

        self._content_filters = content_filters

    @property
    def placeholder(self):
        """Gets the placeholder of this NotificationJobTriggerType.  # noqa: E501


        :return: The placeholder of this NotificationJobTriggerType.  # noqa: E501
        :rtype: bool
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this NotificationJobTriggerType.


        :param placeholder: The placeholder of this NotificationJobTriggerType.  # noqa: E501
        :type: bool
        """

        self._placeholder = placeholder

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
        if not isinstance(other, NotificationJobTriggerType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
