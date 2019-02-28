#include<bits/stdc++.h>
using namespace std;

unsigned short moves[] = {
1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
};

unsigned int permutation2[] = {
  14, 17, 11, 24,  1, 5,
  3, 28 ,15,  6, 21, 10,
  23, 19, 12,  4, 26, 8,
  16,  7, 27, 20, 13, 2,
  41, 52, 31, 37, 47, 55,
  30, 40, 51, 45, 33, 48,
  44, 49, 39, 56, 34, 53,
  46, 42, 50, 36, 29, 32
};

unsigned char KeyScheduleArr[16][48];

int main()
{
    ofstream ofile;
    ofile.open("key_permutation_file.txt");
    unsigned int i, j, k, t1, t2,z;
    static unsigned char cNd[56]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56};
    int sw1=0,r=6;
  
    for ( i=0; i<r; i++) {
      for (j =0; j <moves[i]; j++) {
        t1 = cNd[0];
        t2 = cNd[28];
        for ( k=0; k<27; k++) {
          cNd[k] = cNd[k+1];
          cNd[k+28] = cNd[k+29];
        }
        cNd[27] = t1;
        cNd[55] = t2;
      }
      j = sw1 ? r-1-i :i ;
      for (k=0; k< 48 ; k++)  KeyScheduleArr[j][k] = cNd[permutation2[k] -1];
    }
    
    for(z=0;z<48;z++) ofile<<int(KeyScheduleArr[5][z])<<' ';
    return 0;
}