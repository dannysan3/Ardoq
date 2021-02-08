class FindLargest {

  public static void main(String[] args){

    int[] array = {1,10,2,6,5,3};
    printLargest(array);
  }



  static void printLargest(int[] n){

    selectionSort(n);
    int size = n.length;
   

    int test = n[0]*n[1]*n[size-1];

    int test2 = n[size-1]*n[size-2]*n[size-3];

    if (test>test2){
      System.out.println(test);
    }
    else {
      System.out.println(test2);
    }

  }


  public static void selectionSort(int[] a) {
    int n = a.length;

    for (int i=0; i<n;i++) {
      int k = i;
      for (int j=k+1; j<n; j++) {
        if (a[j]< a[k]){
          k = j;
        }
      }
      if (k!=i) {
        int temp = a[k];
        a[k] = a[i];
        a[i] = temp;
      }
    }


  }
}
