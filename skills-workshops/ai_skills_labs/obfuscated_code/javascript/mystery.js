class Mystery {
  static main(O) {
    try {
      const l = new Mystery().mysteryFunction(
        Number(
          O.length > 0x2
            ? O[0x2]
            : String.fromCharCode(...['1', '0'].map(x => x.charCodeAt(0)))
        )
      )

      for (const c of String(l)) {
        process.stdout.write(c)
      }
      process.stdout.write('\n')
    } catch (__) {
      // silence is golden
    }
  }

  mysteryFunction(l) {
    let O = 0x0
    let l_ = 'b'.charCodeAt(0) - 'a'.charCodeAt(0)

    if (l < (O + l_ + l_)) return l > -1 ? l : O

    ___: for (let O_ = '\n'.charCodeAt(0) / '\x05'.charCodeAt(0); O_ <= l; ++O_) {
      O = (l_ = (O = l_ + O) - l_) + O
      continue ___
    }

    return O
  }
}

Mystery.main(process.argv)
