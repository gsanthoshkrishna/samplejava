def pipeline
    node('master') {
    	checkout scm
        pipeline = load 'test.groovy'
        pipeline.firstTest()
    }
    
    
    
   