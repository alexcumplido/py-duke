
from flask import Flask
from flask import render_template
from random import choices
import json
import random

app = Flask(__name__)


def random_fruit():
    """Returns random fruit"""
    fruits = ["apple", "banana", "orange", "strawberry", "grape"]

    return choices(fruits)


@app.route("/")
def fruit():
    """Return random fruit"""

    my_fruit = random_fruit()
    return render_template("index.html", title="Random Fruit", fruit=my_fruit)

@app.route("/route-json")
def fruit_json():
    """"Return random fruit in json format"""
    my_fruit = random_fruit()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "fruit": my_fruit
        })
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
