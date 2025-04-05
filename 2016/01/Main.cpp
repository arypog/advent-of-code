#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int part1(vector<string> instructions) {
  int x = 0, y = 0, lk = 0;
  int dx[4] = {0, 1, 0, -1};
  int dy[4] = {1, 0, -1, 0}; 
  for (string ins : instructions) {
    char dir = ins[0];
    int amount = stoi(ins.substr(1));
    if(dir == 'R') lk = (lk + 1) % 4;
    else lk = (lk + 3) % 4;
    x += dx[lk] * amount; 
    y += dy[lk] * amount; 
  }

  int manhattan_distance = abs(0 - x) + abs(0 - y); 
  return manhattan_distance;
}

int part2(vector<string> instructions) {
  set<pair<int,int>> visited;
  for (string ins : instructions) {
    int x = 0, y = 0, lk = 0;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0}; 
    for (string ins : instructions) {
      char dir = ins[0];
      int amount = stoi(ins.substr(1));
      if(dir == 'R') lk = (lk + 1) % 4;
      else lk = (lk + 3) % 4;
      for (int i = 0; i < amount; i++) {
        x += dx[lk]; 
        y += dy[lk]; 
        pair<int,int> key = {x, y};
        if (visited.count(key) != 0) {
          int manhattan_distance = abs(0 - x) + abs(0 - y); 
          return manhattan_distance;
        }
        visited.insert(key);
      }
    }
  }

  return 0;
}

using namespace std;
int main() {
  string line;
  //ifstream f ("2016/01/test");
  ifstream f ("2016/01/pub");

  getline(f, line);
  istringstream line_2(line);    
  vector<string> instructions;

  for (string direction; getline(line_2, direction, ','); ) {
    if (direction.front() == ' ')
      instructions.push_back(direction.substr(1));
    else
      instructions.push_back(direction);
  }
  
  cout << part1(instructions) << endl;
  cout << part2(instructions) << endl;

  f.close();

  return 0;
}
