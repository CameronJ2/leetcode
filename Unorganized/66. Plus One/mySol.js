function plusOne(digits) {
  for (var i = digits.length - 1; i >= 0; i--) {
    digits[i] += 1
    if (digits[i] < 10) {
      break
    }
    if (i === 0) {
      digits.unshift(1)
      digits[i + 1] = 0
      break
    }
    digits[i - 1] += 1
    digits[i] = 0
  }
  return digits
}
var digits = [8, 9, 9, 9]
console.log(plusOne(digits))
