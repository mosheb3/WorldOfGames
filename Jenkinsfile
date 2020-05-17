pipeline {
   agent any
   options {
      timestamps()
   }

   environment {
       PROJ_ENVIRONMENT="master"
       PROJ_BRANCH="master"
       PYTHON_INTERPRETER="/usr/bin/python3"
       BUILD_NUMBER="latest"
       registry = "mosheb3/wog"
       registry_web = "mosheb3/wog-web"
       registryCredential = 'docker_hub_cred'
       dockerImage = ''
       dockerImage_web = ''
   }

   parameters {
      string(name: "MAIL_TO", defaultValue: "mosheb3@gmail.com")
      string(name: "WORK_DIR", defaultValue: "/srv/projects/WorldOfGames")
      choice(name: 'BUILD_OPS', choices: "NO\nYES", description: 'Building image options')
      choice(name: 'DEPLOY_OPS', choices: "NO\nYES", description: 'Deploy options')
   }

   stages {
      stage('Cloning From GitHub') {
         steps {
            echo 'Cloning App ..'
            git 'https://github.com/mosheb3/WorldOfGames'
         }
      }

      stage('Building image') {
         steps{
            script {
               if ("${params.BUILD_OPS}" == "YES") {
                  dockerImage = docker.build registry + ":$BUILD_NUMBER"
                  dockerImage_web = docker.build registry_web + ":$BUILD_NUMBER"
               }
               else {
                  echo "No need to build new version."
               }
            }
         }
      }

      /*stage('Building image') {
         steps{
            script {
               if ("${params.BUILD_OPS}" == "YES") {
                  echo 'Building App Image..'
                  sh('docker build -t mosheb3/wog:latest .')
                  echo 'Building WebServer Image..'
                  sh('docker build -f Dockerfile_web -t mosheb3/wog-web:latest .')
               }
            }
         }
      }*/

      stage('Running WebServer') {
         steps{
            echo 'Running WebServer ..'
            //sh('chmod +x ./runWebServer.sh')
            //sh('./runWebServer.sh')
            script{
                dockerImage_web.inside {
                   sh('chmod +x ./runWebServer.sh')
                   sh('./runWebServer.sh')
                   echo "Run Tests .."
                   sh('chmod +x ./runTests.sh')
                   sh('./runTests.sh')
                }
            }
         }
      }

      /*stage('Running Game4Testing') {
         steps{
            echo 'Running..'
            //sh('python3 MainGame.py < test_answers.txt')
            sh('chmod +x ./runTests.sh')
            sh('./runTests.sh')
         }
      }*/

      stage('Deploy Image') {
         steps{
            script {
               if ("${params.DEPLOY_OPS}" == "YES") {
                  docker.withRegistry( '', registryCredential ) {
                     dockerImage.push()
                     dockerImage_web.push()
                  }
               }
               else {
                  echo "No need to deploy new version."
               }
            }
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
