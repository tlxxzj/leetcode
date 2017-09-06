class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder():n(0) {
        
    }
    
    void addNum(int num) {
        if(n&1) r.push(num);
        else l.push(num);
        if (n++ > 1)
        {
            while (l.top() > r.top())
            {
                int a = l.top(), b = r.top();
                l.pop(); r.pop();
                l.push(b); r.push(a);
            }
        }
    }
    
    double findMedian() {
        if (n&1) return (double)l.top();
        else return (l.top() + r.top()) / 2.0;
    }

private:
    priority_queue<int, vector<int>, greater<int>> r;
    priority_queue<int, vector<int>, less<int>>l;
    int n;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */