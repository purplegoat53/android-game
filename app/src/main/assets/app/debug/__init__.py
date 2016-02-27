from bottle import Bottle, run, view, request
import thread, traceback, sys, os, json, base64
from StringIO import StringIO

def main_server():
  app = Bottle()
  interpreter_vars = {}

  @app.route('/')
  @view("index")
  def index():
    res = []
    files = os.listdir(app_path)
    for file in files:
      if not file.endswith(".py"):
        continue
      tab = {"name": file}
      with open(os.path.join(app_path, file), "rb") as f:
        tab["contents"] = f.read()
      res.append(tab)
    return {"tabs": base64.b64encode(json.dumps(res))}

  @app.route('/ajax/interpret', method="POST")
  def interpret():
    code = request.forms.get("code")
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
    sys.stdout = sys.stderr = pipe = StringIO()
    try:
      eval(compile(code, "<string>", "single"), interpreter_vars)
    except Exception as e:
      return {"result": traceback.format_exc(), "exception": str(e)}
    finally:
      sys.stdout = orig_stdout
      sys.stderr = orig_stderr
    return {"result": pipe.getvalue()}

  path, _ = os.path.split(__file__)
  bottle.TEMPLATE_PATH = [os.path.join(path, "views")]
  run(app, host='0.0.0.0', port=8080)

#FIX: shouldn't need to hardcode app module
import app
app_path, _ = os.path.split(app.__file__)

if __name__ == "__main__":
  main_server()
else:
  thread.start_new_thread(main_server, ())
