import sqlite3



def create_database():
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()
    wis.execute("CREATE TABLE IF NOT EXISTS jobs(id INTEGER PRIMARY KEY, company_name TEXT, job_title TEXT, job_id INTEGER, salary INTEGER, status TEXT, description TEXT)")
    conn.commit()


def get_column_names():
    names = [i[0] for i in sqlite3.connect("jobs.sql").cursor().execute("SELECT * FROM jobs").description]
    return names



conn = sqlite3.connect("jobs.sql")
wis = conn.cursor()
