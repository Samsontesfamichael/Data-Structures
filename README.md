# Data Structures and Algorithms

A comprehensive collection of data structures and algorithms implemented in both **Python** and **C/C++**.

## 🎓 For New Students & Learners

### What is This Repository?

This is a **complete learning resource** for understanding data structures and algorithms - the fundamental building blocks of computer science. Whether you're a beginner or reviewing concepts, this repository provides:

- ✅ **Clear implementations** in two languages (Python for learning, C for understanding memory)
- ✅ **Working examples** you can run immediately
- ✅ **Step-by-step explanations** in code comments
- ✅ **Time/space complexity** for each operation

### Prerequisites

**For Python:**
- Basic Python knowledge (variables, loops, functions)
- Python 3.6 or higher installed

**For C:**
- Basic C knowledge (pointers, structs, memory management)
- GCC compiler or any C compiler

**No prior data structures knowledge required!** Start from the beginning and work your way up.

### 📚 Recommended Learning Path

Follow this order for the best learning experience:

#### **Level 1: Basics (Start Here!)**
1. **Arrays** (built-in to languages)
2. **Linked Lists** → `python/data_structures/linked_list.py`
   - Understand: How to connect data using pointers/references
   - Why: Foundation for all other structures
3. **Stacks & Queues** → `python/data_structures/queues.py`
   - Understand: LIFO (Last In First Out) and FIFO (First In First Out)
   - Why: Used everywhere (browser history, task scheduling)

#### **Level 2: Intermediate**
4. **Binary Search Tree** → `python/data_structures/binary_search_tree.py`
   - Understand: Hierarchical data organization
   - Why: Fast searching, sorting, and organizing data
5. **Heap** → `python/data_structures/heap.py`
   - Understand: Priority-based data access
   - Why: Used in priority queues, scheduling algorithms
6. **Sets** → `python/data_structures/sets.py`
   - Understand: Unique collections and set operations
   - Why: Remove duplicates, check membership

#### **Level 3: Advanced**
7. **AVL Tree** → `python/data_structures/avl_tree.py`
   - Understand: Self-balancing trees
   - Why: Guaranteed O(log n) performance

#### **Algorithms: Sorting**
8. **Start with simple sorts** → `python/algorithms/sorting.py`
   - Bubble Sort (easiest to understand)
   - Insertion Sort (how humans sort cards)
9. **Move to efficient sorts**
   - Merge Sort (divide and conquer)
   - Quick Sort (most commonly used)

### 🚀 Quick Start Guide

#### Step 1: Choose Your Language

**Python** (Recommended for beginners):
- Easier to read and understand
- Focus on concepts, not syntax
- No memory management needed

**C** (For deeper understanding):
- See how memory actually works
- Understand pointers and manual memory management
- Better for systems programming

#### Step 2: Run Your First Example

```bash
# Navigate to the project folder
cd c:\Users\UserName\Directory\Data-Structures
OR
cd D/E:\Directory\Data-Structures

# Run a Python example
python python/data_structures/linked_list.py
```

You'll see output showing:
- How to insert elements
- How to search for values
- How to delete elements
- How the data structure works

#### Step 3: Read the Code

Open the file and read through:
1. **Class/struct definition** - How data is stored
2. **Methods/functions** - What operations you can do
3. **Comments** - Explanations of WHY things work
4. **Example usage** - See it in action

#### Step 4: Experiment!

Modify the example code:
- Change the values being inserted
- Try different operations
- Break it and fix it (best way to learn!)

### 📖 Understanding the Code

Each file follows this structure:

```python
# 1. DEFINITION - What is this data structure?
class DataStructure:
    def __init__(self):
        # How we store data
        
    # 2. OPERATIONS - What can we do?
    def insert(self, value):
        # Add data
        
    def search(self, value):
        # Find data
        
    def delete(self, value):
        # Remove data

# 3. EXAMPLES - See it working!
if __name__ == "__main__":
    # Test code you can run
```

### 🎯 Learning Tips

1. **Start Simple**: Don't jump to AVL trees on day one!
2. **Run the Code**: Reading is good, running is better
3. **Draw It Out**: Sketch the data structures on paper
4. **Modify Examples**: Change values, add your own tests
5. **Compare Languages**: See Python vs C implementations
6. **Check Complexity**: Understand WHY operations take certain time

### 🤔 Common Questions

**Q: Which language should I learn first?**  
A: Start with Python. It's clearer and lets you focus on concepts.

