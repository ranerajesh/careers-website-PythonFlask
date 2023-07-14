from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

db_connection_string = my_secret
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM joviancareers.jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


def load_job_from_db(id):
  str = "SELECT * FROM jobs WHERE id={}".format(id)
  with engine.connect() as conn:
    t = text(str)
    result = conn.execute(t)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      #return rows[0]._maping
      return dict(rows[0]._mapping)


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
