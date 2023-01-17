import sqlite3
import json
import string
from flask import Flask, request, redirect, url_for, render_template, flash, get_flashed_messages, abort, Response
from flask_restful import Resource, Api, reqparse, request
from database import create_database
from database import get_column_names
from func import search_by_id, if_id_exist, transform, delete_args, post_args
from func import get_by_company_name, get_by_job_title




app = Flask(__name__)
app.secret_key = "RapeManBruh!"

api = Api(app)

create_database()



def abort_if_id_not_exist(id:int):
    e = search_by_id(id)
    if e == []: abort(404, message="id not found")


get_id_pasrse = reqparse.RequestParser()
get_id_pasrse.add_argument("id", type=int, help="id not provided", required=True)


post_pasrse = reqparse.RequestParser()
post_pasrse.add_argument("id", type=int, help="id not provided", required=True)
post_pasrse.add_argument("comapany_name", type=str, help="comapany_name not provided", required=True)
post_pasrse.add_argument("job_title", type=str, help="id not provided", required=True)
post_pasrse.add_argument("salary", type=int, help="salary not provided", required=True)
post_pasrse.add_argument("status", type=str, help="status not provided", required=True)
post_pasrse.add_argument("desc", type=str, help="description not provided", required=True)
post_pasrse.add_argument("email", type=str, help="email not provided", required=True)

delete_pasrse = reqparse.RequestParser()
delete_pasrse.add_argument("id", type=int, help="id not provided", required=True)


class Job(Resource):
    def get(self):
        args = get_id_pasrse.parse_args()
        e = search_by_id(args["id"])
        if e == []: return {'message': "id not found"}, 404
        e = list(e[0])
        result = transform(get_column_names(), e)
        return json.dumps(result, indent=4)


    def post(self):
        args = post_pasrse.parse_args()
        if if_id_exist(args["id"]):return {"message": "id already exist, try another one"}, 209
        else:
            post_args(args)
            return {"status": "Job has been posted"},308

    def delete(self):
        args = delete_pasrse.parse_args()
        if if_id_exist((args["id"])):
            delete_args(args["id"])
            return {"status": "Job has been posted"}, 200
        else: return {"message": "id already exist, try another one"}, 209

class JobFilter(Resource):
    def get(self, type:str, input:str):

        if type == "company":
            result = {}
            for i in range(0, len(get_by_company_name(input))):
                result[i+1] = transform(get_column_names(), get_by_company_name(input)[i])
            if result == {}:
                return {"message": "Job was not found"}, 209
            else:
                return json.dumps(result, indent=4)
        elif type == "jobtitle":
            result = {}
            for i in range(0, len(get_by_job_title(input))):
                result[i+1] = transform(get_column_names(), get_by_job_title(input)[i])
            if result == {}:
                return {"message": "Job was not found"}, 209
            else:
                return json.dumps(result, indent=4)
        else:
            return {"message": "Query is invalid"}


api.add_resource(Job, "/dev/jobs/")
api.add_resource(JobFilter, "/dev/jobs/filter/<string:type>/<string:input>")


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")



@app.route("/search", methods=["POST", "GET"])
def search():
    conn = sqlite3.connect("jobs.sql")
    wis = conn.cursor()


    result = get_by_job_title(request.form.get("search1"))
    print(result)
    #flash(str(request.form.get("search1")))
    flash(result)
    return render_template("index.html")


@app.route("/lookup")
def lookup():
    return render_template("lookup.html")



@app.errorhandler(404)
def error_handler(e):
    return render_template("404.html")





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")