from flask import Flask, render_template, request, current_app
import os

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'home':1, 'menu':0}
    return render_template('index.html', menu=menu)

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    menu = {'home':0, 'menu':1}
    if request.method == 'GET':
        languages = [
            {'disp':'영어', 'val':'en'},
            {'disp':'일어', 'val':'jp'},
            {'disp':'중국어', 'val':'cn'},
            {'disp':'프랑스어', 'val':'fr'},
            {'disp':'스페인어', 'val':'es'},
        ]
        return render_template('menu.html', menu = menu,
        options=languages) # 서버에서 클라이언트로 정보 전달
    else:
        # 사용자가 입력한 정보를 서버가 읽음. tag 안에 특정한 name을 갖는 걸 부르는 듯
        index = request.form['index'] 
        lang = request.form['lang']
        lyrics = request.form['lyrics']
        print(lang, index, lyrics, sep = '\n')
        
        # 사용자가 입력한 파일 읽기, upload 디렉토리에 저장
        f_image = request.files['image']
        print(f_image.filename)  # 사용자가 입력한 파일 이름
        filename = os.path.join(current_app.root_path, 'static/upload/') + f_image.filename # 저장할 경로까지 만든 것
        print(filename)

        f_image.save(filename)

        ### !!! 모델 실행 후 결과를 돌려줌 !!! ###
        # ex) 동물 분류하는 모델을 학습시켰고 그 모델을 저장, 여기에서 불러와서 predict한다면
        result = '독수리 (73.52%)'
    
        return render_template('menu_res.html', result = result, f_name = f_image.filename,menu = menu)
        
if __name__ == '__main__':
    app.run(debug=True)