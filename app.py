from flask import Flask,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def Hello_world():
    return "for testing purpose"


if __name__== "__main__":
    app.run(debug=True,port=8000)
