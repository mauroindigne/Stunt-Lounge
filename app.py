import os
from flask import Flask
if os.path.exists(:"env.py"):
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hellow world .. again'

if __name__ == '__main__':
    app.run(host=os.enviorn.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)