from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, IN',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Engineer',
  'location': 'Delhi, IN',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'SF,USA',
  'salary': '$150,000'
}, {
  'id': 4,
  'title': 'Frontend Engineer',
  'location': 'Pune, IN'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=False)
