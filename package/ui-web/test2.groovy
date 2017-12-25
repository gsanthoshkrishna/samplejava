def firstTest16() {
    def me = sh (script:'git show --name-only origin/master',returnStdout:true).trim().split('/')
    println(me)
    
}

return this