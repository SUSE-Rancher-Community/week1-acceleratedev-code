from typing import List
from flask import request, redirect, render_template

from database.database import get_db

def configure_routes(app):

    @app.route('/')
    def index():
        db = get_db()
        res = db.execute(
            "SELECT item FROM shoppinglist"
        ).fetchall()
        shoppinglist = list()
        for item in res:
            shoppinglist.append(tuple(item))
        return render_template('index.html', shoppinglist_formatted=shoppinglist)

    @app.route('/addentry', methods=['POST'])
    def add_value():
        item = request.form['value']
        print("Received entry " + item + ", adding to shopping list...")
        db = get_db()
        db.execute(
            "INSERT INTO shoppinglist (item, quantity) VALUES (?, ?)",
            (item, 1,)
        )
        db.commit()
        return redirect("/", code=302)

    @app.route('/removeentry', methods=['POST'])
    def remove_value():
        item = request.form['value']
        print("Received entry " + item + ", removing from shopping list...")
        db = get_db()
        db.execute(
            "DELETE FROM shoppinglist WHERE item = ?",
            (item,) # change this to (item,) <- the comma is what matters - don't ask me why...
        )
        db.commit()
        return redirect("/", code=302)
