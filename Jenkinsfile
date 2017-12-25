def pipeline
node('master') {
		checkout scm
		def pipeline = load 'package/ui-web/test2.groovy'
		pipeline.firstTest14()
    }
    
    
    
   
