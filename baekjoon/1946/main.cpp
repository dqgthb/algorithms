#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
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
#include <cassert>
#include <cmath>
#define FAST ios_base::sync_with_stdio(false);cin.tie();cout.tie();
#define FILE_READ_IN freopen("i","r",stdin);
#define FILE_READ_OUT freopen("o","w",stdout);

using namespace std;

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).end(), (a).begin()
#define test int t; cin>>t; while(t--)
#define init(arr,val) memset(arr,val,sizeof(arr))
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loopr(i,a,b) for(int i=a;i>=b;i--)
#define loops(i,a,b,step) for(int i=a;i<b;i+=step)
#define looprs(i,a,b,step) for(int i=a;i>=b;i-=step)

#define L list
#define V vector
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
#define D deque
#define ST set
#define MS multiset
#define M map
#define UM unordered_map
#define mp make_pair
#define pb push_back
#define pf push_front
#define eb emplace_back
#define MM multimap
#define F first
#define S second
#define IT iterator
#define RIT reverse_iterator
#define P pair
#define PLL pair<long long, long long>
#define PII pair<int, int>
typedef long long int int64;
typedef long int int32;

#define PI 3.14159265358979

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ll MAXINIT = -2e9 + 9;
const ll MININIT = 2e9 + 9;

int N;
V<PII> A;

void solve(){
    cin >> N;
    A.clear();
    A.reserve(N);

    loop(i, 0, N){
        int a, b;
        cin >> a >> b;
        A.eb(a, b);
    }

    sort(all(A));

    int cnt = 0;
    int document = MININIT;
    int interview = MININIT;

    for (auto&& [docScore, intScore]: A){
        if (interview > intScore){
            ++cnt;
            interview = intScore;
        }
    }
    cout << cnt << '\n';
}

int main(int argc, const char **argv){
    FAST

    #ifndef ONLINE_JUDGE
        if (argc == 2){
            ifstream ff(argv[1]);
            assert(ff.good());
            cout << argv[1] << " is open\n";
            freopen(argv[1], "r", stdin);
        } else {
            cout << "basic input file i is open\n";
            FILE_READ_IN
        }

        cout << "there are a way to solve this problem in linear time...\n";
    #endif

    test{
        solve();
    }

    return 0;
}
