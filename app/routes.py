from app import app, db
from app.models import Crime
from flask import render_template, request
import simplejson as json
import datetime
import dateparser
import string

categories = ['mugging', 'break-in']


def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None


def sanitize_string(userinput):
    whitelist = string.letters + string.digits + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)


@app.route("/")
def home(error_message=None):
    crimes = Crime.query.all()
    crimes = [crime.as_dict() for crime in crimes]
    crimes = json.dumps(crimes)
    return render_template(
        "home.html",
        crimes=crimes,
        categories=categories,
        error_message=error_message)


@app.route("/add", methods=['POST'])
def add():
    crime_description = request.form.get("userinput")
    crime = Crime(description=crime_description)
    db.session.add(crime)
    db.session.commit()
    return home()


@app.route("/clear")
def clear():
    # db_uri = 'postgres://postgres:postgres@localhost/crimemap'
    # engine = create_engine(db_uri, convert_unicode=True)
    # db.metadata.bind = engine
    # db.metadata.drop_all()
    Crime.query.delete()
    db.session.commit()
    return home()


@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    date = format_date(request.form.get("date"))
    if not date:
        return home("invalid date. Please use yyyy-mm-dd format")
    category = request.form.get("category")
    if category not in categories:
        return home()
    description = sanitize_string(request.form.get("description"))

    crime = Crime(
        latitude=latitude,
        longitude=longitude,
        date=date,
        category=category,
        description=description)
    db.session.add(crime)
    db.session.commit()
    return home()
