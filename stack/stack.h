#ifndef STACK
#define STACK

template <typename T>
class stack
{
private:
	T *data;
	int last_count;
	int max_count;

public:
	stack();
	void push(T num);
	void pop();
	T top();
	int size();
	bool empty();
	void swap(stack<T> &stak2);
	void print();

	~stack();
};

#endif 
