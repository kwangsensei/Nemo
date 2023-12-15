import connexion
import six

from swagger_server.models.average_mq2 import AverageMQ2  # noqa: E501
from swagger_server.models.average_mq9 import AverageMQ9  # noqa: E501
from swagger_server.models.average_pmapi import AveragePMAPI  # noqa: E501
from swagger_server.models.average_pms7 import AveragePMS7  # noqa: E501
from swagger_server.models.height import Height  # noqa: E501
from swagger_server.models.pmapi import PMAPI  # noqa: E501
from swagger_server.models.pms7 import PMS7  # noqa: E501
from swagger_server import util


def controller_get_height():  # noqa: E501
    """Returns a list of heights.

     # noqa: E501


    :rtype: List[Height]
    """
    return 'do some magic!'


def controller_get_height_co_average(height_id):  # noqa: E501
    """Returns the average collected CO values for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[AverageMQ9]
    """
    return 'do some magic!'


def controller_get_height_details(height_id):  # noqa: E501
    """Returns complete details of the specified height

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: Height
    """
    return 'do some magic!'


def controller_get_height_pm_api_average(height_id):  # noqa: E501
    """Returns the average collected PMs from AQI for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[AveragePMAPI]
    """
    return 'do some magic!'


def controller_get_height_pm_average(height_id):  # noqa: E501
    """Returns the average collected PMs for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[AveragePMS7]
    """
    return 'do some magic!'


def controller_get_height_smoke_average(height_id):  # noqa: E501
    """Returns the average collected Smoke values for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[AverageMQ2]
    """
    return 'do some magic!'


def controller_get_pm_api_in_height(height_id):  # noqa: E501
    """Returns a list of collected PMs from AQI for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[PMAPI]
    """
    return 'do some magic!'


def controller_get_pms_in_height(height_id):  # noqa: E501
    """Returns a list of collected PMs for specific height.

     # noqa: E501

    :param height_id: 
    :type height_id: int

    :rtype: List[PMS7]
    """
    return 'do some magic!'
