#include <iostream>
#include <vector>
#include <fstream>
#include <bitset>
using namespace std;

vector<string> read_input(std::string path)
{
	std::ifstream in(path.c_str());
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

auto get_nth_bit = [](const vector<string> &input, int n)
{
	int zero_count = 0;
	int ones_count = 0;
	for (size_t i = 0; i < input.size(); ++i)
	{
		if (input[i][n] == '0')
		{
			zero_count++;
		}
		else
		{
			ones_count++;
		}
	}
	if (ones_count == zero_count)
	{
		return -1;
	}
	return zero_count > ones_count ? 0 : 1;
};

auto discard_bit = [](const vector<string> &input, int n, int bit, bool flip)
{
	std::vector<string> output;
	if (bit == -1)
	{
		for (size_t i = 0; i < input.size(); ++i)
		{
			if (input[i][n] == '1' && flip == true)
			{
				output.push_back(input[i]);
			}
			if (input[i][n] == '0' && flip == false)
			{
				output.push_back(input[i]);
			}
		}
		return output;
	}
	char nth_bit = bit == 0 ? '0' : '1';
	for (size_t i = 0; i < input.size(); ++i)
	{
		if (input[i][n] == nth_bit)
		{
			output.push_back(input[i]);
		}
	}
	return output;
};

int get_oxygen(vector<string> input)
{
	int n = 0;
	while (input.size() > 1)
	{
		int nth_bit = get_nth_bit(input, n);
		input = discard_bit(input, n, nth_bit, true);
		n++;
	}
	char *end;
	int decimal = strtoll(input[0].c_str(), &end, 2);
	return decimal;
}

int get_co2(vector<string> input)
{
	int n = 0;
	while (input.size() > 1)
	{
		int nth_bit = get_nth_bit(input, n);
		input = discard_bit(input, n, nth_bit == -1 ? nth_bit : abs(1 - nth_bit), false);
		
		n++;
	}
	char *end;
	int decimal = strtoll(input[0].c_str(), &end, 2);
	return decimal;
}
int main(int argc, char **argv)
{

	vector<string> input = read_input(argv[1]);
	cout<< get_oxygen(input) * get_co2(input);
}
