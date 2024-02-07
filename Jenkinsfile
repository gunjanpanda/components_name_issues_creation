pipeline {
    agent any

    stages {
        
        stage('Run Python Script') {
            steps {
                // Run your Python script
                script {
                    sh 'python3 bulk_issue_creation.py'
                }
            }
        }

        
    }
}