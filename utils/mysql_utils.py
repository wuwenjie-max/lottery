import pandas
import pymysql
import datetime

from lottery.settings import BASE_DIR, DATABASES

def write_scrapy_data_to_mysql():
    df = pandas.read_csv('{}/spider/spider/data.csv'.format(BASE_DIR), encoding='utf-8')
    df['data_time'] = df['data_time'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    insert_from_df(df, 'dao_twocolorball')

def db_connect():
    info = DATABASES['default']
    connection = pymysql.connect(host=info['HOST'],
                                 port=info['PORT'],
                                 user=info['USER'],
                                 password=info['PASSWORD'],
                                 database=info['NAME'],
                                 charset="utf8")
    connection.select_db(info['NAME'])
    return connection

def exec_sql(sql):
    conn = db_connect()
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()

def insert_from_df(df: pandas.DataFrame, tablename, split_row=1000):
    columns = df.columns.tolist()
    base_sql = "insert into {} (`{}`) values ".format(tablename, '`,`'.join(columns))
    for index in df.index:
        row = [str(item) if type(item) != datetime else item for item in df.loc[index].tolist()]
        print(type(row[0]))
        if index == 0:
            sql = base_sql + ('("{}")'.format('","'.join(row)))
        else:
            sql = sql + ',("{}")'.format('","'.join(row))
    print(sql)
    exec_sql(sql)


write_scrapy_data_to_mysql()