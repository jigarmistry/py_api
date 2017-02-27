from flask import Blueprint
from db.models import Person

from datetime import datetime

api = Blueprint('api', __name__)


@api.route('/api')
def index():
    return "API Index"


@api.route('/api/user')
def get_user():
    grandma = Person.get(Person.name == 'Grandma')
    print(grandma.name)
    return "User"


@api.route('/api/create')
def create_user():
    a = Person.create(
        name='Grandma', birthday=datetime(1935, 3, 1), is_relative=True)
    print(a)
    return "create"
