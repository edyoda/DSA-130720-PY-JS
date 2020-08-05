function Hanoi(n , source, destination, via)
{
  if (n==1){
      console.log("Move disk 1 from source",source,"to destination",destination)
      return
  }

  Hanoi(n-1, source, via, destination);
  console.log("Move disk",n,"from source",source,"to destination",destination);
  Hanoi(n-1, via, destination, source);

}

n = 2
Hanoi(n,'a','b','c')