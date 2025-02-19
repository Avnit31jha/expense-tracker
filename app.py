from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory expense data (in a real application, you'd use a database)
expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']
        expenses.append({'name': name, 'amount': amount, 'category': category})
        return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['GET'])
def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
