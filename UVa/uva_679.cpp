#include "iostream"
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	while (t--)
	{
		int D, I;
		scanf("%d %d", &D, &I);
		int idx = 1;
		int remainder = I;
		for (int i = 0; i < D - 1; i++) {
			if (remainder % 2 == 1) {
				idx = 2 * idx;
				remainder = (remainder + 1) / 2;
			}
			else {
				idx = 2 * idx + 1;
				remainder /= 2;
			}
		}
		printf("%d\n", idx);
	}

	return 0;
}