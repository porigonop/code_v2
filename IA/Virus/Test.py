
class Test():
    def __init__(self):
        self.msg = ""

    def run_test(self, function, data, expected):
        for i in range(data):
            if function(data) != expected:
                print("failure")
                self.msg += "function(" + str(data)+ ") doesn't return "+ str(expected)\
                 + "\n"+"-"*10+"\n"
        self.msg += "all "+ len(data)+ "test effectued"



if __name__ == "__main__":
    def foo(fct):
        print(fct)
        return fct(3)

    def f(d):
        return d

    print(foo(f))