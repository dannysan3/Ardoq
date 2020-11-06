class Task1 {

  public static void main(String[] args){

    int[] array = {1,20,2,6,5,3,2,25,33};
    printLargest(array);
  }



  static void printLargest(int[] n){

    selectionSort(n);
    int len = n.length;
    System.out.println(n[len-1]*n[len-2]*n[len-3]);
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
