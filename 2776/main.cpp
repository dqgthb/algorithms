#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cassert>

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
#define TEST int t; cin>>t; while(t--)
#define init(arr,val) memset(arr,val,sizeof(arr))
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loopr(i,a,b) for(int i=a;i>=b;i--)
#define loops(i,a,b,step) for(int i=a;i<b;i+=step)
#define looprs(i,a,b,step) for(int i=a;i>=b;i-=step)

#define V vector
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
#define ST set
#define MS multiset
#define UM unordered_map
#define mp make_pair
#define pb push_back
#define pf push_front
#define eb emplace_back
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

int N, M, tmp;
V<int> A;

const int BUF_SZ = 1 << 15;
inline namespace Input {
char buf[BUF_SZ];
int pos;
int len;
char next_char() {
	if (pos == len) {
		pos = 0;
		len = (int)fread(buf, 1, BUF_SZ, stdin);
		if (!len) {
			return EOF;
		}
	}
	return buf[pos++];
}

int read_int() {
	int x;
	char ch;
	int sgn = 1;
	while (!isdigit(ch = next_char())) {
		if (ch == '-') {
			sgn *= -1;
		}
	}
	x = ch - '0';
	while (isdigit(ch = next_char())) {
		x = x * 10 + (ch - '0');
	}
	return x * sgn;
}
} // namespace Input
inline namespace Output {
char buf[BUF_SZ];
int pos;

void flush_out() {
	fwrite(buf, 1, pos, stdout);
	pos = 0;
}

void write_char(char c) {
	if (pos == BUF_SZ) {
		flush_out();
	}
	buf[pos++] = c;
}

void write_int(int x) {
	static char num_buf[100];
	if (x < 0) {
		write_char('-');
		x *= -1;
	}
	int len = 0;
	for (; x >= 10; x /= 10) {
		num_buf[len++] = (char)('0' + (x % 10));
	}
	write_char((char)('0' + x));
	while (len) {
		write_char(num_buf[--len]);
	}
	write_char('\n');
}

// auto-flush output when program exits
void init_output() { assert(atexit(flush_out) == 0); }
} // namespace Output


int readInt(){
    return read_int();
}


int readInt2(){
    int a;
    scanf("%d", &a);
    return a;
}


template<typename T>
auto bisectLeft(const vector<T>& a, int val){
    auto l = 0;
    auto r = N;
    T mVal;
    while (l < r){
        auto m = l + r >> 1;
        mVal = a[m];

        if (mVal < val){
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l;
}


void solve(){
    N = readInt();
    A.clear();
    A.reserve(N);
    loop(i, 0, N){
        tmp = readInt();
        A.eb(tmp);
    }

    sort(all(A));
    M = readInt();
    loop(i, 0, M){
        tmp = readInt();

        auto&& it = lower_bound(all(A), tmp);
        if (it != A.end() && *it == tmp) {
        //auto idx = bisectLeft(A, tmp);
        //if (idx != N && A[idx] == tmp){
            //cout << "1\n";
            write_int(1);
        } else {
            //cout << "0\n";
            write_int(0);
        }
    }
}


int main(int argc, const char **argv){
    init_output();
    FAST

    #ifndef ONLINE_JUDGE
        if (argc == 2){
            ifstream ff(argv[1]);
            assert(ff.good());
            //cout << argv[1] << " is open\n";
            freopen(argv[1], "r", stdin);
        } else {
            //cout << "basic input file i is open\n";
            FILE_READ_IN
        }

        //cout << "unordered_set, set all failed...\n";
    #endif

    int T = readInt();
    loop(i, 0, T){
        solve();
    }

    return 0;
}
