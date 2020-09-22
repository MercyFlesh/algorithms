#pragma once
#include <memory>


template <typename T>
class MyStack
{
public:
	MyStack();
	MyStack(const MyStack<T>& other);
	MyStack(MyStack<T>&& other) noexcept;
	void operator= (const MyStack<T>& other);
	void operator= (MyStack<T>&& otheer) noexcept;
	~MyStack();

	void push(const T& num);
	void pop();
	T top();

	int size() const;
	bool empty() const;

private:
	std::unique_ptr<T[]> data;
	unsigned size_;
	unsigned capacity;	
};
