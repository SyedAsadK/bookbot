# bookbot

Bookbot is a command-line application written in Python that analyzes text files, such as novels, to generate a statistical report of word and character usage.
This project was built as part of the "Build a Bookbot in Python" course on Boot.dev.

## Features

    Word Count: Counts the total number of words in a given text file.

    Character Count: Calculates the frequency of each character, including letters, numbers, and symbols.

    Report Generation: Outputs a formatted report displaying the word count and a sorted list of character frequencies.

## How to Use

    Clone the Repository:

```

    git clone https://github.com/SyedAsadK/Bookbot.git
    cd Bookbot

```

    Add Your Text File:
    Place a plain text file (e.g., a .txt file) that you wish to analyze into the repository's directory.

    Run the Program:
    Execute the main.py script from your terminal, passing the filename as an argument.

```

    python3 main.py <your_file.txt>
```

Project Structure

    main.py: The primary script that orchestrates the analysis, taking a text file as input and generating the final report.

    stats.py: Contains the core functions for data analysis, such as counting words and characters.
