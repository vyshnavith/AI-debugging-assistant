from flask import Flask, render_template, request
from ai_engine import explain_bug
app=Flask(_name_)
@app.route("/",methods=["GET","POST"])
def home():
    explaination=""
    if request.method=="POST":
        error_log=reuqest.form["error_log"]
        explaination=explain_bug(error_log)
        return render_template("index.html",explaination=explaination)
if __name__=="__main__":
    app.run(debug=True)
