from bottle import Bottle, run
import thread

def main_server():
	app = Bottle()

	@app.route('/hello')
	def hello():
		return "Hello World!"

	run(app, host='0.0.0.0', port=8080)

thread.start_new_thread(main_server, ())

