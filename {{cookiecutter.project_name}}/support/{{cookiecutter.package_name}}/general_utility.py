import logging
import time
import math
import pandas as pd
import pyodbc
import os
from {{cookiecutter.package_name}}.config import config

logger = logging.getLogger(__name__)


def convert_size(size_bytes):
    """Converts bytes into proper size.
    
    Parameters
    ---------
    size_bytes : int
        The number of bytes of any memory object.
    
    Returns
    ---------
    str
    """
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def size_of_dataframe(data):
    """Return the size of the dataframe.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataframe in which to return the total size in memory.
    """
    return convert_size(data.memory_usage(deep=True).sum())


def write_parquet(data, path, compression="gzip", index=False):

    try:
        logger.info(f"\n Writing data to {path}.")
        data.to_parquet(path, compression=compression, index=index)
        logger.info(
            f"\n Data saved to: {path} \n Number of Columns: "
            ""
            + str(len(data.columns))
            + """\n Number of Rows: """
            + str(len(data))
            + """\n Total Memory of Dataframe: """
            + str(size_of_dataframe(data))
        )
    except Exception as e:
        logger.error(f"{e}")
        raise


def read_parquet(path):
    try:
        logger.info(f"\n Reading data from {path}.")
        data = pd.read_parquet(path)
        logger.info(
            f"\n Number of Columns: "
            ""
            + str(len(data.columns))
            + """\n Number of Rows: """
            + str(len(data))
            + """\n Total Memory of Dataframe: """
            + str(size_of_dataframe(data))
        )
    except Exception as e:
        logger.error(f"{e}")
        raise
    return data

def odbc_connection(connectioninfo,debug="No"):
    
    from sqlalchemy import create_engine
    import urllib
    
    try:
        logger.info("Trying to connect to ODBC Connection")
        if debug == "Yes":
            logger.info(f"DEBUG ON - ODBC String: {connectioninfo}")
        params = urllib.parse.quote_plus(connectioninfo)
        if debug == "Yes":
            logger.info(f"DEBUG ON - params: {params}")
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        if debug == "Yes":
            logger.info(f"DEBUG ON - engine: {engine}")
        odbc_connection = engine.connect()
    except Exeception as e:
        logger.error(f"{e}")
        raise
    return odbc_connection
        
        
        
        
        
        
        