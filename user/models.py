# This is where we will keep the templates of things to store (or the models)

# Import all this good stuff from flask
from flask import Flask, jsonify, request, session, redirect
# For hashing passwords
from passlib.hash import pbkdf2_sha256
# We need to link mongodb (specifically the instance called db)
from app import db
# For generating a unique id for data entries
import uuid


class User:
    """Data on user."""

    def start_session(self, user):
        # Start the user session

        # First we don't want to store the password in the session
        del user['password']
        # However, store other information
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200


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

        # Now save this data into mongodb and start user session if successfull
        if(db.users.insert_one(user)):
            # Pass in user method including id, name, email, and password
            return self.start_session(user)

        # Something went wrong, throw an error
        return jsonify({"Error", "Signup failure"}), 400


    # Method for logging in users
    def login(self):
        # Find a user with this email address
        user = db.users.find_one({
            "email": request.form.get("email")
        })


        # If user exists and unencrypted password matches encrypted password
        if(user and pbkdf2_sha256.verify(request.form.get('password'), user['password'])):
            return self.start_session(user)

        # Invalid credentials, send an error code of 401
        return jsonify({"error": "Username or password are incorrect."}), 401



    def signout(self):
        # Clear the session and sign the user out
        session.clear()
        return redirect('/')