**Q: Do I need to memorize all the code?**  
A: No! Understand the concepts. You can always look up syntax.

**Q: What's "Big O" notation?**  
A: It tells you how slow/fast an operation gets as data grows. O(1) = super fast, O(n²) = gets slow quickly.

**Q: Why learn both Python and C?**  
A: Python shows WHAT happens. C shows HOW it happens in memory.

**Q: Where do I use these in real life?**  
A: Everywhere! Databases use trees, operating systems use queues, games use heaps for AI, etc.

### 📊 Visual Guide to Complexity

```
O(1)      - Instant          ⚡ [Best]
O(log n)  - Very Fast        🚀
O(n)      - Linear           ✓
O(n log n)- Pretty Good      ✓
O(n²)     - Gets Slow        ⚠️
O(2ⁿ)     - Very Slow        ❌ [Avoid]
```

**Example**: Finding a name in a phone book
- O(n): Check every page (Linear Search)
- O(log n): Open middle, go left/right (Binary Search)
- O(1): Know the exact page (Hash Table)

## 📚 Contents

### Part I: Data Structures

#### 1. Linked Lists
- **Singly Linked List**
  - Insertion (beginning, end, position)
  - Searching
  - Deletion (by value, by position)
  - Traversal (forward and reverse)
  
- **Doubly Linked List**
  - Insertion (beginning, end, position, after node)
  - Deletion (by value, by position)
  - Bidirectional traversal

#### 2. Binary Search Tree (BST)
- Insertion
- Searching
- Deletion
- Finding parent nodes
- Finding min/max values
- Tree traversals:
  - Preorder (Root → Left → Right)
  - Inorder (Left → Root → Right) - sorted order
  - Postorder (Left → Right → Root)
  - Breadth-first (level order)

#### 3. Heap
- Min Heap implementation
- Insertion
- Deletion (extract min)
- Searching
- Heapify operations
- Build heap from array

#### 4. Sets
- **Unordered Set** (hash-based)
- **Ordered Set** (sorted array/tree-based)
- Set operations: union, intersection, difference
- Subset/superset checking

#### 5. Queues
- **Standard Queue** (FIFO)
- **Priority Queue** (heap-based)
- **Double Ended Queue (Deque)**

#### 6. AVL Tree
- Self-balancing binary search tree
- Tree rotations (left, right)
- Automatic rebalancing
- Insertion with balancing
- Deletion with balancing
- Maintains O(log n) height

### Part II: Algorithms

#### Sorting Algorithms
1. **Bubble Sort** - O(n²) time, O(1) space
2. **Merge Sort** - O(n log n) time, O(n) space
3. **Quick Sort** - O(n log n) average, O(n²) worst
4. **Insertion Sort** - O(n²) time, O(1) space
5. **Shell Sort** - O(n log n) to O(n²) time
6. **Radix Sort** - O(d×(n+k)) time, non-comparison based

#### Numeric Algorithms
1. **Primality Test** - Check if number is prime
2. **Base Conversions** - Convert between number bases
3. **GCD/LCM** - Greatest common denominator and least common multiple
4. **Factorial** - Calculate factorial with multiple approaches
5. **Fibonacci** - Generate Fibonacci numbers
6. **Fast Exponentiation** - Efficient power calculation

#### Searching Algorithms
1. **Sequential Search** - Linear search through array
2. **Probability Search** - Self-organizing search (move-to-front, transpose)
3. **Binary Search** - O(log n) search on sorted arrays
4. **Jump Search** - O(√n) search algorithm
5. **Interpolation Search** - O(log log n) for uniform distributions

#### String Algorithms
1. **Word Reversal** - Reverse word order in sentences
2. **Palindrome Detection** - Check if string reads same forwards/backwards
3. **Word Counting** - Count words in text
4. **Repeated Words** - Find and count repeated words
5. **Character Matching** - Find matching characters between strings
6. **Anagram Detection** - Check if strings are anagrams
7. **String Compression** - Run-length encoding
8. **String Rotation** - Check if one string is rotation of another

## 🗂️ Project Structure

```
Data-Structures/
├── python/
│   ├── data_structures/
│   │   ├── linked_list.py
│   │   ├── doubly_linked_list.py
│   │   ├── binary_search_tree.py
│   │   ├── heap.py
│   │   ├── sets.py
│   │   ├── queues.py
│   │   └── avl_tree.py
│   └── algorithms/
│       ├── sorting.py
│       ├── numeric.py
│       ├── searching.py
│       └── strings.py
└── c/
    ├── data_structures/
    │   ├── linked_list.c
    │   ├── doubly_linked_list.c
    │   ├── binary_search_tree.c
    │   ├── heap.c
    │   └── queues.c
    └── algorithms/
        ├── sorting.c
        ├── numeric.c
        ├── searching.c
        └── strings.c
```

