The following program is a ball brick game. That can be played to a customized board size. We can also create the customized brick pattern with different values of powers given to bricks. In each hit the value or power of the brick is decremented by 1.And when finally the brick value goes to '0' it disappers
Input and outputs are as follows:
Sample Input and Output:
Enter size of the NxN matrix : 7
Enter the brick's position and the brick type : 2 2 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 2 3 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 2 4 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 2 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 3 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 4 1
Do you want to continue(Y or N)?N
Enter ball Count : 3
Sample Output:
W W W W W W W
W           W
W   1 1 1   W
W   1 1 1   W
W           W
W           W
W G G o G G W
Ball count is 3.

sample 2:
Enter size of the NxN matrix : 7
Enter the brick's position and the brick type : 2 2 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 2 3 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 2 4 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 2 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 3 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 4 1
Do you want to continue(Y or N)?N
Enter ball Count : 3
Sample Output:
W W W W W W W
W           W
W   1 1 1   W
W   1 1 1   W
W           W  
W           W
W G G o G G W
Ball count is 3.
Next Input:
Enter the direction in which the ball need to traverse : ST
Next Output:
W W W W W W W
W           W
W   1 1 1   W
W   1   1   W
W           W
W           W 
W G G o G G W
Ball count is 3.
Next Input:
Enter the direction in which the ball need to traverse : LD

Next Output:
W W W W W W W
W           W
W   1 1 1   W
W       1   W
W           W
W           W
W G o G G G W
Ball count is 2.


sample 3:
Sample Input:
Enter size of the NxN matrix : 7
Enter the brick's position and the brick type : 2 3 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 2 4 3
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 2 1
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 3 2
Do you want to continue(Y or N)?Y
Enter the brick's position and the brick type : 3 4 1
Do you want to continue(Y or N)?N
Enter ball Count : 3
Sample Output:
W W W W W W W
W           W
W     1 3   W
W   1 2 1   W
W           W
W           W
W G G o G G W
Ball count is 3
Next Input:
Enter the direction in which the ball need to traverse : ST
Next Output:

W W W W W W W
W           W
W     1 3   W
W   1 1 1   W
W           W
W           W
W G G o G G W
Ball count is 3.