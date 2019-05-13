import pymysql.cursors
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    mysqli = pymysql.connect(
        host='bxuqyfegql9xovrcltj5-mysql.services.clever-cloud.com',
        user='uyy9j8kdtdeqsdr8',
        password='C5ESGfjRHJkLSr6vCiBx',
        db='bxuqyfegql9xovrcltj5',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with mysqli.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM tb_mhs"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        mysqli.close()

        if result is None:
            return "Tidak ada data yang ditemukan"
        else:
            return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()