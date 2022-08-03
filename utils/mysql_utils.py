import pandas
import pymysql
import datetime
import sys

sys.path.append('./')
from lottery.settings import BASE_DIR, DATABASES

def write_scrapy_data_to_mysql(file_name='twocolorball.csv', table='dao_twocolorball'):
    df = pandas.read_csv('{}/spider/spider/{}'.format(BASE_DIR, file_name), encoding='utf-8')
    df['data_time'] = df['data_time'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    df['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_from_df(df, table)


def db_connect():
    info = DATABASES['default']
    connection = pymysql.connect(host=info['HOST'],
                                 port=int(info['PORT']),
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

def insert_from_df(df: pandas.DataFrame, tablename, split_row=1000, replace=True):
    columns = df.columns.tolist()
    if replace:
        base_sql = "replace into {} (`{}`) values ".format(tablename, '`,`'.join(columns))
    else:
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


if __name__ == '__main__':
    write_scrapy_data_to_mysql('twocolorballs.csv', 'dao_twocolorball')
    write_scrapy_data_to_mysql('biglotto.csv', 'dao_biglotto')