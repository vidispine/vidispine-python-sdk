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

class NotificationTypeAction(object):
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
        'sqs': 'NotificationSQSActionType',
        'jms': 'NotificationJmsActionType',
        'javascript': 'NotificationJavaScriptActionType',
        'http': 'NotificationHttpActionType',
        'ejb': 'NotificationEjbActionType'
    }

    attribute_map = {
        'sqs': 'sqs',
        'jms': 'jms',
        'javascript': 'javascript',
        'http': 'http',
        'ejb': 'ejb'
    }

    def __init__(self, sqs=None, jms=None, javascript=None, http=None, ejb=None):  # noqa: E501
        """NotificationTypeAction - a model defined in OpenAPI"""  # noqa: E501

        self._sqs = None
        self._jms = None
        self._javascript = None
        self._http = None
        self._ejb = None
        self.discriminator = None

        if sqs is not None:
            self.sqs = sqs
        if jms is not None:
            self.jms = jms
        if javascript is not None:
            self.javascript = javascript
        if http is not None:
            self.http = http
        if ejb is not None:
            self.ejb = ejb

    @property
    def sqs(self):
        """Gets the sqs of this NotificationTypeAction.  # noqa: E501


        :return: The sqs of this NotificationTypeAction.  # noqa: E501
        :rtype: NotificationSQSActionType
        """
        return self._sqs

    @sqs.setter
    def sqs(self, sqs):
        """Sets the sqs of this NotificationTypeAction.


        :param sqs: The sqs of this NotificationTypeAction.  # noqa: E501
        :type: NotificationSQSActionType
        """

        self._sqs = sqs

    @property
    def jms(self):
        """Gets the jms of this NotificationTypeAction.  # noqa: E501


        :return: The jms of this NotificationTypeAction.  # noqa: E501
        :rtype: NotificationJmsActionType
        """
        return self._jms

    @jms.setter
    def jms(self, jms):
        """Sets the jms of this NotificationTypeAction.


        :param jms: The jms of this NotificationTypeAction.  # noqa: E501
        :type: NotificationJmsActionType
        """

        self._jms = jms

    @property
    def javascript(self):
        """Gets the javascript of this NotificationTypeAction.  # noqa: E501


        :return: The javascript of this NotificationTypeAction.  # noqa: E501
        :rtype: NotificationJavaScriptActionType
        """
        return self._javascript

    @javascript.setter
    def javascript(self, javascript):
        """Sets the javascript of this NotificationTypeAction.


        :param javascript: The javascript of this NotificationTypeAction.  # noqa: E501
        :type: NotificationJavaScriptActionType
        """

        self._javascript = javascript

    @property
    def http(self):
        """Gets the http of this NotificationTypeAction.  # noqa: E501


        :return: The http of this NotificationTypeAction.  # noqa: E501
        :rtype: NotificationHttpActionType
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this NotificationTypeAction.


        :param http: The http of this NotificationTypeAction.  # noqa: E501
        :type: NotificationHttpActionType
        """

        self._http = http

    @property
    def ejb(self):
        """Gets the ejb of this NotificationTypeAction.  # noqa: E501


        :return: The ejb of this NotificationTypeAction.  # noqa: E501
        :rtype: NotificationEjbActionType
        """
        return self._ejb

    @ejb.setter
    def ejb(self, ejb):
        """Sets the ejb of this NotificationTypeAction.


        :param ejb: The ejb of this NotificationTypeAction.  # noqa: E501
        :type: NotificationEjbActionType
        """

        self._ejb = ejb

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
        if not isinstance(other, NotificationTypeAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other