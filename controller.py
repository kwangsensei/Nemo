import sys
import pymysql
from flask import abort
from swagger_server import models
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME


sys.path.append(OPENAPI_STUB_DIR)

pool = PooledDB(
    creator=pymysql,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWD,
    database=DB_NAME,
    maxconnections=1,
    blocking=True
)


def get_height():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, zone, altitude
            FROM height
        """)
        result = [models.Height(*row) for row in cs.fetchall()]
        return result


def get_height_details(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, zone, altitude
            FROM height
            WHERE height_id=%s
        """, [height_id])
        result = cs.fetchone()
    if result:
        height_id, zone, altitude = result
        return models.Height(*result)
    else:
        abort(404)


def get_pms_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, pm10, pm25
            FROM pms7
            WHERE height_id=%s
            """, [height_id])
        result = [models.PMS7(*row) for row in cs.fetchall()]
        return result


def get_cos_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, co
            FROM mq9
            WHERE height_id=%s
            """, [height_id])
        result = [models.MQ9(*row) for row in cs.fetchall()]
        return result
    

def get_smokes_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, smoke
            FROM mq2
            WHERE height_id=%s
            """, [height_id])
        result = [models.MQ2(*row) for row in cs.fetchall()]
        return result
    

def get_dust_api_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, height_id, name, pm10, pm25
            FROM dust_api
            WHERE height_id=%s
            """, [height_id])
        result = [models.DustApi(*row) for row in cs.fetchall()]
        return result


def get_temp_api_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, height_id, temp
            FROM temp_api
            WHERE height_id=%s
            """, [height_id])
        result = [models.TempApi(*row) for row in cs.fetchall()]
        return result


def get_height_pm_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
            FROM pms7
            WHERE height_id=%s
            GROUP BY height_id
            """, (height_id,))
        result = [models.AveragePMS7(height_id=row[0], pm10=row[1], pm25=row[2]) for row in cs.fetchall()]
        return result


def get_height_co_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, AVG(co)
            FROM mq9
            WHERE height_id=%s
            GROUP BY height_id
            """, [height_id])
        result = [models.AverageMQ9(*row) for row in cs.fetchall()]
        return result


def get_height_smoke_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, AVG(smoke)
            FROM mq2
            WHERE height_id=%s
            GROUP BY height_id
            """, [height_id])
        result = [models.AverageMQ2(*row) for row in cs.fetchall()]
        return result


def get_height_pm_api_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, name, AVG(pm10), AVG(pm25)
            FROM dust_api
            WHERE height_id=%s
            GROUP BY height_id, name
            """, [height_id])
        result = [models.AverageDustApi(*row) for row in cs.fetchall()]
        return result
    

def get_height_temp_api_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, AVG(temp)
            FROM temp_api
            WHERE height_id=%s
            GROUP BY height_id
            """, [height_id])
        result = [models.AverageTempApi(*row) for row in cs.fetchall()]
        return result


# def get_basin_annual_rainfall(basin_id, year):
#     with pool.connection() as conn, conn.cursor() as cs:
#         cs.execute("""
#             SELECT SUM(daily_avg)
#             FROM (
#                 SELECT r.year, r.month, r.day, AVG(r.amount) as daily_avg
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id=s.station_id
#                 INNER JOIN basin b ON b.basin_id=s.basin_id
#                 WHERE b.basin_id=%s AND r.year=%s
#                 GROUP BY r.year, r.month, r.day
#             ) daily_avg
#         """, [basin_id, year])
#         result = cs.fetchone()
#     if result and result[0]:
#         amount = round(result[0], 2)
#         return amount
#     else:
#         abort(404)


# def get_basin_monthly_average(basin_id):
#     with pool.connection() as conn, conn.cursor() as cs:
#         cs.execute("""
#             SELECT month, AVG(monthly_amount)
#             FROM (
#                 SELECT SUM(r.amount) as monthly_amount, month
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id=s.station_id
#                 INNER JOIN basin b ON s.basin_id=b.basin_id
#                 WHERE b.basin_id=%s
#                 GROUP BY r.station_id, month, year
#             ) monthly
#             GROUP BY month
#             ORDER BY month ASC
#             """, [basin_id])
#         months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#         result = [
#             models.MonthlyAverage(months[month-1], month, round(amount, 2))
#             for month, amount in cs.fetchall()
#         ]
#         return result
