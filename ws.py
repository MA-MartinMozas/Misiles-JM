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
mis = dict()

class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()



    def open(self):
        self.connections.add(self)
        print('New connection was opened')
        # self.write_message("Conn!")


    def on_message(self, message):
        # print(message)
        # print(type(message))
        json_string = u'%s' %(message,)
        # print(json_string)
        # json_string = u'{ "id":"123456789"}'
        # print(json_string)
        msg = json.loads(json_string)
        # print(type(msg))
        obj = json.loads(json_string)
        # print(type(obj))

        if msg['tipo'] == 'geo':
            global geo
            geo = msg
            result = d_aerodinamico.principal(geo)
            # result = resultados
            print("reynoolds", result["Rex"])
            self.write_message(result)
            print("* " * 10)
            print("geo:", geo)
        elif msg['tipo'] == 'actualiza':
            # global geo
            print("* "*10)
            print("geo:", geo)
            result = d_aerodinamico.principal(geo)
            self.write_message(result)
        elif msg['tipo'] == 'mis':
            global mis
            mis = msg
            result = MisionMisil.principal2(mis)
            self.write_message(result)
            print("* " * 10)
            print("mis:", mis)
        else:
            # global mis
            print("* " * 10)
            print("mis:", mis)
            result = MisionMisil.principal2(mis)
            self.write_message(result)



        print("result=",result)






    def on_close(self):
        print('connection closed\n')



application = tornado.web.Application([(r'/', IndexHandler),
                                       (r'/ws', WSHandler),
                                       (r'/(.*)', tornado.web.StaticFileHandler,  {'path': r'C:\Users\manu3m94\Desktop\UNI\python java\Misiles-JM-master'}),])
# en el enlace anterior tenemos que poner el lugar donde se encuentra el archivo si cambiamos de ordenador cambiará la posición
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

