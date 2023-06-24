func validUtf8(data []int) bool {
	n := len(data)
	i := 0
	for i < n {
		// 4 bytes
		if data[i]&0xf8 == 0xf0 {
			if i+4 > n || data[i+1]&0xc0 != 0x80 || data[i+2]&0xc0 != 0x80 || data[i+3]&0xc0 != 0x80 {
				return false
			}
			i += 4
		} else if data[i]&0xf0 == 0xe0 {
			if i+3 > n || data[i+1]&0xc0 != 0x80 || data[i+2]&0xc0 != 0x80 {
				return false
			}
			i += 3
		} else if data[i]&0xe0 == 0xc0 {
			if i+2 > n || data[i+1]&0xc0 != 0x80 {
				return false
			}
			i += 2
		} else if data[i]&0x80 == 0 {
			i++
		} else {
			return false
		}
	}
	return true
}
