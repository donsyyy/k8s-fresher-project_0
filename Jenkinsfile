pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Static Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh '''$SCANNER_HOME/bin/sonar-scanner \
                        -Dsonar.scanner.javaOpts="-Djava.net.preferIPv4Stack=true" \
                        -Dsonar.projectKey=K3s-Boutique \
                        -Dsonar.projectName=K3s-Boutique \
                        -Dsonar.sources=k8s,scripts \
                        -Dsonar.language=py'''
                }
            }
        }

        stage('Deploy to K3s') {
            steps {
                sh '''
                    kubectl apply -n webapps -f k8s/app-manifests.yaml
                    kubectl rollout status deployment/frontend -n webapps --timeout=60s
                '''
            }
        }

        stage('Cluster Health Check') {
            steps {
                sh '''
                    echo "=== Active Pods in webapps ==="
                    kubectl get pods -n webapps -o wide
                    echo "=== Service Endpoints ==="
                    kubectl get svc -n webapps
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD Deployment Succeeded!"
        }
        failure {
            echo "Pipeline Failed - check logs."
        }
    }
}
