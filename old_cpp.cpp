#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

void clear() {
	for (int i = 0; i < 40; i ++) {
		cout << endl;
	}
}

int main() {
	ifstream key("vwllss.txt");
	int lvl=0;
	int mins,N;
	vector<pair<string,string>> levels;
	
	key >> N >> mins;
	for (int i = 0; i < N; i ++) {
		string a,b;
		key >> a >> b;
		levels.push_back({a,b});

	}
	
	clear();

	cout << "Welcome to VWLLSS!" << endl;
	cout << "Press <return> to start!" << endl;
	cin.ignore();
	
	clear();
	string correct;
	string inp;
	int tries;
	
	int score;
	for (int i = 0; i < N; i ++) {
		clear();
		cout << "STAGE " << i+1 << endl;
		tries=0;
		correct=levels[i].second;
		inp=levels[i].first;
		while (inp!=correct) {
			cout << inp << endl;
			cout << "Turn " << tries+1 << endl;
			string turn;
			int pos;
			cin >> turn >> pos;
			pos=max(0,min(int(inp.length()),int(pos)));
			if (turn=="-") {
				if (pos==0) {
					pos ++;
				}
				pos--;
				if (inp[pos]=='a'||inp[pos]=='e'||inp[pos]=='i'||inp[pos]=='o'||inp[pos]=='u') {
					inp.erase(inp.begin()+pos);
					tries++;
				}
			} else {
				if (turn=="a"||turn=="e"||turn=="i"||turn=="o"||turn=="u") {
					inp.insert(pos, turn);
					tries++;
				}
			}
		}
		cout << "You took " << tries << " turns to complete the word \'" << correct << "\'!" << endl;
		score+=tries;
		cin.ignore();
	}
	
	clear();
	
	cout << "CONGRATULATIONS!" << endl;
	cout << "YOU BEAT THE GAME" << endl;
	if (score==mins) {
		cout << "You took only " << score << " turns to beat this game!" << endl;
		cout << "You beat this game perfectly!" << endl;
		cout << "Good job!" << endl;
	} else {
		cout << "You took a total of " << score << " turns to beat this game!" << endl;
		cout << "The minimum possible was " << mins << "!" << endl;
		cout << "imagine being bad" << endl;
	}
}
