from bottle import route, run

@route('/hello')
def hello():
    return "tungtungtungsahur"

run(host='localhost', port=8080, debug=True)