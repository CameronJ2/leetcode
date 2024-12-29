function findWords(words: string[]): string[] {
  const sets: Set<string>[] = [
    new Set(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]),
    new Set(["a", "s", "d", "f", "g", "h", "j", "k", "l"]),
    new Set(["z", "x", "c", "v", "b", "n", "m", ""]),
  ]

  const returnWords: string[] = []

  let wordSet = new Set()

  let lowerWords = words.map((value) => {
    return value.toLowerCase()
  })

  lowerWords.forEach((word, wordIdx) => {
    wordSet = new Set()
    const letters = word.split("")

    letters.forEach((letter, _letterIdx) => {
      if (sets[0].has(letter)) {
        wordSet.add(0)
      } else if (sets[1].has(letter)) {
        wordSet.add(1)
      } else if (sets[2].has(letter)) {
        wordSet.add(2)
      }
    })

    if (wordSet.size === 1) {
      returnWords.push(words[wordIdx])
    }
  })

  return returnWords
}

const words = ["Hello", "Alaska", "Dad", "Peace"]

console.log(findWords(words))
