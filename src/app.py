from flask import Flask , jsonify
import pymysql.cursors

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def index():
    list_pers = [
        {'name': 'anderson'},
        {'name': 'andres'},
        {'name': 'rico'},
        {'name': 'niebles'}
    ]

    return jsonify(list_pers)

if __name__ == '__main__':
    app.run(debug=True)

def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 databases='python',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection                                 