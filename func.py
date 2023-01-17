import string
from unittest import result
from flask import abort
import sqlite3
from database import get_column_names




def search_by_id(id:int):
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()

    wis.execute("SELECT * FROM jobs WHERE job_id =?", (id, ))
    return wis.fetchall()


def if_id_exist(id:int):
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    wis.execute("SELECT job_id FROM jobs WHERE job_id =?", (id, ))
    
    if wis.fetchone():return True
    else: return False

def generate_row_id():
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    wis.execute("SELECT * FROM jobs")
    count_id = len(wis.fetchall())
    op_id = count_id + 1
    return op_id


def post_args(args:dict):
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    val = (generate_row_id(), str(args["comapany_name"]).lower(), 
    str(args["job_title"]).lower(), args["id"], args["salary"], str(args["status"]).lower(), 
    args["desc"], args["email"], )
    wis.execute("INSERT INTO jobs VALUES(?,?,?,?,?,?,?,?)", val)
    conn.commit()

def delete_args(id:int):
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()

    wis.execute("DROP * FROM jobs WHERE job_id=?", (id, ))
    conn.commit()



def transform(list1:list, list2:list):
    dic = {}
    for i in range(0, len(list1)): dic[list1[i]] = list2[i]
    return dic



def get_by_company_name(cname:str):
    list1 = []

    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    
    wis.execute("SELECT * FROM jobs")
    
    result = list(wis.fetchall())

    for i in result:
        if (cname.lower()).replace(" ", "") == str(i[1]).replace(" ", ""):
            list1.append(list(i))
    
    return list1

def get_by_job_title(jname:str):
    list1 = []

    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    
    wis.execute("SELECT * FROM jobs")
    
    result = list(wis.fetchall())

    for i in result:
        if (jname.lower()).replace(" ", "") == str(i[2]).replace(" ", ""):
            list1.append(list(i))
    
    return list1
#print(get_by_company_name("dev tech"))







def binary_search(arr, target):
    midpoint = int(len(arr) / 2)
    if arr[midpoint] == target: return target, midpoint
    elif arr[midpoint] < target: return binary_search(arr[midpoint:], target)
    elif arr[midpoint] > target: return binary_search(arr[:midpoint], target)