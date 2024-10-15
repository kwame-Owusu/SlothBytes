#include <iostream>
#include <vector>


void ping_pong(std::vector<std::string>& arr, bool win){
  std::string pong = "Pong!";
  for (int  i = 1; i < arr.size(); i += 2)
  {
    arr.insert(arr.begin() + i , pong);
  }
  // Check the last element before appending
    if (win) {
        // Append "Pong!" if last element is not already "Pong!"
        if (arr.empty() || arr.back() != pong) {
            arr.push_back(pong);
        }
    } else {
        // Append "Ping!" if last element is not already "Ping!"
        if (arr.empty() || arr.back() != "Ping!") {
            arr.push_back("Ping!");
        }
    }
  for (const std::string& c : arr){
    std::cout<< c << " ";
  }
  std::cout << std::endl;
  

}

int main(){
  std::vector<std::string> ping_1 = {"Ping!"};
  std::vector<std::string> ping_2 = {"Ping!", "Ping!"};
  std::vector<std::string> ping_3 = {"Ping!", "Ping!", "Ping!"};
  ping_pong(ping_1, 1);
  ping_pong(ping_2, 0);
  ping_pong(ping_3, 1);
 
  return 0;
}

