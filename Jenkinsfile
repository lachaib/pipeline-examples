node {
    checkout scm
    def version='0.0.1')
    docker.withServer('<YOUR_REGISTRY>') {
    def img = docker.build('python-test' , 'test/')

    parallel(

        unittest: {
            stage('Unit Test') {
                img.inside {
                    sh 'pytest test/test.py'
                }
            }
        },
        pylint: {
            stage('Pylint') {
                img.inside {
                    sh 'pylint src/'
                }
            }
        })
    

    stage('Package') {
        docker.build('myApp:$version', '.')
    }

    if(env.BRANCH_NAME =~ /release/) {
        stage('Push') {
            docker.push('myApp:$version')
        }
    }
    }
}
