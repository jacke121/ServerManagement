from flask import request,render_template,redirect,url_for,session
import time
from index import app
import json
import os
import base64
import traceback
from .login import cklogin
pluginsList = ['php','phpmyadmin','nginx','mysql','Pureftpd','Apache','Redis','MariaDB']
@app.route('/plugins',methods=['GET','POST'])
@cklogin()
def plugins():
    return render_template('plugins.html',pluginsList=pluginsList)
