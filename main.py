



from flask import Flask, request, render_template,url_for

import os
import json
import num2text

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET','POST'])
def home():
   
    if request.method == 'POST':
        num = request.form.get('number')
        num=int(num)

        print(num)
        text=num2text.num2text(num)
        print(text)

       
        return render_template('index.html', text=text)
    text=''
    return render_template('index.html', text='')
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
if __name__ == '__main__':
    app.run(port=3000, debug=True)
