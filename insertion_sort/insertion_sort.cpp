#include <iostream>
#include <vector>

using namespace std;


template <typename RandomIt>
void insertion_sort(RandomIt begin, RandomIt end)
{
	for (RandomIt i = begin+1; i != end; i++)
	{
		RandomIt j = i - 1;
		typename RandomIt::value_type temp = *i;
		
		while ((*j > temp) && (j != begin))
		{
			*(j+1) = *j;
			j--;
		}

		if ((j == begin) && (*j > temp))
		{
			*(j+1) = *j;
			*j = temp;
		}
		else
		{
			*(j+1) = temp;
		}
	}
}


int main()
{
	vector<int> a = { 5, 1, 4, 3, 9, 6, 2, 8, 7 };
	
	insertion_sort(a.begin(), a.end());
	for (const auto& i : a)
		cout << i << " ";

	return 0;
}
