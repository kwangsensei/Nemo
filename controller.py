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


def get_height_pm_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, AVG(pm10), AVG(pm25)
            FROM pms7
            WHERE height_id=%s
            GROUP BY height_id
            """, (height_id,))
        result = [models.AveragePMS7(height_id=row[0], pm10=row[1], pm25=row[2]) for row in cs.fetchall()]
        return result


def get_pm_api_in_height(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, height_id, name, pm10, pm25
            FROM dust_api
            WHERE height_id=%s
            """, [height_id])
        result = [models.PMAPI(height_id=row[1], name=row[2], pm10=row[3], pm25=row[4]) for row in cs.fetchall()]
        return result
    

def get_height_pm_api_average(height_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT height_id, name, AVG(pm10), AVG(pm25)
            FROM dust_api
            WHERE height_id=%s
            GROUP BY height_id, name
            """, [height_id])
        result = [models.AveragePMAPI(*row) for row in cs.fetchall()]
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
