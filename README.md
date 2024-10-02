# Quantization Program

This Python program performs **quantization** on input samples, allowing users to input a range of values and a quantization level. The program then maps the sample values to quantization zones and provides the corresponding binary representation of the zone.

## Features

- Input a range \((a, b)\) for sample values.
- Define the quantization level \(q\), which divides the range into equal steps.
- Enter multiple sample values, and the program will calculate which quantization zone the sample falls into and provide the binary representation of the zone.
- Users can continuously input sample values until they choose to stop.

## How the Program Works

1. **Define the Range**: The user enters the lower bound `a` and the upper bound `b` of the range.
2. **Set Quantization Level**: The user sets the quantization level `q`, which determines how many zones the range \((a, b)\) is divided into.
3. **Input Samples**: The user inputs sample values, and the program will:
   - Determine which quantization zone the sample belongs to.
   - Output the corresponding zone index and its binary representation.
4. **Exit**: The user can exit by entering anything other than a number.

## Program Structure

The program uses the following logic:
- It calculates the step size by dividing the range \((b-a)\) by the quantization level `q`.
- Each input sample is checked to see if it falls within the range \((a, b)\).
- If the sample is within the range, the program calculates the zone and the binary code for that zone.
- Users can input as many samples as they want, and the program stops when a non-numeric value is entered.

## How to Use

### Prerequisites

- **Python 3.x** installed.

### Running the Program

1. **Clone the repository** (or download the code):

   ```bash
   git clone https://github.com/yourusername/Quantization-Program.git
   ```

2. **Run the program**:

   ```bash
   python quantization_program.py
   ```

3. **Input Range**:

   The program will prompt you to enter the range for the sample values:
   
   ```
   Please enter the range of these numbers (a,b)
   a: 0
   b: 10
   ```

4. **Input Quantization Level**:

   The program will then ask for the quantization level:
   
   ```
   Now please enter the quantization level: 4
   ```

5. **Input Sample Values**:

   You can input as many sample values as you like, and the program will return the quantization zone and its binary representation:
   
   ```
   Please enter the value of the sample: 2
   It is in the zone: 0, binary: 0
   ```

   To stop inputting sample values, type anything other than a number:
   
   ```
   Please enter the value of the sample: done
   ```

### Example Input and Output

```
Please enter the range of these numbers (a,b)
a: 0
b: 10
Now please enter the quantization level: 4
Now you will set the values of the samples, when you finish please type anything but a number
Please enter the value of the sample: 2
It is in the zone: 0, binary: 0
Please enter the value of the sample: 6
It is in the zone: 2, binary: 10
Please enter the value of the sample: 9
It is in the zone: 3, binary: 11
Please enter the value of the sample: done
```

### Explanation of Results

- **Zone**: The program divides the range into `q` equal zones. Each sample value is placed into the appropriate zone based on its value.
- **Binary Representation**: The index of the zone is represented in binary form.
