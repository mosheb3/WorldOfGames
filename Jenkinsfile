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
      stage('build'){
         steps {
            sh ("docker build -t wog .")
         }
      }
   }
}