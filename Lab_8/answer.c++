#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum CacheState {
    INVALID,
    SHARED,
    EXCLUSIVE,
    MODIFIED
};

string stateToString(CacheState state) {
    switch (state) {
    case INVALID:
        return "INVALID";
    case SHARED:
        return "SHARED";
    case EXCLUSIVE:
        return "EXCLUSIVE";
    case MODIFIED:
        return "MODIFIED";
    default:
        return "UNKNOWN";
    }
}

class CacheSystem {
private:
    vector<CacheState> caches;

public:
    CacheSystem() : caches(4, INVALID) {}

    void processRead(int proc) {
        if (caches[proc] == INVALID) {
            bool otherHasData = false;
            bool anyModified = false;

            for (int i = 0; i < 4; i++) {
                if (i != proc && (caches[i] == SHARED || caches[i] == EXCLUSIVE || caches[i] == MODIFIED)) {
                    otherHasData = true;
                    if (caches[i] == MODIFIED) anyModified = true;   
                }
            }

            if (otherHasData){
                caches[proc] = SHARED;

                for (int i = 0; i < 4; i++){
                    if (caches[i] == MODIFIED){
                        caches[i] = SHARED;
                    }
                    else if (caches[i] == EXCLUSIVE) {
                        caches[i] = SHARED;
                    }
                }
            }
            else caches[proc] = EXCLUSIVE;
            
        }
    }

    void processWrite(int proc) {
        for (int i = 0; i < 4; i++) {
            if (i != proc) caches[i] = INVALID;
        }

        caches[proc] = MODIFIED;
    }

    void printStates() {
        for (int i = 0; i < 4; i++) {
            cout << "C" << (i + 1) << ": " << stateToString(caches[i]);
            if (i < 3)
                cout << ", ";
        }
        cout << endl;
    }
};

int main() {
    CacheSystem system;
    int a;
    char b;
    int c;

    while (true) {
        cout << "Enter (a b c) : ";
        cin >> a >> b >> c;

        if (a < 1 || a > 4 || (b != 'R' && b != 'W') || (c != 0 && c != 1)) {
            cout << "Invalid input. Format: a b c (a ∈ {1,2,3,4}, b ∈ {R,W}, c ∈ {0,1})" << endl;
            continue;
        }

        if (b == 'R') system.processRead(a - 1);
        else system.processWrite(a - 1);
        
        system.printStates();
        if (c == 0) break;
    }
    return 0;
}

