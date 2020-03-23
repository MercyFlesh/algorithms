#include <iostream>
#include <random>

using namespace std;

void quicksort(int* arr, int size)
{
	int i = 0;
	int j = size - 1;
	int center = arr[size / 2];
	int temp = 0;

	while (i <= j)
	{
		while (arr[i] < center)
		{
			i++;
		}
		while (arr[j] > center)
		{
			j--;
		}
		if (i <= j)
		{
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}

	if (j > 0)
	{
		quicksort(arr, j + 1);
	}
	if (size > i)
	{
		quicksort(arr + i, size - i);
	}
}

int main()
{
	default_random_engine gen;
	uniform_int_distribution<int> distr(-1000, 1000);

	const int size_arr = 1000;
	int arr[size_arr];
	for (int i = 0; i < size_arr; ++i)
		arr[i] = distr(gen);

	quicksort(arr, size_arr);
	
	for (int i = 0; i < size(arr); ++i)
		cout << arr[i] << " ";
	cout << endl;
}