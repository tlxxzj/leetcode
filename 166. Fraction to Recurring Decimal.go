func fractionToDecimal(numerator int, denominator int) string {
	var num, deno int64 = int64(numerator), int64(denominator)
	if num%deno == 0 {
		return strconv.FormatInt(num/deno, 10)
	}

	var res string
	if (num < 0) != (deno < 0) {
		res += "-"
	}

	if num < 0 {
		num = -num
	}

	if deno < 0 {
		deno = -deno
	}

	res += strconv.FormatInt(num/deno, 10)
	res += "."

	num = num % deno
	nums := make(map[int64]int)
	for num != 0 {
		if _, ok := nums[num]; ok {
			res = res[:nums[num]] + "(" + res[nums[num]:] + ")"
			break
		}

		nums[num] = len(res)
		num *= 10
		res += strconv.FormatInt(num/deno, 10)
		num %= deno
	}
	return res
}