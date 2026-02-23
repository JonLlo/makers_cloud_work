public class Mystery {
    public static void main(String[] O) {
        try {
            long l = new Mystery().mysteryFunction(Integer.valueOf(O.length > 0x0 ? O[0x0] : new String(
                new char[]{'1','0'})));
            for(char c : String.valueOf(l).toCharArray()) {
                System.out.write(c);
            }
            System.out.write('\n');
        } catch (Exception __) {
            // Silence is golden
        }
    }

    private long mysteryFunction(int l) {
        long O = 0x0L, l_ = (long)(int)('b' - 'a');
        if (l < (O + l_ + l_)) return l > -1 ? l: O;
        ___: for (int O_ = (int)('\n' / '\u0005'); O_ <= l; ++O_){
            O = (l_ = (O = l_ + O) - l_) + O;
            continue ___;
        }
        return O;
    }
}
