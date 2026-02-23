# Feature Extensions

## Core Features

### Range Calculations
Generate Fibonacci numbers within a specified range of indices.

**Description**: Instead of calculating just the nth Fibonacci number, allow users to generate all Fibonacci numbers from index A to index B (inclusive). This is useful for analysing sequence patterns or generating datasets.

**Example Usage**:
```
python fibonacci --range 5 10
# Output: F(5)=5, F(6)=8, F(7)=13, F(8)=21, F(9)=34, F(10)=55
```

**Implementation Considerations**:
- Validate that A ≤ B
- Handle negative indices appropriately
- Consider memory usage for large ranges
- Support different output formats (list, CSV, etc.)

### Mathematical Properties

#### Is Fibonacci Check
Determine whether a given number exists in the Fibonacci sequence.

**Description**: Given an arbitrary positive integer, determine if it's a Fibonacci number. This involves checking if one of `5*n²+4` or `5*n²-4` is a perfect square (mathematical property of Fibonacci numbers).

**Example Usage**:
```
python fibonacci --is-fib 13
# Output: true (13 is F(7))

python fibonacci --is-fib 14
# Output: false
```

#### Closest Fibonacci
Find the Fibonacci number closest to a given value.

**Description**: For any positive integer, find the Fibonacci number with the smallest absolute difference. If there's a tie, return both numbers or use a specified tie-breaking rule.

**Example Usage**:
```
python fibonacci --closest 20
# Output: 21 (F(8), difference = 1)

python fibonacci --closest 15
# Output: 13 (F(7), difference = 2) or 21 (F(8), difference = 6)
```

## Advanced Features

### Multiple Sequence Types
Support for different mathematical sequences beyond Fibonacci.

#### Lucas Numbers
**Description**: Implement the Lucas sequence, which follows the same recurrence relation as Fibonacci (L(n) = L(n-1) + L(n-2)) but starts with L(0) = 2, L(1) = 1.

**Example Usage**:
```
python fibonacci --sequence lucas 7
# Output: 29 (L(7) = 29)
```

#### Tribonacci
**Description**: Extend to Tribonacci numbers where each term is the sum of the three preceding terms: T(n) = T(n-1) + T(n-2) + T(n-3), starting with T(0) = 0, T(1) = 0, T(2) = 1.

**Example Usage**:
```
python fibonacci --sequence tribonacci 8
# Output: 24 (T(8) = 24)
```

#### Custom Sequences
**Description**: Allow users to define their own sequences by specifying:
- Initial values (seeds)
- Number of previous terms to sum
- Custom recurrence relations

**Example Usage**:
```
python fibonacci --custom --seeds 1,1,2 --terms 4 10
# Creates a 4-term recurrence starting with [1,1,2]: each term = sum of previous 4 terms
```

## Implementation Tips

### General Considerations
- **Error Handling**: Validate all inputs and provide meaningful error messages
- **Performance**: Consider memoization for repeated calculations
- **Testing**: Write comprehensive tests for edge cases and mathematical properties
- **Documentation**: Include examples and mathematical explanations

### Mathematical Validation
- Verify sequence properties using known mathematical formulas
- Test edge cases (negative indices, zero, large numbers)
- Compare results with established mathematical references

### Code Design
- Use polymorphism or strategy pattern for different sequence types
- Separate calculation logic from input/output handling
- Consider using arbitrary precision arithmetic for very large numbers

## Bonus Challenges

1. **Performance Benchmarking**: Compare different algorithms (iterative, recursive, matrix multiplication)
2. **Visualization**: Generate graphs showing sequence growth rates
3. **Web Interface**: Create a simple web UI for the calculator
4. **File I/O**: Support batch processing from input files
5. **Mathematical Analysis**: Calculate ratios between consecutive terms, identify patterns

Each feature can be implemented incrementally, allowing learners to build complexity gradually while maintaining clean, testable code.
<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ai_skills_labs/3_ticket_to_quality_code/PYTHON_FEATURES.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ai_skills_labs/3_ticket_to_quality_code/PYTHON_FEATURES.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ai_skills_labs/3_ticket_to_quality_code/PYTHON_FEATURES.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ai_skills_labs/3_ticket_to_quality_code/PYTHON_FEATURES.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=skills-workshops&prefill_File=ai_skills_labs/3_ticket_to_quality_code/PYTHON_FEATURES.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
