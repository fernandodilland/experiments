// Simple C++ program to display "Hello World"

#include <iostream>
#include <time.h> // For sleep

using namespace std;

void sleepcp(int milliseconds);

void sleepcp(int milliseconds) // Cross-platform sleep function
{
    clock_t time_end;
    time_end = clock() + milliseconds * CLOCKS_PER_SEC/1000;
    while (clock() < time_end)
    {
    }
}

int main()
{
    cout << "Hello World" << endl;
    sleepcp(3000); // 3 seconds sleep
}