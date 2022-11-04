from flask import Flask,request,render_template
import pyshorteners 
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home(): 

    if request.method == 'POST':
        # print(request.form['name'])
        url=request.form['url'] #get url from input field 
        s=pyshorteners.Shortener() #logic for converting entered url to shorten one 
        shorter=s.tinyurl.short(url)
        return render_template('home.html',shorter=shorter)

    return render_template('home.html') 

if __name__=='__main__':
    app.run(debug=True)