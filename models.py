from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mahasiwa(db.model):

    id = db.Column(db.integer, primary_keys=True) 
    npm = db.Column(db.string(20))
    nama = db.Column(db.string(100))
    kelas = db.Column(db.string(20))
    jurusan = db.Column(db.string(100))
    