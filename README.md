# Bigram Probability For The Tragedy of Julius Caesar by William Shakespeare 1599 Corpus
### Running the Bigram Probability Model

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can check this by running:
   ```bash
   python --version
   ```

2. **Install Required Libraries**: Ensure that the required libraries are installed. Open your terminal or command prompt and run:
   ```bash
   pip install pandas
   ```

3. **Prepare Your Files**:
   - **`corpus.txt`**: Download the corpus.text file:
     ```
     The Tragedy of Julius Caesar by William Shakespeare 1599
     ```
   - **`test.txt`**: Create a file named `test.txt` and add your test sentences. For example:
     ```
     Mark Antony, here take you Caesar's body: you shall not come to them, poet.
     No, sir, there are no comets seen; the heavens speed thee in thine enterprise.
     ```

4. **Run Your Script**: Execute the `main.py` script by specifying an option for how the probabilities should be calculated (0 for raw counts, 1 for Laplace smoothing). Open your terminal or command prompt and navigate to the directory where your `main.py` script is located. Run one of the following commands:
   ```bash
   python main.py 0  # For raw counts
   ```
   or
   ```bash
   python main.py 1  # For Laplace smoothing
   ```

5. **Check the Output**: After running the script, check for the generated output file named `output_<option>.txt` (e.g., `output_0.txt` or `output_1.txt`). Open this file to see:
   - The original sentences.
   - The bigram counts.
   - The bigram probabilities.
   - The total probability of each sentence.

### Example Output

Here is what you might expect in `output_0.txt` or `output_1.txt`:

```
Mark Antony, here take you Caesar's body: you shall not come to them, poet.

Bigram Counts: 
             <s>    Mark    Antony,    here    take    you    Caesar's    body:    you    shall    not    come    to    them,    poet.   </s>
<s>         ...
Mark      ...
Antony,   ...
...

Bigram Probabilities: 
             <s>    Mark    Antony,    here    take    you    Caesar's    body:    you    shall    not    come    to    them,    poet.   </s>
<s>         ...
Mark      ...
Antony,   ...
...

Probability of the Sentence: X.XXXXXX
########################################################################################################################################################################################################
```
