#include <iostream>
#include "../include/svd.h"

namespace Optimization {

	Mat3<float> ensure_positive_Z(Mat3<float> u, Mat3<float> v, bool base) {
		bool sign;
		float x;
		if(base) {
			x = u(2, 2);
		}
		else {
			x = v(2, 2);
		}
		sign = (x > 0) - (x < 0);
		if(base) {
			return u * sign;
		}
		else {
			return v * sign;
		}
	}
}
