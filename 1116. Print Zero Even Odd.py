import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock0 = threading.Lock()
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()
    
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lock0.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.lock1.release()
            else:
                self.lock2.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.lock2.acquire()
            printNumber(i)
            self.lock0.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.lock1.acquire()
            printNumber(i)
            self.lock0.release()
        