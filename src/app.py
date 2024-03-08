from flask import Flask , jsonify
from 
import pymysql.cursors

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 databases='python',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection                                 


@app.route('/users', methods=["POST"])
def create():
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (data['email'], data['password']))

        connection.commit()

    return jsonify({
        'message': 'creacion exitosa'
    }), 201


@app.route('/users', methods=["GET"])
def listar():
    connection = connection_mysql()
        
    with connection.cursor() as cursor:

        sql = 'SELECT id, email FROM users'
        cursor.execute(sql)

        result = cursor.fetchall()

        return jsonify({
            'data': result
        }), 200


@app.route('/users', methods=["PUT"])
def update():
    connection = connection_mysql()

    with connection.cursor() as cursor:

        sql = 'UPDATE users SET email = %s WHERE email = %s'
        cursor.execute(sql)

        return jsonify({
            'message': 'datos actualizados'
        }), 200



@app.route('/users', methods=["DELETE"])
def delete():
    connection = connection_mysql()

    with connection.cursor() as cursor:

        sql = 'DELETE FROM user WHERE id =%s'
        cursor.execute(sql)

        return jsonify({
            'message': 'datos eliminados'
        }), 200