#ifndef NODE
#define NODE

template<typename T>
struct Node
{
	Node *next;
	Node *prev;
	T data;

	Node(T data = T(), Node *next = nullptr, Node *prev = nullptr)
	{
		this->data = data;
		this->next = next;
		this->prev = prev;
	}
};

#endif