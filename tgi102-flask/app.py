from flask import Flask, request, jsonify
import poker as p

app = Flask(
    __name__,
    static_url_path='/resource',
    static_folder='./static2'
)


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


@app.route('/hello_post', methods=["GET", "POST"])
def hello_post():
    output_html = """
    <form action="/hello_post" method="POST">
    <label>What is your name?</label>
    <br>
    <input name="name">
    <button type="submit">SUBMIT</button>
    </form>
    """
    method = request.method  # return "GET" or "POST"
    if method == "GET":
        return output_html
    elif method == "POST":
        name = request.form.get('name')
        output_html += """
        <h1>Hello {}</h1>
        """.format(name)
        return output_html

# /poker?player=5
@app.route('/poker')
def play_poker():
    player = int(request.args.get('player'))
    output_json = p.poker(player)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
