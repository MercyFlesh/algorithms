#include <iostream>
#include <vector>

using namespace std;

template<typename T>
void shell_sort(vector<T>& data)
{
	for (size_t i = static_cast<size_t>(data.size() / 2); i > 0; i /= 2)
	{
		for (size_t j = i; j < data.size(); j++)
		{
			for (int k = j - i; k >= 0; k -= i)
			{
				if (data[k + i] >= data[k])
					break;
				else
					swap(data[k], data[k + i]);
			}
		}
	}
}

int main()
{
	vector<int> data = { 5, 1, 4, 3, 9, 6, 2, 8, 7 };
	shell_sort(data);

	for (const int& i : data)
		cout << i << " ";
	cout << endl;

	return 0;
}