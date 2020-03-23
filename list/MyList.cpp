#include "MyList.h"
#include "Node.h"
#include <iostream>

template<typename T>
MyList<T>::MyList()
{
	tail = nullptr;
	head = nullptr;
	size = 0;
}

template<typename T>
void MyList<T>::push_front(T data)
{
	if (size == 0)
	{
		head = tail = new Node <T>(data, head, tail);
	}
	else if (size == 1)
	{
		head = new Node <T>(data, head);
		tail->prev = head;
	}
	else
	{
		Node<T> *new_head = head;
		head = new Node<T>(data, head);
		new_head->prev = head;
	}

	size++;
}

template<typename T>
void MyList<T>::push_back(T data)
{
	if (size == 0)
	{
		head = tail = new Node <T>(data);
	}
	else if (size == 1)
	{
		tail = new Node <T>(data, nullptr, tail);
		head->next = tail;
	}
	else
	{
		Node<T> *new_tail_node = tail;
		new_tail_node = new Node <T>(data, nullptr, tail);
		tail->next = new_tail_node;
		tail = new_tail_node;
	}

	size++;
}

template<typename T>
void MyList<T>::insert(int pos, T data)
{
	if (pos == 0)
	{
		push_front(data);
	}
	else if (pos == size)
	{
		push_back(data);
	}
	else
	{
		Node<T> *pos_node = head;
		for (int i = 0; i < pos - 1; i++)
		{
			pos_node = pos_node->next;
		}

		Node<T> *new_node = new Node<T>(data, pos_node->next, pos_node);
		pos_node->next = new_node;
		Node<T> *Next_pos_node = new_node->next;
		Next_pos_node->prev = new_node;

		size++;
	}
	
}

template<typename T>
void MyList<T>::pop_back()
{
	if (size > 1)
	{
		Node <T> *temp = tail;
		tail = tail->prev;
		delete temp;
	}
	else
	{
		Node<T> *temp = tail;
		tail = head = tail->prev;
		delete temp;
	}

	size--;
}

template<typename T>
void MyList<T>::pop_front()
{
	if (size > 1)
	{
		Node <T> *temp = head;
		head = head->next;
		delete temp;
	}
	else
	{
		Node <T> *temp = head;
		tail = head = head->next;
		delete temp;
	}

	size--;
}

template<typename T>
void MyList<T>::clear()
{
	for (size_t i = size; i > 0; i--)
	{
		pop_back();
	}
}

template<typename T>
void MyList<T>::print()
{
	Node<T> *temp_node = head;
	for (size_t i = 0; i < size; i++)
	{
		std::cout << temp_node->data << ' ';
		temp_node = temp_node->next;
	}
	std::cout << '\n';
}

template<typename T>
T& MyList<T>::operator[] (int index)
{
	if (index <= size / 2)
	{
		Node <T> *index_node = this->head;

		for(int i = 0; i < index; i++)
		{				
			index_node = index_node->next;
		}

		return index_node->data;
	}
	else
	{
		Node <T> *index_node = this->tail;
		for(int i = size - 1; i > index; i--)
		{
			index_node = index_node->prev;
		}
		return index_node->data;
	}
	
}

template<typename T>
int MyList<T>::get_size()
{
	return size;
}


template<typename T>
MyList<T>::~MyList()
{
	clear();
}


template class MyList<int>;
template class MyList<float>;
template class MyList<double>;
template class MyList<char>;