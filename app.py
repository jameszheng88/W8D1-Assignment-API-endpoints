from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    data = None
    message = None
    if request.method == 'POST':
        city = request.form['cityName']
        data = get_current_weather(city)

        if not data:
            message = "No city found"
    
    elif request.method == 'GET':
        city = request.args.get('cityName')
        if city:
            data = get_current_weather(city)
            
            if not data:
                message = "No city found"

    return render_template('index.html', data=data, message=message)
    

if __name__ == "__main__":
    app.run(debug=True)