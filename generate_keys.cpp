#include <bits/stdc++.h>
using namespace std;

void recur(int index, vector<string>&ans,string temp){
    if(index==56){
        ans.push_back(temp);
        return;
    }
    if(temp[index]=='*'){
        temp[index]='0';
        recur(index+1,ans,temp);
        temp[index]='1';
        recur(index+1,ans,temp);
    }else{
        recur(index+1,ans,temp);
    }
}

int main() {
	string input = "010001100110************100010011010100000101011"; // 56 length with *
	vector <int> permut = {24 ,27 ,21 ,6 ,11 ,15 ,13 ,10 ,25 ,16 ,3 ,20,
	 5 ,1 ,22 ,14 ,8 ,18 ,26 ,17 ,9 ,2 ,23 ,12 ,51 ,34 ,41,
	 47 ,29 ,37 ,40 ,50 ,33 ,55 ,43 ,30 ,54 ,31 ,49 ,38 ,44,
	 35 ,56 ,52 ,32 ,46 ,39 ,42};
	 
	 string temp;
	 for(int i=0;i<56;i++) temp.push_back('*');
	 
	 for(int i =0;i<48;i++){
	     temp[permut[i]-1] = input[i];
	 }
	 cout << temp << endl;
	 string key = temp;
	 vector<string> ans;
	 recur(0,ans,key);
	 cout << ans.size() << endl;
	 cout << ans[0] << endl;
	 
// 	 FILE *fo;
// 	 fo = fopen("all_keys.txt","w+");
// 	 for(int i=0;i<pow(2,20);i++){
// 	     fprintf(fo, ans[i]);
// 	 }
// 	 fo.close();
    ofstream myfile;
    myfile.open("all_keys.txt");
    for(int i=0;i<ans.size();i++){
        myfile << ans[i] << "\n";
    }
    myfile.close();
	return 0;
}
