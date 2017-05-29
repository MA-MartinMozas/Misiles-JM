import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
import d_aerodinamico
import MisionMisil

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("This is your response")
        #self.finish()
        self.render("SeleccionGeo.html")

geo = dict()

class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()
    mis = dict()


    def open(self):
        self.connections.add(self)
        print('New connection was opened')
        # self.write_message("Conn!")


    def on_message(self, message):
        # print(message)
        print(type(message))
        json_string = u'%s' %(message,)
        print(json_string)
        # json_string = u'{ "id":"123456789"}'
        print(json_string)
        msg = json.loads(json_string)
        print(type(msg))
        obj = json.loads(json_string)
        print(type(obj))

        if msg['tipo'] == 'geo':
            global geo
            geo = msg
            result = d_aerodinamico.principal(geo)
            print("reynoolds", result["Rex"])
            self.write_message(result)
            print("* " * 10)
            print("geo:", geo)
        elif msg['tipo'] == 'actualiza':
            global geo
            print("* "*10)
            print("geo:", geo)
            result = d_aerodinamico.principal(geo)
            self.write_message(result)
        else:
            mis=msg
            result = MisionMisil.principal2(mis)
            self.write_message(result)
        # message = msg

        print(result)




        # print('received message: %s\n' %message)
        # print(self.connections)
        # for elem in self.connections:
        #     elem.write_message({"d": message["d"] + ' a todos'}, binary=False)

        # [con.write_message('Hi!') for con in self.connections]

        # con este self.write envio lo de dentro al javascript de vuelta por tanto mandaremos un diccionario con los resultados obtenidos en el python



    def on_close(self):
        print('connection closed\n')



application = tornado.web.Application([(r'/', IndexHandler),
                                       (r'/ws', WSHandler),
                                       (r'/(.*)', tornado.web.StaticFileHandler,  {'path': r'C:\Users\graficos\Desktop\25-5-2017jp\Misiles-JM-master'}),])
# en el enlace anterior tenemos que poner el lugar donde se encuentra el archivo si cambiamos de ordenador cambiará la posición
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

