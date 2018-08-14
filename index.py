from flask import Flask, request, render_template, jsonify, redirect, url_for
import sqlite3

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS todo_tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, status TEXT)")

app = Flask(__name__)

@app.route('/')
def index():

	conn = sqlite3.connect('todo.db')
	c = conn.cursor()

	c.execute('SELECT * FROM todo_tasks')
	todos = c.fetchall()

	return render_template('index.html', todos = todos)

@app.route('/process', methods=['POST'])
def process():

    # title = request.form.get('titleInput')
    # description = request.form.get('descriptionInput')
    # return ("<b style='font-family: Kristen ITC;'>Title: " + title + "  Description: " + description + "<b>")
    # return render_template("display.html", title = title)
	title = request.form['title']
	i = 0

	conn = sqlite3.connect('todo.db')
	c = conn.cursor()

	def get_last_id():
		c.execute("SELECT * FROM todo_tasks")
		result_set = c.fetchall()
		for row in result_set:
		    i = row[0]

		print("Latest id: ", i)
		conn.commit()

		return i

	def enter_data(paramTitle):
		i = get_last_id() + 1

		c.execute('INSERT INTO todo_tasks VALUES(' + str(i) + ', "' + paramTitle + '", 1)')
		conn.commit()

		c.execute('SELECT * FROM todo_tasks')
		todos = c.fetchall()

		return render_template('index.html', todos = todos)

		# return redirect(url_for('index'))
		# return jsonify({'title' : 'TODO task added!'})

	if title:
		enter_data(title)
	else:
		return jsonify({'error': "Missing data!"})


if __name__ == '__main__':
    app.run(debug=True)