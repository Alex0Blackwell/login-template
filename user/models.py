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

        # Let's check for an existing email address. Then we don't want to add it
        if(db.users.find_one({"email": user['email']})):
            # Send an error message through ajax to main.js (frontend), status code 400 for failure
            return jsonify({"error": "Email address already in use"}), 400

        # Now save this data into mongodb and return user if successful
        if(db.users.insert_one(user))
            return jsonify(user), 200

        # Something went wrong, throw an error
        return jsonify({"Error", "Signup failure"}), 400