## 🚀 Usage

### Python

Each Python file can be run independently with example usage:

```bash
python python/data_structures/linked_list.py
python python/data_structures/binary_search_tree.py
python python/algorithms/sorting.py
python python/algorithms/numeric.py
python python/algorithms/searching.py
python python/algorithms/strings.py
```

### C

Compile and run C files:

```bash
# Compile
gcc c/data_structures/linked_list.c -o linked_list
gcc c/algorithms/sorting.c -o sorting
gcc c/algorithms/numeric.c -o numeric -lm
gcc c/algorithms/searching.c -o searching -lm
gcc c/algorithms/strings.c -o strings

# Run
./linked_list
./sorting
./numeric
./searching
./strings
```

Or on Windows:
```powershell
gcc c/data_structures/linked_list.c -o linked_list.exe
gcc c/algorithms/sorting.c -o sorting.exe
gcc c/algorithms/numeric.c -o numeric.exe -lm
gcc c/algorithms/searching.c -o searching.exe -lm
gcc c/algorithms/strings.c -o strings.exe

./linked_list.exe
./sorting.exe
./numeric.exe
./searching.exe
./strings.exe
```

**Note**: `-lm` flag links the math library (required for `sqrt`, `pow` functions)

## 📊 Time Complexity Summary

| Data Structure | Insert | Delete | Search | Space |
|---------------|--------|--------|--------|-------|
| Singly Linked List | O(1)* | O(n) | O(n) | O(n) |
| Doubly Linked List | O(1)* | O(n) | O(n) | O(n) |
| Binary Search Tree | O(log n)† | O(log n)† | O(log n)† | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(n) |
| Min Heap | O(log n) | O(log n) | O(n) | O(n) |
| Hash Set | O(1)‡ | O(1)‡ | O(1)‡ | O(n) |

*O(1) for insertion at head/tail  
†Average case; worst case O(n) for unbalanced tree  
‡Average case; worst case O(n)

| Sorting Algorithm | Time (Avg) | Time (Worst) | Space |
|------------------|------------|--------------|-------|
| Bubble Sort | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n²) | O(log n) |
| Insertion Sort | O(n²) | O(n²) | O(1) |
| Shell Sort | O(n log n) | O(n²) | O(1) |
| Radix Sort | O(d×n) | O(d×n) | O(n+k) |

## ✨ Features

- ✅ Complete implementations in both Python and C
- ✅ Comprehensive comments explaining logic
- ✅ Time and space complexity annotations
- ✅ Example usage and test cases in each file
- ✅ Proper memory management in C implementations
- ✅ Clean, readable code following best practices

## 📖 Learning Resources

Each implementation includes:
- Detailed comments explaining the algorithm
- Complexity analysis
- Example usage demonstrating all operations
- Test cases validating correctness

## 🔧 Requirements

**Python**: Python 3.6+  
**C**: GCC compiler or any C compiler supporting C99

## 📝 Notes

- Python implementations prioritize readability and demonstration of concepts
- C implementations demonstrate manual memory management and pointer usage
- All code includes proper error handling
- Test cases are included in main functions for easy verification

## 🤝 Contributing

Feel free to:
- Add more data structures
- Implement additional algorithms
- Optimize existing implementations
- Add more comprehensive test cases

---

**Happy Coding! 🎉**

---

## 📚 References

This implementation is based on concepts and algorithms from:

- **Data Structures Complete Notes** - College of Engineering Trivandrum (CET)
  - Source: [DS Complete.pdf](https://www.cet.edu.in/noticefiles/280_DS%20Complete.pdf)
  - A comprehensive guide covering fundamental data structures and algorithms

- **Data Structures and Algorithms** - Mount Allison University
  - Source: [Dsa.pdf](https://mta.ca/~rrosebru/oldcourse/263114/Dsa.pdf)
  - Course materials by R. Rosebru

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Samson Tesfamichael**

- 🌐 Portfolio: [samsontesfamichael.github.io/personalportfolio](https://samsontesfamichael.github.io/personalportfolio)
- 💻 GitHub: [@Samsontesfamichael](https://github.com/Samsontesfamichael)
- 📧 Email: samsontesfamichael11@gmail.com

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ by Samson Tesfamichael
