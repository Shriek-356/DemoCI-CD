
from flask import Flask, render_template, request,session, url_for, redirect
from dao import auth_user

app = (Flask(__name__))
app.secret_key = "secret123"

#
# Không phân quyền
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     error = None
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#
#         user = auth_user(username, password)
#         if user:   # đúng username/password
#             session["username"] = user["username"]
#             return redirect(url_for("index"))
#         else:
#             error = "Sai tên đăng nhập hoặc mật khẩu!"
#
#     return render_template("login.html", error=error)
#
#
# @app.route("/")
# def index():
#     if "username" in session:   # nếu đã đăng nhập
#         return render_template("index.html", username=session["username"])
#     return redirect(url_for("login"))









#
# Phân quyền
#
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = auth_user(username, password)
        if user:   # đúng username/password
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for("index"))
        else:
            error = "Sai tên đăng nhập hoặc mật khẩu!"

    return render_template("login.html", error=error)

@app.route("/")
def index():
    if "username" in session:
        if session.get("role") == "admin":
            return render_template("admin.html", username=session["username"])
        else:
            return render_template("index.html", username=session["username"])
    return redirect(url_for("login"))




@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
        with app.app_context():
            app.run(debug=True, host="0.0.0.0", port=5000)