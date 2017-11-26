from flask import Flask,request
from flask.templating import render_template
import datetime,time,requests,json,sqlite3,os
import plotly.plotly as py
import plotly.graph_obs as go 


def plotPie():
    labels = ['BANK','IT','PHARMA','METAL']
    values = [10,20,30,40]
    trace = go.pie(labels = labels, values = values)
    pi.iplot([trace],filename='basic_pie_chart')
 
# print( a nice greeting.
#TODO add try catch
def checkOrderFile():
    if os.path.isfile('so.txt'):
        soFile = open('so.txt')
        return soFile.read()
    else:
        return 'asc'

def execSql(sqlStmt,stmtType):
    sqlConn = sqlite3.connect('test.db')
    sqlCur = sqlConn.cursor()
    sqlRes = sqlCur.execute(sqlStmt)
    if stmtType == 'select':
        rslt = sqlRes.fetchall()
        return rslt
    else:
        sqlConn.commit()
        return None

def getCustDetails(sortBy):
    sOrd = checkOrderFile()
    if sOrd == None or sOrd == '':
        sOrd = 'asc'
    sqlStmt = 'select * from customer order by '+sortBy+' '+sOrd
    soFile = open('so.txt','w')
    if sOrd == 'asc':
        soFile.write('desc')
    else:
        soFile.write('asc')
    sqlRes = execSql(sqlStmt, 'select')
    print('customer details')
    return sqlRes

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

def sendUpdate():
    custJson = getCustList()
    print(custJson)
    
def getCustList(): 
    custFile = open('cst.json','r')
    cstCont = custFile.read()
    print(cstCont)
    custJson = json.loads(cstCont)
    return custJson

def getReqResp(url):
    retJson = {}
    #print(url)
    res = requests.get(url)    
    res = requests.get('http://finance.google.com/finance/info?client=ig&q=NSE:SBIN')
    respCont = res.content[4:]
    #print respCont
    respJsonList = json.loads(respCont)
    '''
    for respJson in respJsonList:
        retJson['name'] = respJson['t']
        retJson['price'] = respJson['l']
    '''
    respJson = respJsonList[0]
    retJson['name'] = respJson['t']
    retJson['price'] = int(respJson['l'])
    return retJson
    
def getHoldings():
    holdingsFile = open('holdings.json','r')
    holdingsCont = holdingsFile.read()
    holdingsJson = json.loads(holdingsCont)
    return holdingsJson

def checkTgt(holdingJson,retJson):
    tgtJson = {}
    
    tgtPr = (holdingJson['pr'] * 0.03) + holdingJson['pr']
    curDiff = retJson['price'] - holdingJson['pr']
    tgtDiff = tgtPr - holdingJson['pr']
    
    percRchd = (curDiff/tgtDiff)*100
    tgtJson['name'] = holdingJson['name']
    tgtJson['price'] = retJson['price']
    tgtJson['tgtPrcnt'] = percRchd
    if percRchd > 90:        
        tgtJson['color'] = '#00FF00'
    else:
        tgtJson['color'] = '#ffff00'
        
    return tgtJson
    
def getCustTable(custJson):
    for custJsonItem in custJson:
        expDate = datetime.datetime.strptime(custJsonItem['expiry'],'%Y-%m-%d')
        today = datetime.datetime.now()
        daysDiff = (today - expDate).days
        if daysDiff >= 0:
             custJsonItem['color'] = '#ff0000'
        else:
            if daysDiff > -2 and daysDiff < 0 :
                custJsonItem['color'] = '#ffff00'
            else:
                custJsonItem['color'] = '#00FF00'
    return custJson
    

    
# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

@application.route('/welcome')
def welcomeMsg():
    holdingJson = getHoldings()
##################################################### ## Status :::: Done till here. getting error when uncommenting below line######################
    retJson = getReqResp('http://echo.jsontest.com/key/value/t/'+holdingJson['name']+'/l/1111')
    #tgtJson = checkTgt(holdingJson, retJson)
    return 'test Guru'
    
@application.route('/cstlist',methods=['POST','GET'])
def getCustomers():
    custRenList = []
    sortType = None
    print request.form.get('User', None)
    if request.form.get('User', None) == "User":
        sortType = 'User'
    elif request.form.get('Balance', None) == "Balance":
            sortType = 'Balance'
    elif request.form.get('Phone', None) == "Phone":
        sortType = 'Phone'
    elif request.form.get('ExpiresOn', None) == "ExpiresOn":
        sortType = 'ExpiresOn'
    print 'sort',sortType
    if sortType == None or sortType == '':
        sortType = 'user'
    custList = getCustDetails(sortType)
    for custItem in custList:
        custJsonItem = {}
        custJsonItem['user'] = custItem[0]
        custJsonItem['expiry'] = custItem[1]
        custJsonItem['balance'] = custItem[2]
        custJsonItem['phone'] = custItem[3]
        custRenList.append(custJsonItem)
    custJson = getCustList()
    custJson = getCustTable(custJson)
    return render_template('cstlist.html',tgtJson = custRenList)

@application.route('/newUser',methods=['POST','GET'])
def newUser():
    print('hi')
    if request.method == 'POST':
        print('post')
        usr = request.form['user']
        exp = request.form['expiresOn']
        phone = request.form['phone']
        area = request.form['area']
        bal = request.form['balance']
        newUsr = {}
        newUserList = ()
        newUsr['user'] = usr
        newUsr['expiry'] = exp
        newUsr['phone'] = phone
        newUsr['area'] = area
        insrtStmt = 'insert into customer values("'+usr+'","'+exp+'",'+bal+','+phone+',"'+area+'","TestAddress")'
        execSql(insrtStmt, 'insert')
        custJsonList = getCustList()
        custJsonList.append(newUsr)
        custJsonList = getCustTable(custJsonList)
        print 'new user'
        custFile = open('cst.json','w')
        
        custFile.write(json.dumps(custJsonList))
        return render_template('/cstlist.html',tgtJson = custJsonList)
    else:
        print('Get')
        return render_template('/newUser.html')
    return 'hi'
    

    
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=8080)
