#include <bits/stdc++.h>
using namespace std;

int main()
{
  long long int i = 0;
  long long int k;
  char arr1[64];
  long long int arr2[64];
  long long int t1,t2;
  char  part1[17],part2[17];
  int  s[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0};


  FILE *fileInput,*fileOutput;
  fileInput = fopen("random.txt","r+");
  fileOutput = fopen("input_random.txt","w+");
  
  while(i < 100000)
  {
    fscanf(fileInput,"%s",arr1);
    for(int j = 0 ; j < 64 ; j++)
    {
      t1 = arr1[j]-48;
      t2 = s[j];
      arr2[j] =(t1^t2);

    }
    int l;
    for(l = 0 ; l < 16 ; l++)
    {
      int var1,var2;
      var1 = (arr1[l*4]-48)*8+(arr1[l*4+1]-48)*4+(arr1[l*4+2]-48)*2+(arr1[l*4+3]-48);
      var2 = arr2[l*4]*8+arr2[l*4+1]*4+arr2[l*4+2]*2+arr2[l*4+3];
      var1 += 102;
      var2 += 102;
      part1[l] = var1;
      part2[l] = var2;
    }
    part1[l] = '\0';
    part2[l] = '\0';
    i++;
    fprintf(fileOutput, "%s\n",part1);
    fprintf(fileOutput, "%s\n",part2);
  }
}