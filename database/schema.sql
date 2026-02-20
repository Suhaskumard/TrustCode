CREATE TABLE IF NOT EXISTS developers (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  github_login TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS commits (
  id TEXT PRIMARY KEY,
  developer_id INT REFERENCES developers(id),
  message TEXT NOT NULL,
  files_changed INT NOT NULL,
  modules_impacted INT NOT NULL,
  tests_touched BOOLEAN NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS risk_scores (
  commit_id TEXT REFERENCES commits(id),
  risk_score NUMERIC(5,2) NOT NULL,
  failure_probability NUMERIC(5,2) NOT NULL,
  explanation JSONB NOT NULL,
  evaluated_at TIMESTAMP DEFAULT NOW()
);
