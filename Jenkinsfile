def pipeline
node('master') {
		#Test cmtgg
    	checkout scm
        pipeline = load 'package/ui-web/tes2.groovy'
        pipeline.firstTest()
    }
    
    
    
   
