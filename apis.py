# flask apis goes here

# - Get route: /search   - query params: email

from flask import Flask, request
from main_googleverifier_01 import main

app = Flask(__name__)




# from fastapi import FastAPI, HTTPException, Query
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.encoders import jsonable_encoder

# # fastapi instance 
# description = """
# Emails Validation API helps you do awesome stuff. 🚀
# ## API Endpoints

# You will be able to:

# * **View Email Status** (_Name, Email, Image, Status_).
# """
# app = FastAPI(title="Email Validation API Documentation",description=description)

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

#################################################################################################################
                                        # RESTFUL APIS #
#################################################################################################################


@app.route("/search")
def dashboard_data():
    """status for email"""
    email = request.args.get("email")
    response = main(email=email)
    if response:
        return response
    else:
        return {
            "email": email,
            "status": "unknown"
        }
    

if __name__ == "__main__":
    app.run(debug=True)