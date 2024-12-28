function canPlaceFlowers(flowerbed: number[], n: number): boolean {
  for (let i = 0; i < flowerbed.length; i++) {
    if (n <= 0) {
      return true
    }

    if (n === 0) {
      return true
    }

    if (flowerbed.length === 1) {
      if (flowerbed[0] === 0 && n === 1) {
        return true
      }
      return false
    }

    if (i === 0) {
      if (flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
        n = n - 1
        flowerbed[i] = 1
      }
      continue
    }

    if (i === flowerbed.length - 1) {
      if (flowerbed[i] === 0 && flowerbed[i - 1] === 0) {
        n = n - 1
        flowerbed[i] = 1
      }
      continue
    }

    if (flowerbed[i] === 0) {
      if (flowerbed[i - 1] === 1 || flowerbed[i + 1] === 1) {
        continue
      }
      n = n - 1
      flowerbed[i] = 1
    }
  }
  return false
}

const flowerbed = [0],
  n = 2

console.log(canPlaceFlowers(flowerbed, n))
