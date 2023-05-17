from flask import Blueprint, render_template, redirect, url_for

page = Blueprint('page', __name__)

@page.route('/', methods = ['GET'])
def home():
    return render_template('index.html')