# 📚 AI-Powered Flashcard Generator from PDFs

This application allows users to generate flashcards from PDF files using artificial intelligence. It is ideal for students and professionals who want to transform text into questions and answers automatically.

⚠️ **Warning** ⚠️ Please note that the document will be processed by OpenAI. Do not enter any personal data or sensitive information.

## 🚀 How to Use the Application?

1. **Upload the PDF**  
   - In the sidebar, select a PDF file containing the information you want to convert into flashcards.
   - Select the number of flashcards you want 

2. **Wait for Processing**  
   - The application will extract text from the PDF and automatically generate flashcards.  
   - This may take a few seconds depending on the size of the document.  

3. **Copy the Generated Flashcards**  
   - Once generated, the flashcards will appear in a text box.  
   - Copy the content.  

4. **Paste into a Flashcard App**  
   - Use an app like **AnkiPro** or any other compatible flashcard application.  
   - Configure the format so that:  
     - `;` separates the question from the answer.  
     - `;;` separates each flashcard.  

## 📌 Example Output

```
Q: What is machine learning?; A: It is a branch of artificial intelligence that allows systems to learn from data without being explicitly programmed.;;
Q: What is the equation of a straight line?; A: The general equation is y = mx + b, where m is the slope and b is the y-intercept.;;
```

By importing this text into **AnkiPro** (or any other compatible app), the flashcards will be created automatically with the correct question-answer separation. 🎓  

## 🛠️ Installation and Execution

To run the application in your own environment:

1. Clone this repository or download the files.
2. Ensure you have **Python 3.8+** installed.
3. Install the dependencies with:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application with:

   ```bash
   streamlit run app.py
   ```

5. Open the application in your browser and start generating flashcards. 🚀

## 📌 Requirements

Ensure you have the following dependencies installed:

- `streamlit`
- `PyPDF2`
- `openai`

You can install them with:

```bash
pip install streamlit PyPDF2 openai
```

## 📌 Additional Notes

- A **valid OpenAI API key** is required for the model to generate flashcards.  
- The application limits the extracted text to **3000 characters** to avoid API overload.  
- The maximum number of flashcards that can be generated is **20**.  

## 📩 Contact

Álvaro Ruedas Mora
    
- Data Scientist from **Ironhack**
- Industrial and Automation Electronics Engineer from **Polytechnic University of Madrid**
- MBA from **EAE Business School**

## 📜 License

This project, including all its code, documentation, and assets, is the intellectual property of the author. Unauthorized reproduction, distribution, or use of any part of this project without explicit permission is prohibited.

📩 We hope this tool helps you study more effectively! 🚀 