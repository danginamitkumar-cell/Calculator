from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:#121212;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;font-family:sans-serif}
.calc{background:#1e1e1e;padding:20px;border-radius:20px;width:280px}
#display{width:100%;height:60px;background:#000;color:#0f0;font-size:32px;text-align:right;padding:10px;box-sizing:border-box;border-radius:10px;border:none;margin-bottom:15px}
.row{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;margin-bottom:10px}
button{height:60px;font-size:22px;border:none;border-radius:10px;background:#333;color:white}
button.op{background:orange}
button.eq{background:#d32f2f}
button:active{transform:scale(0.95)}
</style>
</head>
<body>
<div class="calc">
<input id="display" readonly>
<div class="row"><button onclick="add('7')">7</button><button onclick="add('8')">8</button><button onclick="add('9')">9</button><button class="op" onclick="add('/')">/</button></div>
<div class="row"><button onclick="add('4')">4</button><button onclick="add('5')">5</button><button onclick="add('6')">6</button><button class="op" onclick="add('*')">*</button></div>
<div class="row"><button onclick="add('1')">1</button><button onclick="add('2')">2</button><button onclick="add('3')">3</button><button class="op" onclick="add('-')">-</button></div>
<div class="row"><button onclick="add('0')">0</button><button onclick="clr()">C</button><button class="eq" onclick="calc()">=</button><button class="op" onclick="add('+')">+</button></div>
</div>
<script>
let d=document.getElementById('display')
function add(v){d.value+=v}
function clr(){d.value=''}
function calc(){try{d.value=eval(d.value)}catch{d.value='Error'}}
</script>
</body>
</html>
    """
app.run(host='0.0.0.0', port=5000)
