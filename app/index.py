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

    mahasiswa = ""

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
            for data in result:
                mahasiswa += str(data['id'])
                mahasiswa += '\n'
                mahasiswa += str(data['nim'])
                mahasiswa += "\n"
                mahasiswa += data['nama']
                mahasiswa += "\n"

            return render_template("index.html", result=mahasiswa)


if __name__ == "__main__":
    app.run()