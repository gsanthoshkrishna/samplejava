def pipeline
node('master') {
		#Test cmt
    	checkout scm
        pipeline = load 'package/ui-web/tes2.groovy'
        pipeline.firstTest()
    }
    
    
    
   
