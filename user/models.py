# This is where we will keep the templates of things to store (or the models)

from flask import Flask, jsonify, request
# For hashing passwords
from passlib.hash import pbkdf2_sha256
# We need to link mongodb (specifically the instance called db)
from app import db
# For generating a unique id for data entries
import uuid


class User:
    """Data on user."""

    def signup(self):
        # The get(<name>) matches the "name" attribute of the html form
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # We want to encrypt the password so we don't store in plain text
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Now save this data into mongodb
        db.users.insert_one(user)


        return jsonify(user), 200
