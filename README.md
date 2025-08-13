# Morpheme Analyzer

A comprehensive GUI-based tool for analyzing the morphological structure of English words. This application breaks down words into their constituent morphemes (prefixes, roots, and suffixes) and provides detailed linguistic information about each component.

## Features

### Core Functionality
- **Morpheme Analysis**: Automatically identifies and analyzes prefixes, root words, and suffixes
- **Linguistic Classification**: Categorizes morphemes as bound/free and derivational/inflectional
- **Word Validation**: Uses NLTK's WordNet corpus to verify real English words
- **Tree Visualization**: Displays morphological structure in an ASCII tree format
- **Detailed Meanings**: Provides definitions and semantic information for each morpheme

### User Interface
- **Clean GUI**: Built with Tkinter for cross-platform compatibility
- **Real-time Analysis**: Instant morpheme breakdown upon clicking "Analyze"
- **Dual Output**: Separate panels for detailed analysis and tree visualization
- **File Operations**: Save analysis results to text files
- **Help System**: Built-in help documentation

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Required Dependencies
```bash
pip3 install nltk
```

### NLTK Data Setup
The application requires specific NLTK corpora. Run these commands in Python:

```python
import ssl
import nltk

# Disable SSL verification if needed
ssl._create_default_https_context = ssl._create_unverified_context

# Download required data
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

## Usage

### Running the Application
```bash
python3 gui.py
```

### Basic Operation
1. **Enter a Word**: Type any English word in the input field
2. **Analyze**: Click the "Analyze" button to process the word
3. **View Results**: Review the detailed analysis and tree structure
4. **Save Output**: Use File > Save to export results
5. **Clear Fields**: Click "Refresh" to start over

### Example Analysis
For the word "unhappiness":

**Analysis Output:**
```
Results for: unhappiness
Prefix: un | Meaning: not, opposite of | Type: bound morpheme, derivational (negation) morpheme
Root: happy | Meaning: enjoying or showing or marked by joy or pleasure | Type: free root morpheme
Suffix: ness | Meaning: state or quality | Type: bound morpheme, derivational (forms nouns from adjectives) morpheme
```

**Tree Visualization:**
```
Morpheme Tree:
    unhappiness
    /    |    \
  un    happy   ness
```

## Technical Details

### Morpheme Database
The application includes comprehensive databases of:

#### Prefixes (23 types)
- **Negation**: un-, dis-, in-, im-
- **Temporal**: pre-, fore-, re-
- **Spatial**: sub-, super-, trans-, inter-, circum-
- **Quantitative**: bi-, semi-
- **Others**: anti-, auto-, de-, ex-, mid-, over-, under-, mis-

#### Suffixes (18 types)
- **Inflectional**: -ing, -ed, -est
- **Derivational**: -ness, -er, -ly, -tion, -ity, -ment, -able, -al, -ence, -ful, -ic, -ish, -let, -ous, -ship, -y

### Algorithm
1. **Input Validation**: Checks for alphabetic characters only
2. **Prefix Detection**: Searches for longest matching prefix first
3. **Root Validation**: Verifies remaining word is valid using WordNet
4. **Suffix Detection**: Identifies suffixes from the validated root
5. **Lemmatization**: Uses NLTK's WordNetLemmatizer for root forms
6. **Classification**: Categorizes each morpheme by type and function

### File Structure
```
project/
├── gui.py                 # Main application file
├── README.md             # This documentation
├── MaorphoMatrix.docx    # Project documentation
└── Report-(Word Sense Disambiguation).pdf
```

## Menu Options

### File Menu
- **Save**: Export current analysis to a text file
- **Exit**: Close the application

### Help Menu
- **Help**: Display usage instructions

## Error Handling

### Common Issues
1. **NLTK Data Missing**: Automatically prompts for required downloads
2. **Invalid Input**: Rejects non-alphabetic characters
3. **Network Issues**: Handles SSL certificate problems during NLTK downloads
4. **File Save Errors**: Provides detailed error messages

### Troubleshooting
- **SSL Certificate Errors**: Use the SSL workaround in installation
- **Missing WordNet**: Ensure NLTK data is properly downloaded
- **GUI Not Appearing**: Check Python/Tkinter installation

## Educational Applications

### Linguistics Students
- Learn morphological analysis techniques
- Understand bound vs. free morphemes
- Study derivational vs. inflectional morphology

### Language Teachers
- Demonstrate word formation processes
- Explain etymology and word origins
- Teach vocabulary building strategies

### Researchers
- Analyze morphological patterns
- Study word formation productivity
- Generate morphological data for corpus studies

## Limitations

1. **English Only**: Currently supports English words exclusively
2. **Single Morpheme**: Analyzes one prefix and one suffix maximum
3. **Dictionary Dependent**: Relies on WordNet for word validation
4. **Static Database**: Morpheme lists are predefined, not learned

## Future Enhancements

- Multi-language support
- Machine learning-based morpheme detection
- Batch processing capabilities
- Export to various formats (JSON, CSV, XML)
- Integration with larger linguistic databases
- Phonological analysis features

## Technical Requirements

- **Operating System**: Windows, macOS, Linux
- **Python Version**: 3.6+
- **Memory**: 100MB RAM minimum
- **Storage**: 50MB for NLTK data
- **Display**: 800x600 minimum resolution

## License

This project is developed for educational purposes as part of computational linguistics coursework.

## Contributing

Contributions are welcome! Areas for improvement:
- Additional morpheme patterns
- Better error handling
- Performance optimizations
- UI/UX enhancements

## Support

For issues or questions:
1. Check the built-in Help menu
2. Verify NLTK installation and data
3. Ensure Python dependencies are met
4. Review error messages for specific guidance

---

**Note**: This application is designed for educational and research purposes in computational linguistics and morphological analysis.
