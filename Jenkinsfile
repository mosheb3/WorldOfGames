pipeline {
   agent any
   options {
      timestamps()
   }

   environment {
       PROJ_ENVIRONMENT="master"
       PROJ_BRANCH="master"
       PYTHON_INTERPRETER="/usr/bin/python3"
   }

   parameters {
      string(name: "MAIL_TO", defaultValue: "mosheb3@gmail.com")
      string(name: "WORK_DIR", defaultValue: "/srv/projects/WorldOfGames/")
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
            sh('docker build -f Dockerfile_web -t wog-web:latest .')
         }
      }

      stage('Running WebServer') {
         steps{
            echo 'Running..'
            sh('docker run --rm -d -p 8081:8081 --name wog-web -v "${params.WORK_DIR}":/app wog-web:latest')
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
         bat 'docker login -u mosheb3 -p *******'
         bat 'docker-compose push'
         bat 'docker-compose down --rmi all'
      }
   }*/

} //end pipeline
