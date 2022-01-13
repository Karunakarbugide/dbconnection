import logging
import pandas as pd
import sys
from connection import db_connect
import db_config

logging.basicConfig(filename="logs",
                    filemode='a',
                    format='%(asctime)s %(level)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
"""
 This  code for
  -- connect to source database  and move results in dataframe
  -- connect to target database &  insert data into tables
"""
# Source database infomration
src_db_user = ''
src_db_password = ''
src_oracle_dsn = ''

# Target database information
trg_db_user = ''
trg_db_password = ''
trg_oracle_dsn = ''

# Query for data extraction
sql_query = ''

# connecting to source database & extracting data
try:
    connection = db_connect.connect(src_db_user, src_db_password, src_oracle_dsn)
    conn = connection.cursor()
    logging.info('--------- Connected to Source Database---------')
    source_data = pd.read_sql(sql_query, com=conn)
    conn.close()
    logging.info('{}. of records collected from source system'.format(source_data.index))

except Exception as ex:
    logging.error('Error while  connecting to Source Database', sys.exc_info()[0])



# connecting to target database & insert  data

try:
    connection = db_connect.connect(trg_db_user, trg_db_password, trg_oracle_dsn)
    conn = connection.cursor()
    logging.info('--------- Connected to Target Database---------')

    rows = [tuple(x) for x in source_data.values]

    conn.executemany(''' INSERT INTO table_name (column_name1, column_name2 )
                              VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)''', rows)
    logging.info('data loaded into target database')

    conn.commit()
    conn.close()

except Exception as ex:
    logging.error('Error while  connecting to Source Database', sys.exc_info()[0])





