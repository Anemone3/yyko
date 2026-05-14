public class DigPow {

	public static long digPow(int n, int p) {

		int[] digits = String.valueOf(n)
				.chars()
				.map(c -> c - '0')
				.toArray();

		long sum = 0;

		for (int i = 0; i < digits.length; i++) {
			sum += sumDigit(digits[i], p);
			p++;
		}

		if (sum % n == 0) {
			return sum / n;
		}

		return -1;
	}

	static long sumDigit(int d, int p) {
		return (long) Math.pow(d, p);
	}

}
