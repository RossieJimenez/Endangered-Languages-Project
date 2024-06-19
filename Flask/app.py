from flask import Flask, render_template,send_from_directory
 
# @app.route('/')
# def index():
#     return '<img src="/static/images/bar.png" alt="Number of Languages">'



app = Flask(__name__)

# home page route
@app.route('/')
def index():
    return render_template('index.html')

#map page route  
# @app.route('/map')  
# def map():
#     # Code to fetch data and pass to template
#     # return render_template('index.html', data=data)
#     return '<img src="/resources/map" alt="Number of Languages">'

# bar chart page route
@app.route('/bar_chart')
def bar_chart():
    # Code to generate bar chart using pandas and Matplotlib
    # Save the bar chart as an image file
    # Pass the image file path to the template
    image_path = '/static/images/bar.png'
    text = "This bar chart illustrates the number of languages grouped by their level of endangerment. Each bar represents a specific category ranging from 'Vulnerable' to 'Extinct'. This visualization allows us to quickly grasp which categories contain the highest or lowest number of languages."
    return render_template('bar_chart.html', image_path=image_path, text=text)
    # return '<img src="/static/images/bar.png" alt="Number of Languages">'
    # return redirect(url_for('index'))
                           

# if __name__ == '__main__':

@app.route('/pie_chart')
def pie_chart():
    # Code to generate line chart using pandas and Matplotlib
    # Save the line chart as an image file
    # Pass the image file path to the template
    image_path = '/static/images/pie.png'
    text = "This pie chart provides a visual representation of the distribution of languages across different levels of endangerment. Each segment of the pie represents a specific level of endangerment, such as 'Vulnerable,' 'Definitely Endangered,' 'Severely Endangered,' 'Critically Endangered,' or 'Extinct.' The size of each segment corresponds to the percentage of languages falling into that category."
    return render_template('bar_chart.html', image_path=image_path, text=text)


@app.route('/avg_speakers')
def donut_chart():
    # Code to generate line chart using pandas and Matplotlib
    # Save the line chart as an image file
    # Pass the image file path to the template
    image_path = '/static/images/avg_speakers.png'
    text = "This donut chart provides insights into the distribution of average speakers across different levels of language endangerment.The size of each segment reflects the average number of speakers attributed to languages classified under that particular level of endangerment."
    return render_template('bar_chart.html', image_path=image_path, text=text) 
    return render_template('bar_chart.html', image_path=image_path, text=text)
    # return '<img src="/static/images/avg_speakers.png" alt="avergage number of speakers left">'
    # return redirect(url_for('index'))

app.run(debug=True)