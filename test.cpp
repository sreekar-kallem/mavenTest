#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int getMaximumNutrition(int W, vector<int> value, vector<int> weight, int x) {
	int n=value.size();
	int dp[n + 1][W + 1][x + 1];

	memset(dp, 0, sizeof(dp));
	for(int i = 1;i <= n; i++)
	{
		for(int j = 1;j <= W; j++)
		{
			int lim = x;
			if(lim > i)
			{
				lim = i;
			}
			for(int k = 0;k <= lim; k++)
			{
				dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j][k]);
				int val = j - (weight[i - 1] / 2);
				if(val >= 0 && k > 0)
				{
					dp[i][j][k] = max(dp[i - 1][val][k - 1]+value[i - 1], dp[i][j][k]);
				}
				val = j - weight[i - 1];
				if(val >= 0)
				{
					dp[i][j][k] = max(dp[i - 1][val][k] + value[i - 1], dp[i][j][k]);
				}
			}
		}
	}
	return dp[n][W][x];
}
int main() {
	vector<int> value = {17, 20, 10, 15};
	vector<int> weight = {4, 2, 7, 5};
	int x = 1;
	int W = 4;
	cout << getMaximumNutrition(W, value, weight, x);
	return 0;
}
