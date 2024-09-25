function plusOne(digits: number[]): number[] {
  for (let i = digits.length - 1; i >= 0; i--) {
    digits[i] += 1

    if (digits[i] < 10) {
      break // No carry needed, just exit the loop.
    }

    digits[i] = 0 // Carry over, set current digit to 0.

    if (i === 0) {
      digits.unshift(1) // Add 1 at the beginning if all digits carry over.
    }
  }

  return digits
}

const digits: number[] = [8, 9, 9, 9]
console.log(plusOne(digits))
