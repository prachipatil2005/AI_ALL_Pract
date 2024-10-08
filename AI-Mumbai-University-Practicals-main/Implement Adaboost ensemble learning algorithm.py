class Perceptron :
    def __init__(self, a,b,c,tval):
        self.x = a #nput vector
        self.y = b # activation result
        self.result = c # summation result
        self.threshold = tval
        self.w= []
    def h(self,tw): # calculating summation hypothesis function
        hresult= []
        for i in range(0 , len(self.result)):
            hresult.append(0)
            for j in range(0,len(tw)):
                hresult[i]=hresult[i]+(tw[j][i]*self.x[j][i])   
        return hresult
    def checkthreshold(self, hresult):  # hard threshold function technique for regression
        flag = True
        actfun =[]
        for i in range(0 , len(self.result)) :            
            if (hresult[i] <= self.threshold ):
                actfun.append(0)
            else :
                actfun.append(1)
        print("Ans:",hresult)
        print("Result act fun:", actfun)

        for i in range(0 , len(self.x)) :
            if (actfun[i] != self.result[i]) :
                return False
        return True   
    def training(self, tw, alpha):#passing w vector and alpha value
        i=1
        while i<=10 : # Max 10 attempts                        
                print("Attempt ", i  )
                hresult = self.h(tw) 
                if(self.checkthreshold(hresult)) : #if training result matches the test result                   
                    self.w = tw                                     
                    print("In Attempt number ", i,  ", i got it! I think i have learnt enough: w0-->")
                    for x in range(0,len(self.w)):
                        print("w",x,"->",self.w[x])
                    break
                i = i +1      
                # Changing values of w to reduce error/loss using batch gradient descent learning rule
                for j in range(0,len(self.result)) :
                    for k in range(0,len(tw)):
                        sum=0
                        for n in range(0,len(tw)):
                            sum=sum+(self.result[j]-hresult[j])*self.x[n][j]  
                        tw[k][j] = tw[k][j] + alpha*sum
        if(i>=100):
            print("I am exhausted, tried 100 iterations! plz change something else...")        
a = [[1,1,1,1],[0,0,1,1],[0,1,0,1]]#x vector,x0 is dummy
b = [0,1,1,1]
c = [0.5,0.7,1.3,1.5]#sample h values
p = Perceptron(a,b,c,0.5)
print("Whether reservation is done =", p.x[0])
print("Whether raining outside=", p.x[1])
print("With threshold value =", p.threshold)
r=p.h([[0.5,0.5,0.5,0.5],[0.8,0.8,0.8,0.8],[0.2,0.2,0.2,0.2]])
print("Status:",p.checkthreshold(r))
print("Trying with alpha=0.01 -->")
p.training([[0.7,0.7,0.7,0.7],[0.5,0.5,0.5,0.5],[0.4,0.4,0.4,0.4]],0.01)
print("Trying with alpha=0.5 -->")
p.training([[0.7,0.7,0.7,0.7],[0.5,0.5,0.5,0.5],[0.4,0.4,0.4,0.4]],0.5)
print("Trying with new data-->")
p.training([[0.2,0.2,0.2,0.2],[0.3,0.3,0.3,0.3],[0.5,0.5,0.5,0.5]],0.01)