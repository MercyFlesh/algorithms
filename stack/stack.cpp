#include "stack.h"
#include <iostream>

template<typename T> 
stack<T>::stack()
{
	last_count = 0;
	max_count = 1;
	data = new T[max_count];
}

template<typename T>
void stack<T>::push(T newData)
{
	if (last_count < max_count)
	{
		data[last_count] = newData;
		last_count++;
	}
	else
	{
		T *new_data = new T[max_count + 1];
		memmove(new_data, data, max_count * sizeof(T));
		delete[] data;
		data = new_data;
		data[last_count] = newData;
		max_count++;
		last_count++;
	}
}

template<typename T>
void stack<T>::pop()
{
	if (last_count > 0)
	{
		last_count--;
	}
}

template<typename T>
T stack<T>::top()
{
	return data[last_count - 1];
}


template<typename T>
int stack<T>::size()
{
	return last_count;
}

template<typename T>
bool stack<T>::empty()
{
	if (last_count != 0)
		return true;
	else
		return false;
}




template<typename T>
void stack<T>::swap(stack<T> &stack2)
{
	std::swap(last_count, stack2.last_count);
	std::swap(max_count, stack2.max_count);
	std::swap(data, stack2.data);
}

template<typename T>
void stack<T>::print()
{
	for (int i = 0; i < last_count; i++)
		std::cout << data[i];
}

template<typename T>
stack<T>::~stack()
{
	delete[] data;
}

template class stack<int>;
template class stack<double>;
template class stack<float>;
template class stack<char>;