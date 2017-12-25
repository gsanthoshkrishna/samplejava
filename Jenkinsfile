def pipeline
node('master') {
		checkout scm
		def grvld = load 'package/ui-web/test2.groovy'
		grvld.firstTest16()
    }
    
    
    
   
