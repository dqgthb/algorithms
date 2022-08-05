#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

int N, M, tmp;


template <typename T>
int binLeft(std::vector<T>& arr, T val){
    int L = 0;
    int R = arr.size();

    while (L < R){
        int M = L + R >> 1;
        int mid = arr[M];
        if (mid <= val){
            L = M + 1;
        } else {
            R = M;
        }
    }
    return L;
}


int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream ifile;
    ifile.open("i");
    if (ifile) {
        freopen("i", "r", stdin);
    }

    cin >> N;
    vector<int> A;
    A.reserve(N);

    for (int i = 0; i < N; ++i){
        cin >> tmp;
        A.emplace_back(tmp);
    }

    std::sort(A.begin(), A.end());

    cin >> M;
    vector <int> O;
    O.reserve(M);

    for (int i = 0; i < N; ++i){
        cin >> tmp;
        int idx = binLeft<int>(A, tmp);
        if (idx != 0 && A[idx-1] == tmp){
            O.push_back(1);
        } else {
            O.push_back(0);
        }
    }

    for (auto i : O){
        cout << i << ' ';
    }
    cout << '\n';


    return 0;
}
