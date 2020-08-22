# FizzBuzz Co.

This is a module that helps perform the FizzBuzz excercise with minimal effort. In addition, it also gives an ability for one party to test the output of another.

I wanted to learn how publishing of python modules for wider distribution can be performed. Therefore, I chose to do an experiment of that with one of the most famous examples of excercises given in companies, when testing a new programmer. And since Python essentially has a package for everthing - why not make it for FizzBuzz. Hence, FizzBuzz Co. (FizzBuzz + Companies).

## Installation

Run (approximatelly, depending on the current release version and your version of pip/pip3) the following to install:

```python
pip install fizzbuzz-co
```

## Usage

```python
from FizzBuzz import FizzBuzz
```

### Print FizzBuzz values from 5 to 20:

```python
# Input:
fizzbuzz=FizzBuzz()
fizzbuzz.fizzbuzz(amount=15, start=5)
```

```
# Output
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

### Perform a check if a list of information fits the FizzBuzz criteria

```python
# Input (Positive outcome)
fizzbuzz=FizzBuzz()
sequence=[1, 2, "Fizz", 4, "Buzz"]
answer = fizzbuzz.compliance(sequence=sequence, start=1)
print(answer)
```

```
# Output:
The candidate has passed.
```

```python
# Input (Negative outcome)
fizzbuzz=FizzBuzz()
sequence=[1, "Fizz", 4, "Buzz"]
answer=fizzbuzz.compliance(sequence=sequence, start=1)
print(answer)
```

```
# Output:
The candidate has not passed.
```

### Report generation for the candidates performance

```python
# Input
fizzbuzz=FizzBuzz()
sequence=[1, "Banana", "Fizz", 4, "Buzz"]
fizzbuzz.compliance_report(sequence=sequence, start=1)

# Output in a generated file: FizzBuzz_Report_YYYYMMDD_HHMM (year-month-day_hour_minute)
```

Real Answer | Candidate's Answer | Status
:------------: | :------------: | :------------: |
1 | 1 | :heavy_check_mark:
2 | Banana | :x:
Fizz | Fizz | :heavy_check_mark:
4 | 4 | :heavy_check_mark:
Buzz | Buzz | :heavy_check_mark:





