# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DustApi(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, height_id: int=None, name: str=None, pm10: float=None, pm25: float=None):  # noqa: E501
        """DustApi - a model defined in Swagger

        :param height_id: The height_id of this DustApi.  # noqa: E501
        :type height_id: int
        :param name: The name of this DustApi.  # noqa: E501
        :type name: str
        :param pm10: The pm10 of this DustApi.  # noqa: E501
        :type pm10: float
        :param pm25: The pm25 of this DustApi.  # noqa: E501
        :type pm25: float
        """
        self.swagger_types = {
            'height_id': int,
            'name': str,
            'pm10': float,
            'pm25': float
        }

        self.attribute_map = {
            'height_id': 'heightId',
            'name': 'name',
            'pm10': 'pm10',
            'pm25': 'pm25'
        }
        self._height_id = height_id
        self._name = name
        self._pm10 = pm10
        self._pm25 = pm25

    @classmethod
    def from_dict(cls, dikt) -> 'DustApi':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DustApi of this DustApi.  # noqa: E501
        :rtype: DustApi
        """
        return util.deserialize_model(dikt, cls)

    @property
    def height_id(self) -> int:
        """Gets the height_id of this DustApi.


        :return: The height_id of this DustApi.
        :rtype: int
        """
        return self._height_id

    @height_id.setter
    def height_id(self, height_id: int):
        """Sets the height_id of this DustApi.


        :param height_id: The height_id of this DustApi.
        :type height_id: int
        """

        self._height_id = height_id

    @property
    def name(self) -> str:
        """Gets the name of this DustApi.


        :return: The name of this DustApi.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DustApi.


        :param name: The name of this DustApi.
        :type name: str
        """

        self._name = name

    @property
    def pm10(self) -> float:
        """Gets the pm10 of this DustApi.


        :return: The pm10 of this DustApi.
        :rtype: float
        """
        return self._pm10

    @pm10.setter
    def pm10(self, pm10: float):
        """Sets the pm10 of this DustApi.


        :param pm10: The pm10 of this DustApi.
        :type pm10: float
        """

        self._pm10 = pm10

    @property
    def pm25(self) -> float:
        """Gets the pm25 of this DustApi.


        :return: The pm25 of this DustApi.
        :rtype: float
        """
        return self._pm25

    @pm25.setter
    def pm25(self, pm25: float):
        """Sets the pm25 of this DustApi.


        :param pm25: The pm25 of this DustApi.
        :type pm25: float
        """

        self._pm25 = pm25
