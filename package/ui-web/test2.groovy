def firstTest16() {
    def me = sh (script:'git show --name-only origin/master',returnStdout).trim().split('/')
    me.split('/')
}

return this