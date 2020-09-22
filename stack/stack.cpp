#include "MyStack.hpp"
#include <utility>

using namespace std;


template<typename T> 
MyStack<T>::MyStack()
	: size_(0), capacity(1), data(new T[1]){}


template<typename T>
MyStack<T>::MyStack(const MyStack<T>& other)
	: size_(other.size_), capacity(other.capacity)
{
	data.reset(new T[capacity]);
	for (size_t i = 0; i < size_; i++)
		data[i] = other.data[i];
}


template<typename T>
MyStack<T>::MyStack(MyStack<T>&& other) noexcept
	: size_(other.size_), capacity(other.capacity), 
	data(move(other.data))
{
	other.size_ = other.capacity = 0;
}


template<typename T>
void MyStack<T>::operator= (const MyStack<T>& other)
{
	size_ = other.size_;
	capacity = other.capacity;
	data.reset(new T[capacity]);

	for (size_t i = 0; i < size_; i++)
		data[i] = other.data[i];
}


template<typename T>
void MyStack<T>::operator= (MyStack<T>&& other) noexcept
{
	size_ = other.size_;
	capacity = other.capacity;
	data = move(other.data);

	other.size_ = other.capacity = 0;
}


template<typename T>
void MyStack<T>::push(const T& newData)
{
	if (size_ < capacity)
	{
		data[size_] = newData;
		size_++;
	}
	else
	{
		unique_ptr<T[]> tmp(new T[capacity * 2]);
		for (size_t i = 0; i < size_; i++)
			tmp[i] = data[i];
		
		data = move(tmp);
		data[size_] = newData;
		capacity *= 2;
		size_++;
	}
}


template<typename T>
void MyStack<T>::pop()
{
	if (size_ > 0)
	{
		unique_ptr<T[]> tmp(new T[capacity]);
		for (size_t i = 0; i < size_ - 1; i++)
			tmp[i] = move(data[i]);
		
		data = move(tmp);
		size_--;
	}
}


template<typename T>
T MyStack<T>::top()
{
	return data[size_ - 1];
}


template<typename T>
int MyStack<T>::size() const
{
	return size_;
}


template<typename T>
bool MyStack<T>::empty() const
{
	return size_ == 0;
}


template<typename T>
MyStack<T>::~MyStack()
{
	data.reset();
}


template class MyStack<int>;
template class MyStack<double>;
template class MyStack<float>;
template class MyStack<char>;