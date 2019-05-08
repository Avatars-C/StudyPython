from wsgiref.simple_server import make_server

# 处理函数
def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    body = "<h1>hello world %s<h1>"% (environ["PATH_INFO"][1:] or "web")
    return [ body.encode()]

# 创建一个服务器，是application
server = make_server("localhost", 9999, application)

print("服务启动，按Ctrl+C终止... http://localhost:9999/")

# 开始监听HTTP请求
server.serve_forever()
