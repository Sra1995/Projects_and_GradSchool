### C++ Basics  

**1. Difference between references and pointers?**  
- **References**:  
  - They act as an alias to another variable, meaning they always refer to the same variable once initialized.  
  - Cannot be null and must be initialized at the time of declaration.  
  - Syntax: `int &ref = x;`  

- **Pointers**:  
  - They store the memory address of a variable.  
  - Can be null or uninitialized and can be reassigned to point to other variables during their lifetime.  
  - Syntax: `int *ptr = &x;`  

**2. Difference between memory allocation in stack and heap?**  
- **Stack**:  
  - Automatically managed memory, where local variables and function calls are stored.  
  - Faster allocation/deallocation but limited in size and scope.  
  - Memory is reclaimed as functions return or variables go out of scope.  

- **Heap**:  
  - Dynamically allocated memory using `new` or `malloc`.  
  - Slower to allocate and requires manual deallocation using `delete` or `free`.  
  - Larger and persists until explicitly freed, but prone to memory leaks if not managed properly.  

**3. What kinds of smart pointers exist?**  
- **`unique_ptr`**: Provides sole ownership of an object. No two `unique_ptr`s can own the same object.  
- **`shared_ptr`**: Allows shared ownership of an object with automatic reference counting to manage the object's lifetime.  
- **`weak_ptr`**: Non-owning reference to a `shared_ptr` object, primarily used to prevent cyclic dependencies.  
- **`scoped_ptr`** (deprecated): Provided unique ownership in older versions of C++. Replaced by `unique_ptr`.  

**4. How is `unique_ptr` implemented? How do we force only one owner to exist?**  
- `unique_ptr` is implemented using move semantics (`std::move`), and it deletes its copy constructor and assignment operator to prevent copying.  
- Ownership transfer is only possible using `std::move()`. This ensures that only one `unique_ptr` owns the object at any time.

**5. How does `shared_ptr` work? How is the reference counter synchronized?**  
- `shared_ptr` uses a control block that tracks:  
  1. **Reference count**: How many `shared_ptr` instances own the object.  
  2. **Weak reference count**: Number of `weak_ptr` instances referring to the object.  
- The reference counter is synchronized using atomic operations to ensure thread safety during increment or decrement.

**6. Can we copy `unique_ptr` or pass it from one object to another?**  
- No, `unique_ptr` cannot be copied due to its deleted copy constructor. However, ownership can be transferred to another `unique_ptr` using `std::move()`.

**7. What are rvalue and lvalue?**  
- **lvalue**: An object with a persistent address in memory. Example: Variables (`int x = 5;`).  
- **rvalue**: Temporary object or value without a persistent address. Example: Results of expressions (`x + 10`).  

**8. What are `std::move` and `std::forward`?**  
- **`std::move`**: Converts an lvalue to an rvalue, enabling resources to be "moved" rather than copied (e.g., transferring ownership of a `unique_ptr`).  
- **`std::forward`**: Used in template functions to perfectly forward arguments, preserving their lvalue/rvalue nature.

---

### OOP  

**1. Ways to access private fields of a class?**  
- Use public getters/setters to expose or modify private fields.  
- Declare a function or class as a `friend` to grant access.  
- Use pointer manipulation (not recommended and unsafe).  
- Exploit language-specific quirks or reflection in debug mode (platform-dependent).  

**2. Can a class inherit multiple classes?**  
- Yes, C++ allows multiple inheritance. However, the diamond problem can arise when two parent classes inherit from the same base class.  
- This can be resolved using **virtual inheritance**.  

**3. Is a static field initialized in a class constructor?**  
- No, static fields are initialized separately and shared across all instances of the class. Initialization happens outside the class, typically in a `.cpp` file.  

**4. Can an exception be thrown in a constructor/destructor? How to prevent that?**  
- **Constructors** can throw exceptions when initialization fails. Use RAII to manage resources safely.  
- **Destructors** should avoid throwing exceptions since it may lead to `std::terminate` if exceptions propagate during stack unwinding.  

**5. What are virtual methods?**  
- Virtual methods enable runtime polymorphism, allowing derived class implementations to be invoked via base class pointers or references.

**6. Why do we need a virtual destructor?**  
- Without a virtual destructor, destroying a derived class object through a base class pointer will cause undefined behavior by not calling the derived class destructor.

**7. Difference between abstract class and interface?**  
- Abstract class: Can have pure virtual methods and implemented methods, along with data members.  
- Interface: Conceptually, all methods are pure virtual (no implementation or data members).  

**8. Can a constructor be virtual?**  
- No, constructors cannot be virtual since they are responsible for object creation, and virtual functions rely on an object being constructed.  

**9. How is the `const` keyword used for class methods?**  
- A `const` method guarantees it will not modify the object or call non-const methods. Example:  
  ```cpp
  int getValue() const;
  ```

**10. How to protect an object from copying?**  
- Delete the copy constructor and assignment operator:  
  ```cpp
  MyClass(const MyClass&) = delete;
  MyClass& operator=(const MyClass&) = delete;
  ```

---

### STL Containers  

**1. Difference between `vector` and `list`?**  
- `vector`: Uses contiguous memory, offering fast random access. However, insertions/deletions are slow except at the end due to shifting elements.  
- `list`: Uses a doubly linked list, enabling fast insertions/deletions anywhere, but traversal is slower and memory overhead is higher.  

**2. Difference between `map` and `unordered_map`?**  
- `map`: Stores elements in sorted order, implemented using a Red-Black tree, with O(log n) operations.  
- `unordered_map`: Stores elements in no particular order, implemented using a hash table, with O(1) average-time operations but worse performance for poor hash functions.  

**3. Does calling `push_back()` make an iterator in `vector` invalid?**  
- Yes, if `push_back()` triggers a reallocation (e.g., when the vector grows beyond its capacity), all iterators and references are invalidated.

**4. How to modify your class to use it with `map` and `unordered_map`?**  
- For `map`: Implement `operator<` for ordering.  
- For `unordered_map`: Provide a custom hash function and equality operator.

---

### Threads  

**1. Difference between processes and threads?**  
- **Processes**: Have separate memory spaces and are heavier to create and manage. They do not share memory unless explicitly done using IPC (e.g., pipes).  
- **Threads**: Share the same memory within a process, allowing faster context switching and communication.  

**2. Can the same thread be run twice?**  
- No, once a thread completes, it cannot be restarted. You need to create a new thread for execution.  

**3. Ways to synchronize threads?**  
- Mutexes (e.g., `std::mutex`).  
- Locks (e.g., `std::unique_lock`).  
- Semaphores.  
- Condition variables.  
- Atomic variables for low-level synchronization.  

**4. What is a deadlock?**  
- A situation where two or more threads are stuck waiting for each other to release resources, leading to an indefinite halt.  
- Prevented using lock ordering, avoiding circular dependencies, or using try-lock techniques.  
