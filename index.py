from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_todo_form.html')

@app.route('/process', methods=['POST'])
def process():
    # title = request.form.get('titleInput')
    # description = request.form.get('descriptionInput')
    # return ("<b style='font-family: Kristen ITC;'>Title: " + title + "  Description: " + description + "<b>")
    # return render_template("display.html", title = title)
    title= request.form['title']
    # descriptionInput = request.form['description']

    if title:
    	return jsonify({'title' : title})

    return jsonify({'error': "Missing data!"})


if __name__ == '__main__':
    app.run(debug=True)