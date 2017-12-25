def pipeline
node('master') {
		#Test va
    	checkout scm
        pipeline = load 'package/ui-web/tes2.groovy'
        pipeline.firstTest()
    }
    
    
    
   
