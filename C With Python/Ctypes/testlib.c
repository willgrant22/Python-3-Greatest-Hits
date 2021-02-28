//# -*- coding: utf-8 -*-
//# =============================================================================
//# Author :  Will Grant
//# =============================================================================

#include <stdio.h>

void myprint(void);

void myprint()
{

   /* an array with 5 rows and 2 columns*/
   int a[5][2] = { {0,0}, {1,2}, {2,4}, {3,6},{4,8}};
   int i, j;
 
   /* output each array element's value */
   for ( i = 0; i < 5; i++ ) {

      for ( j = 0; j < 2; j++ ) {
         printf("a[%d][%d] = %d\n", i,j, a[i][j] );
      }
   }
   
   
}
//gcc -shared -Wl,-install_name,testlib.so -o testlib.so -fPIC testlib.c