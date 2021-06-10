// Exercise obtained from the Internet, solved for practice.
// Programmed by: Fernando Dilland Mireles Cisneros

// Arrays: move zeros to the left
// Given an integer array, move all elements that are 0 to the left while
// maintaining the order of other elements in the array. The array has to be
// modified in-place. Try it yourself before reviewing the solution and
// explanation.

void move_zeros_to_left(int A[], int n) {

    if (n < 1) return;
    int write_index = n - 1;
    int read_index = n - 1;

    while(read_index >= 0) {
        if(A[read_index] != 0) {
        A[write_index] = A[read_index];
        write_index--;
        }

        read_index--;
    }

    while(write_index >= 0) {
        A[write_index] = 0;
        write_index--;
    }
    }
    int main() {
    int v[] = {1, 10, 20, 0, 59, 63, 0, 88, 0};
    int n = sizeof(v) / sizeof(v[0]);

    cout << "Original Array" <<endl;

    for(int x=0 ; x<n; x++) {
        cout << v[x];
        cout << ", ";
    }

    move_zeros_to_left(v, n);

    cout << endl<< "After Moving Zeroes to Left"<< endl;
    for(int i=0 ; i<n; i++) {
        cout << v[i];
        cout << ", ";
    }
}