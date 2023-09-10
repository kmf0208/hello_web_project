import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)


@app.route('/names', methods=['GET'])
def get_name():
    new_names = request.args.get('add')
    predefined_names = ["Julia", "Alice", "Karim"]
    
    NwList= []
    if new_names:
        NwList.append(new_names)
        result = [*predefined_names, *NwList]
    else:
        result = predefined_names
    
    response = ', '.join(result)
    return response
    

    return "Julia, Alice, Karim"

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return "you didn't submit any names", 400
    names = request.form['names'].split(',')
    sorted_name = sorted(names)
    return ','.join(sorted_name)

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_num = sum(1 for i in text if i in 'aeiou')
    return f'There are {vowel_num} vowels in "{text}"'

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f'I am waving at {name}'

# == Your Routes Here ==
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

   