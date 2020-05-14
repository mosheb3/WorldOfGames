pipeline {
   agent any
   options {
      timestamps()
   }

   environment {
       PROJ_ENVIRONMENT="master"
       PROJ_BRANCH="master"
       WORK_DIR="/srv/projects/WorldOfGames"
       PYTHON_INTERPRETER="/usr/bin/python3"
   }

   parameters {
      string(name: "MAIL_TO", defaultValue: "mosheb3@gmail.com")
   }

   stages {
      stage('Cloning From GitHub') {
         steps {
            echo 'Cloning..'
            git 'https://github.com/mosheb3/WorldOfGames'
         }
      }

      stage('Building image') {
         steps{
            echo 'Building App Image..'
            sh('docker build -t wog:latest .')
            echo 'Building WebServer Image..'
            sh('docker build -t -f Dockerfile_web wog-web:latest .')
         }
      }

      stage('Running WebServer') {
         steps{
            echo 'running..'
            sh('docker run --rm -d -p 8081:8081 --name wog-web -v $(pwd):/app wog-web:latest')
         }
      }

/*      stage('testing application') {
         steps{
         echo 'testing..'
         bat 'python tests/e2e.py'
      }*/
   } //end stages
/*   post {
      always {
         echo 'finalizing..'
         bat 'docker login -u alexkalugin -p *******'
         bat 'docker-compose push'
         bat 'docker-compose down --rmi all'
      }
   }*/

} //end pipeline
