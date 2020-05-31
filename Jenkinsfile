pipeline {
   agent any
   options {
      timestamps()
      buildDiscarder(logRotator(daysToKeepStr: '1',numToKeepStr: '1'))
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
       ext_dockerfile_web = 'Dockerfile.web'
   }

   parameters {
      string(name: "MAIL_TO", defaultValue: "mosheb3@gmail.com")
      string(name: "WORK_DIR", defaultValue: "/srv/projects/WorldOfGames")
      choice(name: 'BUILD_OPS', choices: "NO\nYES", description: 'Building image options')
   }

   stages {
      stage('Cloning From GitHub') {
         steps {
            echo 'Cloning App ..'
            git branch: 'master', url: 'https://github.com/mosheb3/WorldOfGames'
         }
      }

      stage('Building image') {
         steps {
            script {
               if ("${params.BUILD_OPS}" == "YES") {
                  dockerImage = docker.build registry + ":$BUILD_NUMBER"
                  dockerImage_web = docker.build(registry_web + ":$BUILD_NUMBER", " -f '${ext_dockerfile_web}' .")
                  //dockerImage_web = sh("docker build -f Dockerfile.web -t mosheb3/wog-web:latest .")
                  //dockerImage_web = docker.build registry_web + ":$BUILD_NUMBER"
               }
               else {
                  echo "Build image cancel by user"
               }
            }
         }
      }

      stage('Running WebServer') {
         steps {
            echo 'Running WebServer ..'
            script{
               if ("${params.BUILD_OPS}" == "YES") {
                  dockerImage_web.inside {
                     sh('chmod 744 *.py *.sh')
                     //sh('./runGame.sh')
                     echo "Run Tests ..."
                     sh('chmod +x ./runTests.sh')
                     def test_res = sh(script: "./runTests.sh", returnStdout: true).trim() as String
                     echo("res = ${test_res}")

                     //script {
                     //   def disk_size = sh(script: "df / --output=avail | tail -1", returnStdout: true).trim() as Integer
                     //   println("disk_size = ${disk_size}")
                     //}
                  } //end dockerImage_web.inside
               }
               else {
                  echo "Can't run webserver, build image cancel by user"
               }

               def nextjob=build job: 'WorldOfGames_Deploy_Remote'
            }
         }
      }

      /*stage('Deploy Image') {
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
