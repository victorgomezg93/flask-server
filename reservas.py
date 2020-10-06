from flask import Flask, request

app = Flask(__name__)

@app.route('/reservation', methods=["POST"])

def reservation():
	print("habemus conexion")
	print(request.form)
	'''try:
		Jsonrecived = request.get_json()
		print("aqui")
	except:
		return "Error on transmited data"
	print("Data recived")'''
	resp = {'data':23}
	return resp

if __name__ == '__main__':
    # app.run(host='127.0.0.1',debug = False,threaded = True,ssl_context='adhoc')
    app.run(host='0.0.0.0',port=9090,debug = False,threaded = True,ssl_context='adhoc')