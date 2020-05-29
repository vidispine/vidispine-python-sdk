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

class JobStatusType(object):
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
        'transfer_response': 'list[TransferResponse]',
        'estimated_time_left': 'float',
        'is_running': 'bool',
        'log': 'list[JobLogEntryType]',
        'shape_deduction_response': 'list[ShapeDeductionResponse]',
        'input_progress': 'list[JobInputProgressType]',
        'hash_response': 'list[HashResponse]',
        'request': 'JobRequestChoiceType',
        'aaf_generator_response': 'list[AAFGeneratorResponse]',
        'thumbnail': 'list[ThumbnailInfoType]',
        'status_uri': 'str',
        'is_paused': 'bool',
        'xmp_response': 'list[XMPResponse]',
        'duration_response': 'list[DurationResponse]',
        'progress': 'float',
        'message': 'str',
        'walltime': 'float',
        'id': 'str',
        'exitcode': 'int'
    }

    attribute_map = {
        'transfer_response': 'transferResponse',
        'estimated_time_left': 'estimatedTimeLeft',
        'is_running': 'isRunning',
        'log': 'log',
        'shape_deduction_response': 'shapeDeductionResponse',
        'input_progress': 'inputProgress',
        'hash_response': 'hashResponse',
        'request': 'request',
        'aaf_generator_response': 'aafGeneratorResponse',
        'thumbnail': 'thumbnail',
        'status_uri': 'statusUri',
        'is_paused': 'isPaused',
        'xmp_response': 'xmpResponse',
        'duration_response': 'durationResponse',
        'progress': 'progress',
        'message': 'message',
        'walltime': 'walltime',
        'id': 'id',
        'exitcode': 'exitcode'
    }

    def __init__(self, transfer_response=None, estimated_time_left=None, is_running=None, log=None, shape_deduction_response=None, input_progress=None, hash_response=None, request=None, aaf_generator_response=None, thumbnail=None, status_uri=None, is_paused=None, xmp_response=None, duration_response=None, progress=None, message=None, walltime=None, id=None, exitcode=None):  # noqa: E501
        """JobStatusType - a model defined in OpenAPI"""  # noqa: E501

        self._transfer_response = None
        self._estimated_time_left = None
        self._is_running = None
        self._log = None
        self._shape_deduction_response = None
        self._input_progress = None
        self._hash_response = None
        self._request = None
        self._aaf_generator_response = None
        self._thumbnail = None
        self._status_uri = None
        self._is_paused = None
        self._xmp_response = None
        self._duration_response = None
        self._progress = None
        self._message = None
        self._walltime = None
        self._id = None
        self._exitcode = None
        self.discriminator = None

        if transfer_response is not None:
            self.transfer_response = transfer_response
        if estimated_time_left is not None:
            self.estimated_time_left = estimated_time_left
        self.is_running = is_running
        if log is not None:
            self.log = log
        if shape_deduction_response is not None:
            self.shape_deduction_response = shape_deduction_response
        if input_progress is not None:
            self.input_progress = input_progress
        if hash_response is not None:
            self.hash_response = hash_response
        if request is not None:
            self.request = request
        if aaf_generator_response is not None:
            self.aaf_generator_response = aaf_generator_response
        if thumbnail is not None:
            self.thumbnail = thumbnail
        self.status_uri = status_uri
        self.is_paused = is_paused
        if xmp_response is not None:
            self.xmp_response = xmp_response
        if duration_response is not None:
            self.duration_response = duration_response
        if progress is not None:
            self.progress = progress
        if message is not None:
            self.message = message
        self.walltime = walltime
        self.id = id
        if exitcode is not None:
            self.exitcode = exitcode

    @property
    def transfer_response(self):
        """Gets the transfer_response of this JobStatusType.  # noqa: E501


        :return: The transfer_response of this JobStatusType.  # noqa: E501
        :rtype: list[TransferResponse]
        """
        return self._transfer_response

    @transfer_response.setter
    def transfer_response(self, transfer_response):
        """Sets the transfer_response of this JobStatusType.


        :param transfer_response: The transfer_response of this JobStatusType.  # noqa: E501
        :type: list[TransferResponse]
        """

        self._transfer_response = transfer_response

    @property
    def estimated_time_left(self):
        """Gets the estimated_time_left of this JobStatusType.  # noqa: E501


        :return: The estimated_time_left of this JobStatusType.  # noqa: E501
        :rtype: float
        """
        return self._estimated_time_left

    @estimated_time_left.setter
    def estimated_time_left(self, estimated_time_left):
        """Sets the estimated_time_left of this JobStatusType.


        :param estimated_time_left: The estimated_time_left of this JobStatusType.  # noqa: E501
        :type: float
        """

        self._estimated_time_left = estimated_time_left

    @property
    def is_running(self):
        """Gets the is_running of this JobStatusType.  # noqa: E501


        :return: The is_running of this JobStatusType.  # noqa: E501
        :rtype: bool
        """
        return self._is_running

    @is_running.setter
    def is_running(self, is_running):
        """Sets the is_running of this JobStatusType.


        :param is_running: The is_running of this JobStatusType.  # noqa: E501
        :type: bool
        """
        if is_running is None:
            raise ValueError("Invalid value for `is_running`, must not be `None`")  # noqa: E501

        self._is_running = is_running

    @property
    def log(self):
        """Gets the log of this JobStatusType.  # noqa: E501


        :return: The log of this JobStatusType.  # noqa: E501
        :rtype: list[JobLogEntryType]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this JobStatusType.


        :param log: The log of this JobStatusType.  # noqa: E501
        :type: list[JobLogEntryType]
        """

        self._log = log

    @property
    def shape_deduction_response(self):
        """Gets the shape_deduction_response of this JobStatusType.  # noqa: E501


        :return: The shape_deduction_response of this JobStatusType.  # noqa: E501
        :rtype: list[ShapeDeductionResponse]
        """
        return self._shape_deduction_response

    @shape_deduction_response.setter
    def shape_deduction_response(self, shape_deduction_response):
        """Sets the shape_deduction_response of this JobStatusType.


        :param shape_deduction_response: The shape_deduction_response of this JobStatusType.  # noqa: E501
        :type: list[ShapeDeductionResponse]
        """

        self._shape_deduction_response = shape_deduction_response

    @property
    def input_progress(self):
        """Gets the input_progress of this JobStatusType.  # noqa: E501


        :return: The input_progress of this JobStatusType.  # noqa: E501
        :rtype: list[JobInputProgressType]
        """
        return self._input_progress

    @input_progress.setter
    def input_progress(self, input_progress):
        """Sets the input_progress of this JobStatusType.


        :param input_progress: The input_progress of this JobStatusType.  # noqa: E501
        :type: list[JobInputProgressType]
        """

        self._input_progress = input_progress

    @property
    def hash_response(self):
        """Gets the hash_response of this JobStatusType.  # noqa: E501


        :return: The hash_response of this JobStatusType.  # noqa: E501
        :rtype: list[HashResponse]
        """
        return self._hash_response

    @hash_response.setter
    def hash_response(self, hash_response):
        """Sets the hash_response of this JobStatusType.


        :param hash_response: The hash_response of this JobStatusType.  # noqa: E501
        :type: list[HashResponse]
        """

        self._hash_response = hash_response

    @property
    def request(self):
        """Gets the request of this JobStatusType.  # noqa: E501


        :return: The request of this JobStatusType.  # noqa: E501
        :rtype: JobRequestChoiceType
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this JobStatusType.


        :param request: The request of this JobStatusType.  # noqa: E501
        :type: JobRequestChoiceType
        """

        self._request = request

    @property
    def aaf_generator_response(self):
        """Gets the aaf_generator_response of this JobStatusType.  # noqa: E501


        :return: The aaf_generator_response of this JobStatusType.  # noqa: E501
        :rtype: list[AAFGeneratorResponse]
        """
        return self._aaf_generator_response

    @aaf_generator_response.setter
    def aaf_generator_response(self, aaf_generator_response):
        """Sets the aaf_generator_response of this JobStatusType.


        :param aaf_generator_response: The aaf_generator_response of this JobStatusType.  # noqa: E501
        :type: list[AAFGeneratorResponse]
        """

        self._aaf_generator_response = aaf_generator_response

    @property
    def thumbnail(self):
        """Gets the thumbnail of this JobStatusType.  # noqa: E501


        :return: The thumbnail of this JobStatusType.  # noqa: E501
        :rtype: list[ThumbnailInfoType]
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this JobStatusType.


        :param thumbnail: The thumbnail of this JobStatusType.  # noqa: E501
        :type: list[ThumbnailInfoType]
        """

        self._thumbnail = thumbnail

    @property
    def status_uri(self):
        """Gets the status_uri of this JobStatusType.  # noqa: E501


        :return: The status_uri of this JobStatusType.  # noqa: E501
        :rtype: str
        """
        return self._status_uri

    @status_uri.setter
    def status_uri(self, status_uri):
        """Sets the status_uri of this JobStatusType.


        :param status_uri: The status_uri of this JobStatusType.  # noqa: E501
        :type: str
        """
        if status_uri is None:
            raise ValueError("Invalid value for `status_uri`, must not be `None`")  # noqa: E501

        self._status_uri = status_uri

    @property
    def is_paused(self):
        """Gets the is_paused of this JobStatusType.  # noqa: E501


        :return: The is_paused of this JobStatusType.  # noqa: E501
        :rtype: bool
        """
        return self._is_paused

    @is_paused.setter
    def is_paused(self, is_paused):
        """Sets the is_paused of this JobStatusType.


        :param is_paused: The is_paused of this JobStatusType.  # noqa: E501
        :type: bool
        """
        if is_paused is None:
            raise ValueError("Invalid value for `is_paused`, must not be `None`")  # noqa: E501

        self._is_paused = is_paused

    @property
    def xmp_response(self):
        """Gets the xmp_response of this JobStatusType.  # noqa: E501


        :return: The xmp_response of this JobStatusType.  # noqa: E501
        :rtype: list[XMPResponse]
        """
        return self._xmp_response

    @xmp_response.setter
    def xmp_response(self, xmp_response):
        """Sets the xmp_response of this JobStatusType.


        :param xmp_response: The xmp_response of this JobStatusType.  # noqa: E501
        :type: list[XMPResponse]
        """

        self._xmp_response = xmp_response

    @property
    def duration_response(self):
        """Gets the duration_response of this JobStatusType.  # noqa: E501


        :return: The duration_response of this JobStatusType.  # noqa: E501
        :rtype: list[DurationResponse]
        """
        return self._duration_response

    @duration_response.setter
    def duration_response(self, duration_response):
        """Sets the duration_response of this JobStatusType.


        :param duration_response: The duration_response of this JobStatusType.  # noqa: E501
        :type: list[DurationResponse]
        """

        self._duration_response = duration_response

    @property
    def progress(self):
        """Gets the progress of this JobStatusType.  # noqa: E501


        :return: The progress of this JobStatusType.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobStatusType.


        :param progress: The progress of this JobStatusType.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def message(self):
        """Gets the message of this JobStatusType.  # noqa: E501


        :return: The message of this JobStatusType.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobStatusType.


        :param message: The message of this JobStatusType.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def walltime(self):
        """Gets the walltime of this JobStatusType.  # noqa: E501


        :return: The walltime of this JobStatusType.  # noqa: E501
        :rtype: float
        """
        return self._walltime

    @walltime.setter
    def walltime(self, walltime):
        """Sets the walltime of this JobStatusType.


        :param walltime: The walltime of this JobStatusType.  # noqa: E501
        :type: float
        """
        if walltime is None:
            raise ValueError("Invalid value for `walltime`, must not be `None`")  # noqa: E501

        self._walltime = walltime

    @property
    def id(self):
        """Gets the id of this JobStatusType.  # noqa: E501


        :return: The id of this JobStatusType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobStatusType.


        :param id: The id of this JobStatusType.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search(r'([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/([_A-Za-z]+-)?([A-Za-z_][A-Za-z0-9_]*-|(([A-Za-z_][A-Za-z0-9_]*)?\*))([0-9]{1}[0-9]{0,31})/`")  # noqa: E501

        self._id = id

    @property
    def exitcode(self):
        """Gets the exitcode of this JobStatusType.  # noqa: E501


        :return: The exitcode of this JobStatusType.  # noqa: E501
        :rtype: int
        """
        return self._exitcode

    @exitcode.setter
    def exitcode(self, exitcode):
        """Sets the exitcode of this JobStatusType.


        :param exitcode: The exitcode of this JobStatusType.  # noqa: E501
        :type: int
        """

        self._exitcode = exitcode

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
        if not isinstance(other, JobStatusType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
