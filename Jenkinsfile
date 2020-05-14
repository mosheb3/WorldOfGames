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
      string(name: "WORK_DIR", defaultValue: "/srv/projects/WorldOfGames")
      choice(name: 'Build', choices: "yes\no", description: '')
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
            script {
               if ("${params.build}" == "yes") {
                  echo 'Building App Image..'
                  sh('docker build -t wog:latest .')
                  echo 'Building WebServer Image..'
                  sh('docker build -f Dockerfile_web -t wog-web:latest .')
               }
            }
         }
      }

      stage('Running WebServer') {
         steps{
            echo 'Running..'
            sh('chmod +x ./runWebServer.sh')
            sh('./runWebServer.sh')
         }
      }

      stage('Running Game4Testing') {
         steps{
            echo 'Running..'
            //sh('python3 MainGame.py < test_answers.txt')
            sh('chmod +x ./runTests.sh')
            sh('./runTests.sh')
         }
      }

      stage('Testing App') {
         steps{
            echo 'Testing.. Testing.. '
         }
      }
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
