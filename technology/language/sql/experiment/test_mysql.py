#!/usr/bin/env python3
import datetime
import getopt
import re
import sys
import pymysql
from pymysql import IntegrityError

db = pymysql.connect("localhost", "root", "root", "ep")


def write_users():
    cursor = None
    try:
        cursor = db.cursor()
        for i in range(1, 100000):
            cursor.execute(
                '''INSERT INTO t_user(`name`,`email`)
                   VALUES(%s,%s);
                ''', ('user{}'.format(i), 'user{}@126.com'.format(i)))
        db.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()


def write_groups():
    cursor = None
    try:
        cursor = db.cursor()
        for i in range(1, 100000):
            cursor.execute(
                '''INSERT INTO t_group(`name`,`desc`)
                   VALUES(%s,%s);
                ''', ('group{}'.format(i), 'hello group{}'.format(i)))
        db.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()


def write_groups_user():
    cursor = None
    try:
        cursor = db.cursor()
        for i in range(1, 10000):
            cursor.execute(
                '''
                    INSERT INTO t_group_user(`group_id`,`user_id`) VALUES(%s,%s);
                ''', (i, i))
            cursor.execute(
                '''
                INSERT INTO t_group_user2(`group_id`,`user_id`) VALUES(%s,%s);
                ''', (str(i), str(i)))
        db.commit()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()


if __name__ == '__main__':
    write_groups()
    write_users()
    write_groups_user()
