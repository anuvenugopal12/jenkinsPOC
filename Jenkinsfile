pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip setuptools wheel'
                sh '.venv/bin/python -m pip install -e ".[dev]"'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest'
            }
        }

        stage('Run QA Log Analyzer') {
            steps {
                sh '.venv/bin/qa-log-analyzer sample_logs/app.log --output reports/report.json || true'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/report.json', allowEmptyArchive: true
        }
    }
}