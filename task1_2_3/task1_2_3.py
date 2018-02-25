from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('page1.html')

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['inputFile']
	#return(file.filename)
	names = ["a siddique","b siddique","c siddique","haseeb jan","asad","khan"]
	count = 0
	for n in names:
		fl = n.split()
		fname = fl[0]
		lname = "".join(fl[1:])
		if lname == 'siddique':
			count=count+1
			string = " ".join(fl)
			print(string)
	return render_template('page2.html',count = count)

if __name__ == '__main__':
	app.run(debug=True)
