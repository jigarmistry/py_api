from flask import Blueprint, render_template, abort

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/site')
def index():
    return "Site Index"