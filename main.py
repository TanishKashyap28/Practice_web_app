from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# 1️⃣ LOGIN PAGE (FIRST PAGE)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("splash"))  # go to animation
        else:
            return "Invalid login ❌"

    return render_template("login.html")


# 2️⃣ ANIMATION PAGE
@app.route("/splash")
def splash():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("splash.html")


# 3️⃣ MAIN APP
@app.route("/explore")
def explore():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("explore.html")


# OTHER PAGES (keep yours)
@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/gaming")
def gaming():
    return render_template("gaming.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)