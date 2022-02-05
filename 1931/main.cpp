#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>

using namespace std;

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).end(), (a).begin()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<PII> VPII;
typedef long long int int64;
typedef long int int32;
#define F first
#define S second

#define PI 3.14159265358979

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int N;
VPII A;

void solve()
{
    cin >> N;
    while (N--)
    {
        int a, b;
        cin >> a >> b;
        A.emplace_back(a, b);
    }

    sort(all(A),
         [](PII const &a, PII const &b)
         {
             return a.F < b.F;
         });


    sort(all(A),
         [](PII const &a, PII const &b)
         {
             return a.S < b.S;
         });

    int cnt = 0;
    int finish = 0;
    for (auto && p: A){
        if (finish <= p.F) {
            finish = p.S;
            ++cnt;
        }
    }

    cout << cnt <<'\n';
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    #ifndef ONLINE_JUDGE
        freopen("i", "r", stdin);
    #endif

    int tc = 1;
    //cin >> tc;
    for (int t = 0; t < tc; t++){
        solve();
    }
    return 0;
}
