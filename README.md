# Resume-Classification-Dataset

## Dataset Description
The dataset comprises resumes from various sources, including Google Images, Bing Images, and LiveCareer. Each resume entry has two columns: "Category" and "Text". The "Category" column indicates the job title associated with the resume, while the "Text" column contains the textual content extracted from the resumes using optical character recognition (OCR).

## Data Sources
- Google Images: Resumes were scraped from Google Images through automated scraping techniques. A total of 3015 records were obtained.
- Bing Images: A total of 2722 records were obtained from scrapping Bing Images.
- LiveCareer: A total of 7652 records were obtained from scrapping the website LiveCareer.

## Total Number of Records
The dataset contains 13389 records, encompassing job titles and corresponding resume texts from all three sources.

## Data Collection Process
- The collection process involved several stages, starting with the scraping of resume images from each source. This process was executed using separate scripts tailored for Google Images, Bing Images, and LiveCareer. The scraping phase required approximately 5 hours for Bing, about 25 hours for Google, and nearly 40 hours for LiveCareer due to the different complexities of the websites and the volume of data.
- Following the scraping phase, the downloaded images underwent extensive filtering procedures over approximately 80 hours to ensure the quality and relevance of the data.
- As the final step, optical character recognition (OCR) algorithms were applied to extract textual content from the resume images. This OCR process was completed separately for Google/Bing and LiveCareer data, consuming approximately 95 hours and 145 hours, respectively, to process the entire dataset.

## Visualization:
![Average Word Count]([image-url](https://github.com/noran-mohamed/Resume-Classification-Dataset/blob/main/average_word_count.png)https://github.com/noran-mohamed/Resume-Classification-Dataset/blob/main/average_word_count.png)
![Average Character Count]([image-url](https://github.com/noran-mohamed/Resume-Classification-Dataset/blob/main/average_char_count.png)https://github.com/noran-mohamed/Resume-Classification-Dataset/blob/main/average_char_count.png)

## Challenges in The Dataset

### Unstructured Format
- The data lacks the structured format typically found in datasets, making it challenging to extract specific information such as "Name", "Education", "Experience", etc. Resumes are in a free-text format without clear sections.

### Personal Information
- Resumes may contain personal information like names, phone numbers, and email addresses scattered throughout the text, posing privacy concerns.

### Overlapping Content (Repeated)
- Skills or experiences may be mentioned multiple times in different resume sections, such as both in the summary and work experience sections, leading to redundancy.

### Spelling Errors
- Misspellings like "experiance" instead of "experience" or "technicl" instead of "technical" might be present in the text, affecting the quality of the data.

### Irrelevant Text
- Headers, footers, and contact information at the top or bottom of the resume may not be relevant to the content analysis and should be filtered out.

### Watermarks and Highlighted Text
- Some resumes may have watermarks or highlighted sections that need to be removed or accounted for during analysis to prevent bias.

### Special Characters
- Special characters such as '*', '/', '&', '$', '%', '⚫', '^', '~', '★' may be present in the resume text and need to be handled appropriately during preprocessing.

### Links
- Resumes might contain URLs or links to personal websites or online profiles, which should be handled appropriately to ensure accurate analysis.

### Irrelevant Experience
- Resumes may contain experience irrelevant to the job being applied for, which needs to be identified and filtered out during analysis.


## Data Preprocessing

### Lowercasing
- We converted all text in the 'Text' column to lowercase to ensure consistency in text representation.

### Removing Punctuation
- We removed punctuation marks from the text using regular expressions (re) to eliminate non-alphanumeric characters.

### Additional Cleaning
- We applied a custom function ('Clean_Resume_Text') to perform further cleaning, including removing URLs, Twitter handles, hashtags, and special characters, and converting contractions to their expanded forms.

### Tokenization
- We tokenized the preprocessed text using the 'word_tokenize' function from the nltk library, splitting the text into individual words or tokens.

### Removing Stop Words
- We removed common stop words such as 'and', 'the', and 'is' using NLTK's stop words corpus to improve the quality of the tokenized text.

### Images Data set
- you can find the images dataset through the following [Link](https://www.kaggle.com/datasets/youssefkhalil/resumes-images-datasets/settings)


