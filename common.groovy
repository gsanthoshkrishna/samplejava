def me = sh (script:'git show --name-only origin/master',returnStdout:true).trim().split('/')
    println(me[0])
    println(me[1])
    println(me[2])

def pipetest = load 'package/ui-web/test2.groovy'
pipetest.testui()