from flask import *

def template(file):
    return(render_template(f'./templ/{file}'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')




# if __name__ == '__main__':
app.run(port = 3000, debug = 1)