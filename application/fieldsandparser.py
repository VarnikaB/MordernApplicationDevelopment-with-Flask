from operator import attrgetter
from flask_restful import reqparse,fields

deck_parse=reqparse.RequestParser()
deck_parse.add_argument("deck_name")


card_parse=reqparse.RequestParser()
card_parse.add_argument("card_front")
card_parse.add_argument("card_back")


card_fields={
    "card_id": fields.Integer(attribute="id"),
    "card_question": fields.String(attribute="question"),
    "card_answer": fields.String(attribute="answer")
}

deck_fields={
    "deck_id": fields.Integer(attribute="id"),
    "deck_name":fields.String(attribute="name"),
    "deck_cards": fields.List(fields.Nested(card_fields),attribute="cards")
}

deck_lite={
    "deck_id": fields.Integer(attribute="id"),
    "deck_name":fields.String(attribute="name"),
    
}

user_decks={
    "deck_id": fields.Integer(attribute="id"),
    "deck_name":fields.String(attribute="name"),
}


user_fields={
    "username": fields.String,
    "name": fields.String,
    "decks": fields.List(fields.Nested(deck_fields))
}
