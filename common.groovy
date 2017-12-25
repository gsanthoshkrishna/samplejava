def me = sh (script:'git show --name-only origin/master',returnStdout:true).trim().split('/')

def pipeui = load 'package/ui-web/test2.groovy'
pipetest.testui()


def pipeserv = load 'package/service/test1.groovy'
pipetest.testservice()