def pipeline
    node('master') {
    	Label('Hello#1')
    	checkout scm
        pipeline = load 'package/ui-web/test2.groovy'
        pipeline.firstTest()
    }
    
    
    
   