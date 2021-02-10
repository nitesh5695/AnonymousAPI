from flask import Flask,render_template,request,session,redirect,url_for
import requests
import json
app=Flask(__name__)
app.secret_key="Nitesh@1234"
@app.route('/')
def login_page():
    return render_template('index.html')
@app.route('/login_validate',methods=['POST'])
def login_validate():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        gst_no=request.form.get('gst')
        password=request.form.get('password')
        client_key=request.form.get('g-recaptcha-response')
        secret_key="6Let1lEaAAAAAC-3PummEc5B8BV3xdx-iRRnvT4f"
        data={
	"username":username,
     "email":email,

	"password":password,
	"gst_no":gst_no,
	"captcha":{"secret":secret_key,
	           "response":client_key
	           }
}
        headers={'content-type':'application/json'}
        token_url="http://127.0.0.1:7001/gettoken_anonymous/"
        r=requests.post(url=token_url,headers=headers)
        datauser=r.json()
        print(datauser['access'])
        headers={'Authorization':'Bearer'+' '+datauser['access'],'content-type':'application/json'}
        url='http://127.0.0.1:7001/register/'
        json_data=json.dumps(data)
        r=requests.post(url=url,headers=headers,data=json_data)
        datauser=r.json()
        print(datauser)



        # url= "https://www.google.com/recaptcha/api/siteverify"
        # response_data=requests.post(url,data=data)
        # response=json.loads(response_data.text)
        # print(response)
        # verify=response['success']
        # print(verify)
        return render_template('index.html',message=datauser)
if __name__=='__main__':
    app.run(debug=True)
