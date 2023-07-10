from flask import Flask

# create_app() 이 실행되면 내부에 함수들이 모두 동작을 하게 된다
# create_app은 프레임워크에 이미 내장되어있는 예약어
def create_app():
    # Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서 거기부터 코드를 찾아나갑니다.
    # Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다
    app = Flask(__name__)


    from views import main_views
    
    app.register_blueprint(main_views.bp)
    
    return app
