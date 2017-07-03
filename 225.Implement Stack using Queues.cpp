class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q1.push(x);
        t = x;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        auto ret = t;
        while (q1.size()>2)
        {
            q2.push(q1.front());
            q1.pop();
        }
        t = q1.front();
        q1.pop();
        if(!q1.empty())q1.pop(), q2.push(t);
        swap(q1, q2);
        return ret;
    }
    
    /** Get the top element. */
    int top() {
        return t;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty();
    }
protected:
    queue<int>q1, q2;
    int t;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */