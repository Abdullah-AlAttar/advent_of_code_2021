#include <iostream>
#include <vector>
#include <fstream>
#include <bitset>
using namespace std;

vector<string> read_input(std::string path)
{
	std::ifstream in(path.c_str());
	// Check if object is valid
	if (!in)
	{
		std::cerr << "Cannot open the File : " << path << std::endl;
		return {};
	}
	std::string str;
	std::vector<string> res;
	while (std::getline(in, str))
	{
		res.push_back(str);
	}
	return res;
}

int main(int argc, char **argv)
{

	vector<string> input = read_input(argv[1]);

	auto get_nth_bit = [](const vector<string> &input, int n)
	{
		int zero_count = 0;
		for (size_t i = 0; i < input.size(); ++i)
		{
			if (input[i][n] == '0')
			{
				zero_count++;
			}
		}
		int ones_count = input.size() - zero_count;
		return zero_count > ones_count ? 0 : 1;
	};
	int eps = 0, gamma = 0;

	for (size_t i = 0; i < input[0].size(); ++i)
	{
		int dir = input[0].size() - i - 1;
		int nth_bit = get_nth_bit(input, i);
		gamma = gamma | (nth_bit << dir);
		eps = eps | (abs(nth_bit - 1) << dir);
		// std::bitset<8> tmp(gamma);
		// std::cout << tmp << std::endl;
	}
	std::cout << gamma << " " << eps << std::endl;
	std::cout << gamma * eps << endl;
}
