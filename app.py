from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

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
  jobs = load_jobs_from_db()
  #return render_template('home.html', jobs=JOBS, company_name='Jovian')
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
  #return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
  print(id)
  job = load_job_from_db(id)
  return jsonify(job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
