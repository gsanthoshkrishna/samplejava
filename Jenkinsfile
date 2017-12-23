def pipeline
    node('master') {
    	checkout scm
        pipeline = load 'package/ui-web/test2.groovy'
        pipeline.firstTest()
    }
    
    
    
   