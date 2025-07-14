# Sudoku3D Generator

A fully customizable and unique Sudoku puzzle generator written in Python, using a 3D board structure instead of the traditional 2D format. It allows generating puzzles of varying sizes (e.g., 9x9, 16x16) and difficulty levels (easy, medium, hard).

---

## 📁 Project Structure

* `sudoku_generator.py` – Main script implementing the Sudoku3D class
* `README.md` – Project documentation
* `test_sudoku3d.py` – (Optional) Unit tests for validation

---

## 🧠 Key Idea

Instead of using a flat 2D array for the board, this generator uses a nested **3D list**:

```python
board[row][group][index]
```

* `row` = the horizontal row (0 to grid\_size - 1)
* `group` = which mini-box group within that row
* `index` = position inside the group

This structure simplifies box validation logic and avoids complex math.

---

## ⚙️ Features

* ✅ Fully solved Sudoku generator using backtracking
* ✅ Configurable board sizes: 9x9, 16x16, 25x25 (block size 3–5)
* ✅ Adjustable difficulty (Easy, Medium, Hard)
* ✅ Purely uses index-based logic (no math box-mapping)
* ✅ Clean and readable printing of the puzzle

---

## 🚀 How to Run

```bash
python sudoku_generator.py
```

You will be prompted to:

1. Enter block size (e.g., 3 for 9x9)
2. Choose difficulty: 1 = Easy, 2 = Medium, 3 = Hard

---

## 📌 Example

```bash
Enter block size (e.g., 3 for 9x9, 4 for 16x16): 3
Choose difficulty: [1] Easy  [2] Medium  [3] Hard
Enter difficulty level (1-3): 2
```

---

## 🧪 Testing

You can write unit tests using `pytest` or basic assertions. Sample test functions check:

* Board structure
* Correctness of puzzle solution
* Difficulty clue counts

---

## 📚 Author’s Logic

This project avoids complex box-access math and instead embraces a structure where:

* Box validation uses predefined row ranges
* Column checks iterate via fixed group + index
* No flattening required — keeps data in original nested structure

It balances performance, clarity, and flexibility.

---

## 💡 Future Ideas

* Add GUI interface (Tkinter or Pygame)
* Web version using Flask or Django
* Puzzle solving interface
* Unique puzzle generation enforcement

---

## 🏁 License

Open-source project. You may modify and redistribute with credit.
