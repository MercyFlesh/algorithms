#include <iostream>
#include <vector>

using namespace std;

template<typename T>
vector<T> merge(vector<T> &arr, vector<T> l, vector<T> r, int left, int right) 
{
	int i = 0, j = 0, k = 0;
	
	while (i < left && j < right) 
	{
		if (l[i] <= r[j])
			arr[k++] = l[i++];
		else
			arr[k++] = r[j++];
	}
	
	while (i < left)
		arr[k++] = l[i++];

	while (j < right)
		arr[k++] = r[j++];

	return arr;
}


template<typename T>
vector<T> mergeSort(vector<T> &arr, int n)
{
	if (n < 2)
		return arr;

	int mid = n / 2;
	vector<T> l(mid);
	vector<T> r(n - mid);

	for (int i = 0; i < mid; i++)
		l[i] = arr[i];

	for (int i = mid; i < n; i++)
		r[i - mid] = arr[i];

	mergeSort(l, mid);
	mergeSort(r, n - mid);

	return merge(arr, l, r, mid, n - mid);
}


int main(int argc, char* argv[])
{	
	vector<int> vec = { 12, 11, 13, 5, 6, 7 };
	mergeSort(vec, 6);
	
	for (auto n : vec)
		cout << n << " ";
	cout << endl;

	return 0;
}