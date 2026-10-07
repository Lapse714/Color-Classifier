from flask import Flask, render_template, request, redirect
from models import db, Mahasiwa

app = Flask (__name__)

db.init_app(app)

with app.app_context():
    db.create_all()

#tampilan home awal
@app.route("/")
def home():
    data = Mahasiwa.query.all()
    
    return render_template("index.html", data=data)

#create
@app.route("/tambah", methods=["POST"])
def tambah():
    npm = request.form['npm']
    nama = request.form['nama']
    kelas = request.form['kelas']
    jurusan = request.form['jurusan']

    mahasiswa_baru = Mahasiwa(
        npm=npm,
        nama=nama,
        kelas=kelas,
        jurusan=jurusan
    )

    db.session.add(mahasiswa_baru)
    db.session.commit()

    return redirect("/")

#DELETE
@app.route("/hapus/<int:id>")
def hapus ():
    data = Mahasiwa.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return redirect("/")

#edit
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    
    data = Mahasiwa.query.get(id)

    if request.method == "POST":

        data.npm = request.form['npm']
        data.nama = request.form['nama']
        data.kelas = request.form['kelas']
        data.jurusan = request.form['jurusan']

      db.session.commit()
    
    return redirect("/")
    return render_template("edit.html", data=data)

app.run(debug=True)