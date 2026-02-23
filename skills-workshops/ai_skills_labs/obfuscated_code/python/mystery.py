import sys

class Mystery:
    @staticmethod
    def main(O):
        try:
            l = Mystery().mystery_function(
                int(O[2] if len(O) > 0x2 else ''.join([chr(ord('1')), chr(ord('0'))]))
            )
            for c in str(l):
                sys.stdout.write(c)
            sys.stdout.write('\n')
        except Exception as __:
            # silence is golden
            pass
    
    def mystery_function(self, l):
        O = 0x0
        l_ = ord('b') - ord('a')
        
        if l < (O + l_ + l_):
            return l if l > -1 else O
        
        O_ = ord('\n') // ord('\x05')
        while O_ <= l:
            O = (l_ := (O := l_ + O) - l_) + O
            O_ += 1
        
        return O

if __name__ == "__main__":
    Mystery.main(sys.argv)
