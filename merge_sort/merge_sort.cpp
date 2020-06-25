#include <iostream>
#include <vector>

using namespace std;


template<typename InputIt, typename OutputIt>
void merge(InputIt first_begin, InputIt first_end,
	InputIt second_begin, InputIt second_end,
	OutputIt out_begin)
{
	while (first_begin != first_end && second_begin != second_end)
	{
		if (*first_begin <= *second_begin)
		{
			*out_begin = *first_begin;
			first_begin++;
		}
		else
		{
			*out_begin = *second_begin;
			second_begin++;
		}

		out_begin++;
	}

	while (first_begin != first_end)
	{
		*out_begin = *first_begin;
		first_begin++;
		out_begin++;
	}

	while (second_begin != second_end)
	{
		*out_begin = *second_begin;
		second_begin++;
		out_begin++;
	}
}


template <typename RandomIt>
void MergeSort(RandomIt range_begin, RandomIt range_end)
{
	if ((range_end - range_begin) > 1)
	{
		int mid = (range_end - range_begin) / 2;
		vector<typename RandomIt::value_type> left(range_begin, range_begin + mid);
		vector<typename RandomIt::value_type> right(range_begin + mid, range_end);

		MergeSort(left.begin(), left.end());
		MergeSort(right.begin(), right.end());

		merge(left.begin(), left.end(), right.begin(), right.end(), range_begin);
	}
}


int main()
{
	vector<int> vec = { 3, 5, 1, 4, 7 };
	MergeSort(vec.begin(), vec.end());

	for (const auto& i : vec)
		cout << i << " ";

	return 0;
}
