func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	var pre *ListNode = nil
	root := &ListNode{0, head}
	slow, fast := root, root
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow, pre, slow.Next = slow.Next, slow, pre
	}
	if fast != nil {
		slow, pre, slow.Next = slow.Next, slow, pre
	} else {
		slow = slow.Next
	}

	for slow != nil {
		if slow.Val != pre.Val {
			return false
		}
		slow, pre = slow.Next, pre.Next
	}
	return true
}
