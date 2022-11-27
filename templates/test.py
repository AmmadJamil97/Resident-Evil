def chatroom():
    #return render_template("login.html")

    rows = db.execute("SELECT username, messages FROM users WHERE username =?", session["user_id"])

    for row in rows:
        row["username"]
        row["messages"]

    return render_template("chatroom.html",rows=rows)

@app.route("/message", methods=["GET", "POST"])
def message():

    if request.method == "POST":

        rows = db.execute("SELECT * from users WHERE id = ?", session["user_id"])

        for row in rows:
            db.execute("INSERT INTO users (message) VALUES(?);", request.form.get("message"))

        for row in rows:
            row["username"]
            row["messages"]


        return render_template("chatroom.html", rows = rows)
    else:
        return render_template("test4.html")