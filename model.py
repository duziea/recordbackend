import datetime as dt


class Record:
    def __init__(self, name, phone,thing,note,time,date,finish):
        self.name = name
        self.phone = phone
        self.thing = thing
        self.note = note
        self.time = time
        self.date = date
        self.finish = finish
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)