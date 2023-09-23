from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    user1 = ''
    user2 = ''
    if request.method=='POST':
        user1 = float(request.form['user1'])
        operation = request.form['operation']
        user2 = float(request.form['user2'])
        
        if operation == "add":
            result = user1 + user2
        elif operation == "sub":
            result = user1 - user2
        elif operation == "div":
            result = user1 / user2
        elif operation == "mul":
            result = user1 * user2
        elif operation == "mod":
            result = user1 % user2
        else:
            return render_template('home.html')
        return render_template('home.html', result=result, user1=user1, operation=operation,user2=user2)

    return render_template('home.html', result=result,user1=user1,user2=user2)

if __name__ == "__main__":
    app.run(debug=True)