# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.average_mq2 import AverageMQ2  # noqa: E501
from swagger_server.models.average_mq9 import AverageMQ9  # noqa: E501
from swagger_server.models.average_pmapi import AveragePMAPI  # noqa: E501
from swagger_server.models.average_pms7 import AveragePMS7  # noqa: E501
from swagger_server.models.height import Height  # noqa: E501
from swagger_server.models.pmapi import PMAPI  # noqa: E501
from swagger_server.models.pms7 import PMS7  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_height(self):
        """Test case for controller_get_height

        Returns a list of heights.
        """
        response = self.client.open(
            '/air_pollution_height//heights',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_co_average(self):
        """Test case for controller_get_height_co_average

        Returns the average collected CO values for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/avgCO'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_details(self):
        """Test case for controller_get_height_details

        Returns complete details of the specified height
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_pm_api_average(self):
        """Test case for controller_get_height_pm_api_average

        Returns the average collected PMs from AQI for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/avgPM_api'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_pm_average(self):
        """Test case for controller_get_height_pm_average

        Returns the average collected PMs for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/avgPM'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_height_smoke_average(self):
        """Test case for controller_get_height_smoke_average

        Returns the average collected Smoke values for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/avgSmoke'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pm_api_in_height(self):
        """Test case for controller_get_pm_api_in_height

        Returns a list of collected PMs from AQI for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/pm_api'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_pms_in_height(self):
        """Test case for controller_get_pms_in_height

        Returns a list of collected PMs for specific height.
        """
        response = self.client.open(
            '/air_pollution_height//heights/{heightId}/pm'.format(height_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
