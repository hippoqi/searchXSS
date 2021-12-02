pipeline {
    agent any
    stages {
		stage('test') {
		    agent {
		        docker {
		            image 'python:3.9.7-alpine3.13'
		        }
		    }
            steps {
				sh 'python unit_test.py'
            }
        }

    stage ("OWASP Dependency Check"){
		steps{
			dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
		}

	}
    }
	post{
		success{
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
