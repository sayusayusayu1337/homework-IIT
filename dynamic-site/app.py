"""Простой динамический сайт на Flask: страница генерируется на сервере."""

from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

visits = 0


@app.route("/", methods=["GET", "POST"])
def index():
    global visits
    visits += 1

    name = request.form.get("name", "").strip() if request.method == "POST" else ""
    greeting = f"Привет, {name}!" if name else "Привет, гость!"

    return render_template(
        "index.html",
        greeting=greeting,
        visits=visits,
        server_time=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
