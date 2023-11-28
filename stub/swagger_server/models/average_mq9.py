# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AverageMQ9(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, height_id: int=None, co: float=None):  # noqa: E501
        """AverageMQ9 - a model defined in Swagger

        :param height_id: The height_id of this AverageMQ9.  # noqa: E501
        :type height_id: int
        :param co: The co of this AverageMQ9.  # noqa: E501
        :type co: float
        """
        self.swagger_types = {
            'height_id': int,
            'co': float
        }

        self.attribute_map = {
            'height_id': 'heightId',
            'co': 'co'
        }
        self._height_id = height_id
        self._co = co

    @classmethod
    def from_dict(cls, dikt) -> 'AverageMQ9':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AverageMQ9 of this AverageMQ9.  # noqa: E501
        :rtype: AverageMQ9
        """
        return util.deserialize_model(dikt, cls)

    @property
    def height_id(self) -> int:
        """Gets the height_id of this AverageMQ9.


        :return: The height_id of this AverageMQ9.
        :rtype: int
        """
        return self._height_id

    @height_id.setter
    def height_id(self, height_id: int):
        """Sets the height_id of this AverageMQ9.


        :param height_id: The height_id of this AverageMQ9.
        :type height_id: int
        """

        self._height_id = height_id

    @property
    def co(self) -> float:
        """Gets the co of this AverageMQ9.


        :return: The co of this AverageMQ9.
        :rtype: float
        """
        return self._co

    @co.setter
    def co(self, co: float):
        """Sets the co of this AverageMQ9.


        :param co: The co of this AverageMQ9.
        :type co: float
        """

        self._co = co