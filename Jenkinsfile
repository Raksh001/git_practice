pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('set-environment') {
      when { anyOf { branch 'master'; branch 'staging' ; branch 'release'; branch 'stagingp'} }
      steps {
        script {
          env.REPO = "apply-mobweb"
          env.REG_URL = "997116068644.dkr.ecr.us-east-1.amazonaws.com"
          if (env.BRANCH_NAME == 'staging') {
            env.JOVEO_ENV = "staging"
            env.AWS_INSTANCE_TAG = "staging-apply-mobweb"
          }
          if (env.BRANCH_NAME == 'stagingp') {
            env.JOVEO_ENV = "stagingp"
            env.AWS_INSTANCE_TAG = "stagingp-apply-mobweb"
          }
          else if (env.BRANCH_NAME == 'master') {
            env.JOVEO_ENV = "dev"
            env.AWS_INSTANCE_TAG = "dev-apply-mobweb"
          }
          else if (env.BRANCH_NAME == 'release') {
            env.JOVEO_ENV = "prod"
            env.AWS_INSTANCE_TAG = "prod-apply-mobweb"
            env.REG_URL = "485239875118.dkr.ecr.us-east-1.amazonaws.com"
          }
        }
      }
    }
    stage('build') {
          when { anyOf { branch 'master'; branch 'staging'; branch 'release' ; branch 'stagingp'} }
          steps {
            sh 'sh build.sh $JOVEO_ENV'
          }
        }
    stage('login to ecr') {
        when { anyOf { branch 'release'; branch 'staging'; branch "master"; branch 'stagingp' } }
        steps {
           script {
               if (env.BRANCH_NAME == 'release') {
                   sh '$(aws ecr get-login --region us-east-1 --no-include-email)'
               } else {
                   sh '$(aws ecr get-login --region us-east-1 --no-include-email --profile joveo-dev)'
               }
           }
        }
    }
    stage('push to ecr') {
        when { anyOf {branch 'release'; branch 'master'; branch 'staging'; ; branch 'stagingp'} }
        steps {
           sh 'docker tag joveo/$REPO $REG_URL/$REPO:$JOVEO_ENV'
           sh 'docker push $REG_URL/$REPO:$JOVEO_ENV'
        }
    }
    stage('deploy to ec2') {
      when { anyOf { branch 'release'; branch 'master'; branch 'staging'; branch 'stagingp' } }
      steps {
        sh 'sh -vx deploy.sh $AWS_INSTANCE_TAG $REG_URL/$REPO $JOVEO_ENV'
      }
    }
  }
}
