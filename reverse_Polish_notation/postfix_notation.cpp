#include <iostream>
#include <string>
#include <map>
#include <stack>

using namespace std;

map<char, int> priority = { 
	{'^', 4}, 
	{'*', 3}, {'/', 3},
	{'+', 2}, {'-', 2},
	{'(', 1}, {')', 1}
};

string to_postfix(const string& expression)
{
	string postfix;
	stack<char> some_stack;
	int count_bracket = 0;

	
	for (const auto& symb : expression)
	{
		if (isalpha(symb) || isdigit(symb))
		{
			postfix += symb;
		}	
		else if (symb == '^' || symb == '*' || symb == '/' || symb == '+' || symb == '-')
		{
			while (!some_stack.empty() && some_stack.top() != '(' && priority[some_stack.top()] >= priority[symb])
			{
				postfix += some_stack.top();
				some_stack.pop();
			}
			
			some_stack.push(symb);
		}
		else if (symb == '(')
		{
			count_bracket++;
			some_stack.push(symb);
		}
		else if (symb == ')')
		{
			if (count_bracket == 0)
				throw invalid_argument("incorrect exprection");

			while (!some_stack.empty() && some_stack.top() != '(')
			{
				postfix += some_stack.top();
				some_stack.pop();
			}

			--count_bracket;
			some_stack.pop();
		}
	}

	if (count_bracket == 0)
	{
		while (!some_stack.empty())
		{
			postfix += some_stack.top();
			some_stack.pop();
		}
	}
	else
		throw invalid_argument("incorrect exprection");

	return postfix;
}


int main(int argc, char* argv[])
{
	string expression;
	getline(cin, expression);
	
	try
	{
		cout << to_postfix(expression) << endl;
	}
	catch (invalid_argument& ex)
	{
		cout << ex.what() << endl;
	}
		

	return 0;
}