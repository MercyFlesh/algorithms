#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int	binary_search(const vector<int>& vec, int find_key)
{

	if (is_sorted(vec.begin(), vec.end()))
	{
		int left = 0, right = vec.size(), mid;
	
		while (left <= right)
		{
		
			mid = (left + right) / 2;

			if (mid > vec.size() - 1)
				break;

			if (vec[mid] == find_key)
				return mid;
			else if (find_key < vec[mid])
				right = mid - 1;
			else
				left = mid + 1;
		}
	}
	
	return -1;
}


int main()
{
	vector<int> vec = { 1, 2, 4, 5, 6 };
	cout << binary_search(vec, 5) << endl;

	return 0;
}