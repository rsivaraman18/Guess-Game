from flask import Flask,render_template,request,session
import random


app = Flask(__name__)
app.secret_key = '1234'

@app.route('/',methods=['GET',"POST"])
def gamepage():
    if request.method=="POST":
        myat   = session['attempt']    # 5
        uguess = request.form['uguess']
        cguess = session['cguess']     

        if myat!=0 :
            result = cal(uguess,cguess,myat)
        else:
            result = cal1()

        return render_template('index.html',result =result)


    session.pop('cguess', None)  
    session.pop('attempt', None)

    cguess = random.randint(1,50)
    session['cguess'] = cguess
    session['attempt'] = 5
    uall = []
    session['uall'] = uall
    gres=''
    tip= "Are you ready to Play"
    res = {'tip':tip, 'c':'','a':5,'gres':gres,'uall':uall,'d':''}
    return render_template('index.html',result=res)

    



def cal(u,c,myat):
    myat = myat -1

    uall = session['uall']  
    uall.append(u)
    session['uall'] = uall

    session['attempt'] = myat
    u = int(u)
    d = abs(u-c)

    tip=''
    gres = ''
    if (u==c):
      tip= "You have correctly guess the number"
      gres = 'You Won the Game'


    elif (u>=c) & (d>20):
        tip= "Sry! guess is bigger & far away"

    elif (u>=c) & (d>11 & d<=20):
        tip= "Sry! guess is bigger & onslot"
       
    elif (u>=c) & (d>5  & d<=10 ):
        tip= "Sry! guess is bigger & Near"
    
    elif (u>=c) & (d>2 & d<=5):
        tip= "Sry! guess is bigger & Almost there"
    
    elif (u>=c) & (d>0 & d<=2):
        tip= "Sry! guess is bigger & approx right "

    
    elif (c>=u) & (d>20):
        tip= "Sry! guess is smaller & far away"

    elif (c>=u) & (d>10 & d<=20):
        tip= "Sry! guess is smaller &  on slot"
    
    elif (c>=u) & (d>5  & d<=10 ):
        tip= "Sry! guess is bigger & Near"
       
    elif (c>=u) & (d>2 & d<=5):
        tip= "Sry! guess is bigger & Almost there"

    elif (c>=u) & (d>0 & d<=2):
       tip= "Sry! guess is bigger & approxy "
    
    

    res = {'tip':tip, 'c':c,'a':myat,'gres':gres,'uall':uall,'d':d}
    return res


def cal1():
    tip= "You Lost the Game"
    gres = "Game over"
    c = ''
    myat = '-'

    res = {'tip':tip, 'c':c,'a':myat,'gres':gres}
    return res



       
if __name__ == '__main__':
    app.run(debug=True)






# session.clear()
