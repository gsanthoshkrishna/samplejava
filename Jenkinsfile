def pipeline
node('master') {
		checkout scm
        pipeline = load 'package/ui-web/tes2.groovy'
        pipeline.firstTest1()
    }
    
    
    
   
