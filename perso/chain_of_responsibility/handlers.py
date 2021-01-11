

class Handler:
    def set_next(self, next_handler):
        pass
    def handle(self, request):
        pass

class BaseHandler(Handler):
    next_ = None
    def set_next(self, next_handler):
        self.next_ = next_handler
    def handle(self, request):
        print('a pas marche nonnon')
        if self.next_ != None:
            self.next_.handle(request)

class HandlerA(BaseHandler):
    nb_request = 0
    def handle(self, request):
        self.nb_request += 1
        if 'a' in request:
            print('handler a')
        else:
            super().handle(request)

class HandlerB(BaseHandler):
    nb_request = 0
    def handle(self, request):
        self.nb_request += 1
        if 'b' in request:
            print('handler b')
        else:
            super().handle(request)

class HandlerC(BaseHandler):
    nb_request = 0
    def handle(self, request):
        self.nb_request += 1
        if 'c' in request:
            print('handler c')
        else:
            super().handle(request)

if __name__ == '__main__':
    h1 = HandlerA()
    h2 = HandlerB()
    h3 = HandlerC()

    h1.set_next(h2)
    h2.set_next(h3)

    request = {'a':1}
    h1.handle(request)
    request = {'b':1}
    h1.handle(request)
    request = {'c':1}
    h1.handle(request)
    request = {'b':1, 'b':1}
    h1.handle(request)
    print(h1.nb_request, h2.nb_request, h3.nb_request)
