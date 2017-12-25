def firstTest16() {
    def me = sh 'git show --name-only origin/master'
    me.split('/')
}

return this