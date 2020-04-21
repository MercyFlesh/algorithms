#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


void bucket_sort(vector<double>& vec)
{
	vector<vector<double>> buckets(vec.size());

	for (const auto& val : vec)
	{
		int index = int(val * vec.size());
		buckets[index].push_back(val);
	}

	for (auto& bucket : buckets)
		sort(begin(bucket), end(bucket));

	for (int i = 0, id = 0; i < vec.size(); i++)
		for (const auto& val : buckets[i])
			vec[id++] = val;
}


int main()
{
	vector<double> example_vec = { 0.89, 0.56, 0.65, 0.12, 0.66, 0.34 };

	bucket_sort(example_vec);

	for (const auto& val : example_vec)
		cout << val << " ";
	cout << endl;

	return 0;
}