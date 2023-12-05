#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int ms=0,cnt;
string antivwl(string a) {
	string b="";
	for (int i = 0; i < a.length(); i ++) {
		if (a[i]!='a'&&a[i]!='e'&&a[i]!='i'&&a[i]!='o'&&a[i]!='u') {
			b.push_back(a[i]);
		}
	}
	ms+=a.size()-b.size();
	return b;
}
vector<pair<string,string>> d;
string x;
int main() {
	cin >> cnt;
	for (int i = 0; i < cnt; i ++) {
		cin >> x;
		d.push_back({antivwl(x),x});
	}
	ofstream key("vwllss.txt");
	key << cnt << " " << ms << endl;
	for (int i = 0; i < cnt; i ++) {
		key << d[i].first << " " << d[i].second << endl;
	}
	key.close();
}