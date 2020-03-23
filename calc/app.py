# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def math_add():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
   
    return f"{add(a, b)}"

@app.route("/sub")
def math_sub():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"{sub(a, b)}"

@app.route("/mult")
def math_mult():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"{mult(a, b)}"

@app.route("/div")
def math_div():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"{div(a, b)}"

# Saw this solution
### PART TWO

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)