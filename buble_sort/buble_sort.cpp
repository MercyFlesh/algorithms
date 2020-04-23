#include <iostream>
#include <vector>

using namespace std;


void buble_sort(vector<int>& vec)
{
	int tmp;
	for (int i = 0; i < vec.size(); i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (vec[i] < vec[j])
			{
				tmp = vec[j];
				vec[j] = vec[i];
				vec[i] = tmp;
			}
		}
	}
}


int main()
{
	vector<int> vec = { 5, 14, 3, 4, 9, 4, 1, 8 };

	buble_sort(vec);

	for (const auto& val : vec)
		cout << val << " ";
	cout << endl;

	return 0;
}
