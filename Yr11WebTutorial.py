from bottle import route, run

@route('/hello')
def hello():
    return "What's up my hello!"

run(host='localhost', port=8080, debug=True)