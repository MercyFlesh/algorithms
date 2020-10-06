#include <iostream>
#include <string_view>
#include <vector>

using namespace std;


vector<size_t> prefix_func(string_view str)
{
	size_t length = str.size();
	vector<size_t> prefix(length);

	prefix[0] = 0;
	for (size_t i = 1, j = 0; i < length;)
	{
		if (str[i] == str[j])
		{
			prefix[i] = j + 1;
			i++;
			j++;
		}
		else if (j == 0)
		{
			prefix[i] = 0;
			i++;
		}
		else
			j = prefix[j - 1];
	}

	return prefix;
}

vector<size_t> kamp_search(const string& text, const string& find_substr)
{
	size_t find_length = find_substr.size();
	vector<size_t> find_pos;
	vector<size_t> prefix(prefix_func(find_substr + "#" + text));

	for (size_t i = 0; i < text.size(); ++i)
		if (prefix[find_length + 1 + i] == find_length)
			find_pos.emplace_back(i + 1 - find_length);

	return find_pos;
}

int main()
{
	string str = "abcdabcjabc";
	vector<size_t> pos = kamp_search(str, "abc");

	for (auto i : pos)
		cout << i << " ";
	cout << endl;

	return 0;
}