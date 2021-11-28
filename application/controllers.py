
from flask import current_app as app
from flask import request,redirect,render_template
from flask.helpers import url_for

from application.models import *
from datetime import datetime as dt
import json
import requests as r

base="http://172.18.0.13:8080/"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html",flag=False)
    elif request.method=="POST":
        user=request.form["username"]
        pwd=request.form["pass"]
        name=User.query.filter(User.username==user).first()
        if not(name):
            return '<h1>User does not exist</h1><br><a href="/create">Create New Account</a>'
        else:
            if name.password==pwd:
                return redirect(f"/{user}/dashboard")
            else:
                return "<h2>Wrong password entered</h2>"

@app.route("/create",methods=["GET","POST"])
def create():
    if request.method=="GET":
        return render_template("create_account.html")
    elif request.method=="POST":
        user=request.form["username"]
        pwd=request.form["pass"]
        name=request.form["name"]
        exist=User.query.filter(User.username==user).first()
        if exist:
            return '<h1>Username already present please try with a different username</h1><br><a href="/">Go Back</a>'
        name=User(username=user,password=pwd,name=name)
        db.session.add(name)
        db.session.commit()
        return render_template("login.html",flag=True)

@app.route("/tnc",methods=["GET"])
def tnc():
    return '<h4>Sorry I have no terms and conditions. You can go on!!</h4></br><a href="/create">Go Back</a>'

@app.route("/")
def red():
    return redirect("/login")

@app.route("/<string:username>/dashboard",methods=["GET","POST"])
def dashboard(username):
    user_we_want=User.query.filter(User.username==username).first()
    if request.method=="GET":
        return render_template("dashboard.html",user=user_we_want)
    elif request.method=="POST":
        deck_name=request.form["deck_name"]
        new_deck=decks(name=deck_name)
        user_we_want.decks.append(new_deck)
        db.session.add(new_deck)
        db.session.commit()
        return redirect(f"/{username}/dashboard")


@app.route("/<string:username>/<string:deck_id>",methods=["GET","POST"])
def deck_view(username,deck_id):
    if request.method=="GET":
        user_we_want=User.query.filter(User.username==username).first()
        deck_we_want=decks.query.filter(decks.id==deck_id).first()
        return render_template("deck-view.html",deck=deck_we_want,user=user_we_want)
    elif request.method=="POST":
        deck_we_want=decks.query.filter(decks.id==deck_id).first()
        deck_we_want.name=request.form["new_name"]
        db.session.commit()
        return redirect(f"/{username}/{deck_id}")

@app.route("/<string:username>/<string:deck_id>/show")
def real_stuff(username,deck_id):
    user_we_want=User.query.filter(User.username==username).first()
    deck_we_want=decks.query.filter(decks.id==deck_id).first()
    return render_template("card_view.html",user=user_we_want,deck=deck_we_want)

@app.route("/<string:username>/<string:deck_id>/add",methods=["GET","POST"])
def add_card(username,deck_id):
    user_we_want=User.query.filter(User.username==username).first()
    deck_we_want=decks.query.filter(decks.id==deck_id).first()
    if request.method=="GET":
        return render_template("add-new-card.html",user=user_we_want,deck=deck_we_want)
    elif request.method=="POST":
        qstn=request.form["card-qstn"]
        ans=request.form["card-ans"]
        new_card=cards(question=qstn,answer=ans)
        deck_we_want.cards.append(new_card)
        db.session.add(new_card)
        db.session.commit()
    return redirect(f"/{username}/{deck_id}")

@app.route("/<string:username>/<string:deck_id>/delete",methods=["GET"])
def del_deck(username,deck_id):
    deck_we_want=decks.query.filter(decks.id==deck_id).first()
    cards_of_deck=deck_we_want.cards
    db.session.delete(deck_we_want)
    for card in cards_of_deck:
        db.session.delete(card)
    
    db.session.commit()
    return redirect(f"/{username}/dashboard")
