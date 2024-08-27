func numberToWords(num int) string {

	num0_19 := []string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
		"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}

	num20_90 := []string{"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}

	hundred := "Hundred"
	thousand := "Thousand"
	million := "Million"
	billion := "Billion"

	num2str := func(num int) string {
		res := []string{}
		if num >= 100 {
			res = append(res, num0_19[num/100])
			res = append(res, hundred)
			num %= 100
		}
		if num >= 20 {
			res = append(res, num20_90[num/10])
			num %= 10
		}
		if num > 0 {
			res = append(res, num0_19[num])
		}
		return strings.Join(res, " ")
	}

	if num <= 19 {
		return num0_19[num]
	}

	res := []string{}
	if num >= 1000000000 {
		res = append(res, num2str(num/1000000000))
		res = append(res, billion)
		num %= 1000000000
	}

	if num >= 1000000 {
		res = append(res, num2str(num/1000000))
		res = append(res, million)
		num %= 1000000
	}

	if num >= 1000 {
		res = append(res, num2str(num/1000))
		res = append(res, thousand)
		num %= 1000
	}

	if num > 0 {
		res = append(res, num2str(num))
	}

	return strings.Join(res, " ")
}
