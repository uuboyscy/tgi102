from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1><u>Hello Flask</u></h1>'


@app.route('/hello/<username>')
def hello_someone(username):
    output_html = 'Hello {} !'
    return output_html.format(username)


@app.route('/add/<x>/<y>')
def two_sum(x, y):
    print()
    return str(int(x) + int(y))


@app.route('/auth', methods=['POST'])
def auth():
    return "token"

# @app.route('/emp/<bu_number>/<dep_number>')
# def emp(bu_number, dep_number):
#     sql = """
#     SELECT emp_name, emp_number FROM emp
#     WHERE bu_number='{}' AND dep_number='{}'
#     """.format(bu_number, dep_number)
#     output = conn.execute(sql)
#     return to_json(output)

# /hello_get?name=XXX&age=YYY
@app.route('/hello_get')
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    if name == None:
        return "What's your name?"
    elif age == None:
        return "Hello {}.".format(name)
    else:
        output_html = "Hello {}, you are {} years old."
        return output_html.format(name, age)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
