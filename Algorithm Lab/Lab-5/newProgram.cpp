#include <bits/stdc++.h>
#include <initializer_list>
#include <scoped_allocator>
#include <system_error>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
//#include <gmpxx.h>
using namespace std;
typedef long long ll;
typedef long long int int64;
#define input(v) for(auto &i : v) cin >> i
#define line(x) getline(cin, x)
#define endl "\n"
#define exit exit(EXIT_SUCCESS);
#define revArray(x, n) reverse(x, x+n);
#define all(x)  x.begin(), x.end()
#define lowercase(s) transform(s.begin(), s.end(),s.begin(), ::tolower)
#define uppercase(s) transform(s.begin(), s.end(),s.begin(), ::toupper)
#define multi_string cin.ignore(); 
const long long MOD = 1e9+7;

string meow (string &s) {
    s.erase(remove(s.begin(), s.end(), ' '), s.end());
    return s;
}
struct item {
    int weight, profit;
};
int main() { 
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, w; cin >> n >> w;
    vector<item> items(n);
    for (int i=0; i<n; i++) {
        cin >> items[i].weight >> items[i].profit;
    }
    vector<int> dp(w+1, 0);
    for (int i=0; i<n; i++) {
        for (int j=w; j>=items[i].weight; j--) {
            dp[j] = max(dp[j], dp[j-items[i].weight]+items[i].profit);
        }
    }
    cout << dp[w] << endl;
    return (EXIT_SUCCESS);
}