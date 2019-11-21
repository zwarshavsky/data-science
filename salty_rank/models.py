""" Model schema for SQL table classes """

from salty_rank import app, db


class Troll(db.Model):
    troll_name = db.Column(db.String(100), primary_key=True)
    date_created = db.Column(db.Integer)
    salty_rank = db.Column(db.Float, nullable=False)
    salty_comments = db.Column(db.Integer, nullable=False)
    comments_total = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Troll {self.troll_name} -- Salty Ranking {self.salty_rank}"

    def serialize_troll(self):
        """ serialize object to return JSON format """
        return {
            "troll_name" : self.troll_name,
            "date_created" : self.date_created,
            "salty_rank" : self.salty_rank,
            "salty_comments" : self.salty_comments,
            "comments_total" : self.comments_total
        }


class Comments(db.Model):
    comment_uuid = db.Column(db.BigInteger, primary_key=True)
    troll_name = db.Column(db.String(100), db.ForeignKey('troll.troll_name'))
    is_salty = db.Column(db.Integer)
    text = db.Column(db.String(2500))
    date_created = db.Column(db.BigInteger)

    def __repr__(self):
        return f"Troll {self.troll_name} -- Said: {self.text}"

    def serialize_comments(self):
        """ serialize object to return JSON format """
        return {
            "comment_uuid" : self.comment_uuid,
            "troll_name" : self.troll_name,
            "is_salty" : self.is_salty,
            "text" : self.text,
            "date_created" : self.date_created
        }
