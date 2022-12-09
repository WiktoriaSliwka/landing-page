from flask import Blueprint, render_template, Request, jsonify, url_for
import json
home= Blueprint(__name__, "home")

@home.route('/', methods=['GET'])
def index():
    req = Request.get_json('http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json')
    data=req.content
    return render_template("index.html", data=data)

# @home.route('/')
# def index():
#     return render_template("layouts.html")
