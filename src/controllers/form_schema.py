from flask import Blueprint, request, flash, redirect, url_for
from flask_login import current_user, login_required
from datetime import datetime
from json import dumps

from src.server import db
from src.models import Schema

module = Blueprint('schema',__name__)

@module.route('create',methods=['GET','POST'])
@login_required
def create():
    if request.methods == 'GET':
        return 'form to create the new form'
    else:
        date = datetime.now()
        json_object = dumps({'question 1':'lalalalalala'})

        schema = Schema(user_id=current_user.id,created=date,schema=json_object)

        db.session.add(schema)
        db.session.commit()
        return 'home page'


    
