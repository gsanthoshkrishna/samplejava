def me = sh (script:'git show --name-only origin/master',returnStdout:true).trim().split('/')
println("------------output--------------")
for (i = 0; i <me.length; i++) {
   println(me[i])
   if(me[i] == 'ui-web')
   {
      def pipeui = load 'package/ui-web/test2.groovy'
      pipeui.testui()
   }
   if(me[i] == 'service')
   {
      def pipeserv = load 'package/service/test1.groovy'
      pipeserv.testservice()
   }
   
}




