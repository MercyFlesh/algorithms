#include <iostream>
#include <vector>
#include <random>

using namespace std;


int get_min_run(int n)
{
	int flag = 0;

	while (n >= 64)
	{
		flag |= n & 1;
		n >>= 1;
	}

	return n + flag;
}


template <typename RandomIt>
void merge(RandomIt first_begin, RandomIt first_end,
	RandomIt second_begin, RandomIt second_end, RandomIt output_begin)
{
	if (*(first_end - 1) <= *second_begin || *first_begin >= *(second_end - 1))
		return;
	
	while ((first_begin != first_end) && (second_begin != second_end))
	{
		if (*(first_end - 1) <= *second_begin)
		{
			copy(first_begin, first_end, output_begin);
			output_begin += (first_end - first_begin);
			copy(second_begin, second_end, output_begin);
			return;
		}
		else if (*first_begin >= *(second_end - 1))
		{
			copy(second_begin, second_end, output_begin);
			output_begin += (second_end - second_begin);
			copy(first_begin, first_end, output_begin);
			return;
		}
		else
		{
			if (*first_begin < *second_begin)
			{
				*output_begin = *first_begin;
				first_begin++;
			}
			else
			{
				*output_begin = *second_begin;
				second_begin++;
			}

			output_begin++;
		}	
	}

	for (; first_begin != first_end; first_begin++, output_begin++)
		*output_begin = *first_begin;

	for (; second_begin != second_end; second_begin++, output_begin++)
		*output_begin = *second_begin;
}


template <typename RandomIt>
void isertion_sort(RandomIt begin, RandomIt end)
{
	for (RandomIt i = begin + 1; i != end; i++)
	{
		RandomIt j = i - 1;
		typename RandomIt::value_type temp = *i;

		while ((*j > temp) && (j != begin))
		{
			*(j + 1) = *j;
			j--;
		}

		if ((j == begin) && (*j > temp))
		{
			*(j + 1) = *j;
			*j = temp;
		}
		else
		{
			*(j + 1) = temp;
		}
	}
}


template<typename T>
void timsort(vector<T>& vec)
{
	using VecIter = typename vector<T>::iterator;
	int data_size = vec.size();

	if (data_size > 1)
	{
		int min_run = get_min_run(data_size);

		VecIter it = vec.begin();
		while (it != vec.end())
		{
			int segment_size = min_run <= (vec.end() - it) ? min_run : vec.end() - it;
			isertion_sort(it, it + segment_size);
			it += segment_size;
		}

		int run_size = min_run;
		while (run_size < data_size)
		{
			for (int i = 0; i < data_size; i += run_size * 2)
			{
				int segment_size_first = run_size <= data_size - i ? run_size : vec.size() - i;
				int segment_size_second = run_size <= data_size - i - segment_size_first ? run_size : data_size - i - segment_size_first;
				
				if (segment_size_second > 0)
				{
					vector<T> temp_first, temp_second;
				
					pair<VecIter, VecIter> first = { vec.begin() + i, vec.begin() + i + segment_size_first - 1 };
					pair<VecIter, VecIter> second = { vec.begin() + i + segment_size_first, vec.begin() + i + segment_size_first + segment_size_second - 1 };
					copy(first.first, first.second, back_inserter(temp_first));
					copy(second.first, second.second, back_inserter(temp_second));

					merge(temp_first.begin(), temp_first.end(),
						temp_second.begin(), temp_second.end(), vec.begin() + i);
				}
			}

			run_size *= 2;
		}
	}
}


int main()
{
	random_device rd;
	uniform_int_distribution<int> uid(0, 10000000);
	
	vector<int> vec(100000);
	for (auto& i : vec)
	{
		i = uid(rd);
	}

	timsort(vec);

	for (const auto& it : vec)
	{
		cout << it << " ";
	}

	return 0;
}