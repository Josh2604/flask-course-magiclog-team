import unittest

from flask import Flask, render_template, request
from api.app import create_app

app = create_app()

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
