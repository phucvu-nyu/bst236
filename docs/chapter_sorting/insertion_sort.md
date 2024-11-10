# Insertion sort

<u>Insertion sort</u> is a simple sorting algorithm that works very much like the process of manually sorting a deck of cards.

Specifically, we select a pivot element from the unsorted interval, compare it with the elements in the sorted interval to its left, and insert the element into the correct position.

The figure below shows the process of inserting an element into an array. Assuming the pivot element is `base`, we need to move all elements between the target index and `base` one position to the right, then assign `base` to the target index.

![Single insertion operation](insertion_sort.assets/insertion_operation.png)


## Algorithm process

The overall process of insertion sort is shown in the figure below.

1. Initially, the first element of the array is sorted.
2. The second element of the array is taken as `base`, and after inserting it into the correct position, **the first two elements of the array are sorted**.
3. The third element is taken as `base`, and after inserting it into the correct position, **the first three elements of the array are sorted**.
4. And so on, in the last round, the last element is taken as `base`, and after inserting it into the correct position, **all elements are sorted**.

![Insertion sort process](insertion_sort.assets/insertion_sort_overview.png)

Example code is as follows:

=== "Python"

	```python
	def InsertionSort(A):
		for j in range(1, len(A)):
			key = A[j]
			i = j - 1
			while (i >= 0) and (A[i] > key):
				A[i+1] = A[i]
				i = i - 1
			A[i+1] = key
	```
=== "R"

	```r
	insertion_sort <- function(A) {
		for (j in 2:length(A)) {
			key <- A[j]
			i <- j - 1
			while (i >= 1 && A[i] > key) {
				A[i + 1] <- A[i]
				i <- i - 1
			}
			A[i + 1] <- key
		}
		return(A)
	}
	```

??? pythontutor "Visualize Code"

	https://pythontutor.com/render.html#code=%23%20from%3A%20http%3A//www.ece.uci.edu/~chou/py02/python.html%0Adef%20InsertionSort%28A%29%3A%0A%20%20%20%20for%20j%20in%20range%281,%20len%28A%29%29%3A%0A%20%20%20%20%20%20%20%20key%20%3D%20A%5Bj%5D%0A%20%20%20%20%20%20%20%20i%20%3D%20j%20-%201%0A%20%20%20%20%20%20%20%20while%20%28i%20%3E%3D%200%29%20and%20%28A%5Bi%5D%20%3E%20key%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20A%5Bi%2B1%5D%20%3D%20A%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20i%20-%201%0A%20%20%20%20%20%20%20%20A%5Bi%2B1%5D%20%3D%20key%0A%0Ainput%20%3D%20%5B8,%203,%209,%2015,%2029,%207,%2010%5D%0AInsertionSort%28input%29%0Aprint%28input%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

## Algorithm characteristics

- **Time complexity is $O(n^2)$, adaptive sorting**: In the worst case, each insertion operation requires $n - 1$, $n-2$, ..., $2$, $1$ loops, summing up to $(n - 1) n / 2$, thus the time complexity is $O(n^2)$. In the case of ordered data, the insertion operation will terminate early. When the input array is completely ordered, insertion sort achieves the best time complexity of $O(n)$.
- **Space complexity is $O(1)$, in-place sorting**: Pointers $i$ and $j$ use a constant amount of extra space.
- **Stable sorting**: During the insertion operation, we insert elements to the right of equal elements, not changing their order.

## Advantages of insertion sort

The time complexity of insertion sort is $O(n^2)$, while the time complexity of quicksort, which we will study next, is $O(n \log n)$. Although insertion sort has a higher time complexity, **it is usually faster in cases of small data volumes**.

This conclusion is similar to that for linear and binary search. Algorithms like quicksort that have a time complexity of $O(n \log n)$ and are based on the divide-and-conquer strategy often involve more unit operations. In cases of small data volumes, the numerical values of $n^2$ and $n \log n$ are close, and complexity does not dominate, with the number of unit operations per round playing a decisive role.

In fact, many programming languages (such as Java) use insertion sort in their built-in sorting functions. The general approach is: for long arrays, use sorting algorithms based on divide-and-conquer strategies, such as quicksort; for short arrays, use insertion sort directly.

Although bubble sort, selection sort, and insertion sort all have a time complexity of $O(n^2)$, in practice, **insertion sort is used significantly more frequently than bubble sort and selection sort**, mainly for the following reasons.

- Bubble sort is based on element swapping, which requires the use of a temporary variable, involving 3 unit operations; insertion sort is based on element assignment, requiring only 1 unit operation. Therefore, **the computational overhead of bubble sort is generally higher than that of insertion sort**.
- The time complexity of selection sort is always $O(n^2)$. **Given a set of partially ordered data, insertion sort is usually more efficient than selection sort**.
- Selection sort is unstable and cannot be applied to multi-level sorting.

