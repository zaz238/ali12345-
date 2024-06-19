from sqlalchemy import Column, String
from . import BASE, SESSION


class Gdrive(BASE):
    __tablename__ = "catgdrive"
    cat = Column(String(50), primary_key=True)

    def __init__(self, cat):
        self.cat = cat


Gdrive.__table__.create(bind=SESSION.get_bind(), checkfirst=True)


def is_folder(folder_id):
    try:
        return SESSION.query(Gdrive).filter(Gdrive.cat == str(folder_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def gparent_id(folder_id):
    adder = SESSION.query(Gdrive).get(folder_id)
    if not adder:
        adder = Gdrive(folder_id)
    SESSION.add(adder)
    SESSION.commit()


def get_parent_id():
    try:
        return SESSION.query(Gdrive).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def rmparent_id(folder_id):
    if note := SESSION.query(Gdrive).filter(Gdrive.cat == folder_id):
        note.delete()
        SESSION.commit()
