class Solution {
public:

int evalRPN(vector<string>& tokens) {
	stack<long>st;
	long l, r;
	for (auto t : tokens)
	{
		char firstchar = '0';
		if (t.length() == 1)
		{
			firstchar = t[0];
		}
		switch (firstchar)
		{
		case '+':
			r = st.top(); st.pop();
			l = st.top(); st.pop();
			st.push(l + r);
			break;
		case '-':

			r = st.top(); st.pop();
			l = st.top(); st.pop();
			st.push(l - r);
			break;
		case '*':
			r = st.top(); st.pop();
			l = st.top(); st.pop();
			st.push(l*r);
			break;
		case '/':
			r = st.top(); st.pop();
			l = st.top(); st.pop();
			st.push(l / r);
			break;
		default:
			l = stol(t);
			st.push(l);
			break;
		}
	}
	return st.top();
}

};