import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from flask import Flask, redirect ,request,render_template,jsonify
from flask_bootstrap import Bootstrap
import json
import requests

nc = Flask(__name__)

@nc.route("/")
def check():
    return render_template('sig.html')
    bootstrap = Bootstrap(nc)
@nc.route('/output', methods=['POST'])
def output():
    #json形式でURLを受け取る
    allA = int(request.json['allA'])
    allB = int(request.json['allB'])
    CVA = int(request.json['CVA'])
    CVB = int(request.json['CVB'])
    
    a,b,c,d=chi2_contingency(np.array([[allA,CVA],[allB,CVB]]))
    # a,b,c,d=chi2_contingency(np.array([[400,20],[150,10]]))
    # if b>0.05:
    #     print("有意であるとは言えません")
    # if 0.01<b<0.05:
    #     print("95%有意です")
    # else b<=0.01:
    #     print("99%有意です")

    # return_data = {"result":b}
    return_data = {"result":b}
    return jsonify(ResultSet=json.dumps(return_data))

if __name__ == '__main__':
    nc.run(host="127.0.0.1", port=8080)
