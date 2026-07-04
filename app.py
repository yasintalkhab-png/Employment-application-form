from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os


app = Flask(__name__)
CORS(app)


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    conn = sqlite3.connect("employees.db")


    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees(
        first_name,
        last_name,
        national_id,
        birthdate,
        gender,
        email,
        phone,
        website,
        degree,
        newsletter,
        description
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["first_name"],
        data["last_name"],
        data["national_id"],
        data["birthdate"],
        data["gender"],
        data["email"],
        data["phone"],
        data["website"],
        data["degree"],
        data["newsletter"],
        data["description"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "اطلاعات با موفقیت دریافت شد."
    })


@app.route("/employees")
def employees():

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    conn.close()

    html = """
    <h1>لیست متقاضیان</h1>

    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>نام</th>
            <th>نام خانوادگی</th>
            <th>کد ملی</th>
            <th>ایمیل</th>
            <th>تلفن</th>
        </tr>
    """

    for row in rows:
        html += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>{row[6]}</td>
            <td>{row[7]}</td>
        </tr>
        """

    html += "</table>"

    return html


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
