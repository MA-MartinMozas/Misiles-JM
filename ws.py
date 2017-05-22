import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import prueba1

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("This is your response")
        #self.finish()
        self.render("index.html")

class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()
    lastMessage = ""

    def open(self):
        self.connections.add(self)
        print('New connection was opened')
        self.write_message("Conn!")

    def on_message(self, message):
        # print(message)
        print(type(message))
        json_string = u'%s' %(message,)
        print(json_string)
        # json_string = u'{ "id":"123456789"}'
        print(json_string)
        msg = json.loads(json_string)
        print(type(msg))
        # obj = json.loads(json_string)
        # print(type(obj))
        message = msg['msg']

        print('received message: %s\n' %message)
        print(self.connections)
        for elem in self.connections:
            elem.write_message({"msg": message + ' a todos'}, binary=False)

        # [con.write_message('Hi!') for con in self.connections]
        # aqui tengo que meter cada uno de los apartados del diccionario
        self.write_message({"msg": message ,'otrallave': 1})
        self.lastMessage = message
        print("Last Message = " + message)
        pr = prueba1.prueba1()
        pr.hazAlgo(str(message))

    def on_close(self):
        print('connection closed\n')



application = tornado.web.Application([(r'/', IndexHandler),(r'/ws', WSHandler),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

