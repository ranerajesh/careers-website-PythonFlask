from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://6rt2vm6iz3lnnb2m4aqx:pscale_pw_L6mEw74nlYzmx3mGEcOqVpvrDbjvQ0qdKiGcr1gTWeO@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM joviancareers.jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
