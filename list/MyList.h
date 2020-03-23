#ifndef LIST
#define LIST

#include "Node.h"

template <typename T>
class MyList
{
private:
	int size;
	Node<T> *tail;
	Node<T> *head;
public:
	MyList();
	void push_front(T data);
	void push_back(T data);
	void insert(int pos, T data);
	void pop_back();
	void pop_front();
	void clear();
	void print();
	int get_size();
	T& operator[] (int index);
	~MyList();
};

#endif