def pipeline
node('master') {
		#Test vate
    	checkout scm
        pipeline = load 'package/ui-web/tes2.groovy'
        pipeline.firstTest()
    }
    
    
    
   
