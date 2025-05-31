pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        FLASK_APP = "app.py"
        DATABASE_URL = "sqlite:///${WORKSPACE}\\instance\\trustbot.db"
        SECRET_KEY = "8Wq_L6DYvP3V7HPbA-FXZr4U8OtX8mVdeDKpWnDU90M" 
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/M-Uzair-Farooq/TrustBot.git',
                        credentialsId: '' 
                    ]]
                ])
                bat 'dir'  
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat """
                    python -m venv "${VENV_DIR}"
                    call "${VENV_DIR}\\Scripts\\activate"
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Initialize Database') {
            steps {
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    python -c "from app import create_app; app = create_app()"
                """
                bat """
                    mkdir instance || echo "Instance folder exists"
                """
            }
        }

        stage('Run Application') {
            steps {
                bat """
                    call "${VENV_DIR}\\Scripts\\activate"
                    python app.py
                """
            }
        }
    }

    post {
        always {
            bat 'taskkill /F /IM python.exe /T || echo "No Python processes to kill"'
            cleanWs()
        }
    }
}