try:
    # Some code to attempt to run
except Exception as e:
    # Some other code to run as a fallback if an error happens
As you can see in the example, try and except are keywords in Python. They work together as follows:

Python tries to run the code in the try block.

If something goes wrong, Python jumps to the except block and runs that code instead of crashing.

Note that the code in try and except blocks must be indented by four spaces or one Tab space. This tells Python which lines belong in the try block and which belong in the except block.

You can think of an except block as a fallback plan for when something goes wrong. Here is where you can provide a friendly message to the user about what went wrong or run other code that would need to run regardless of the error.
except Exception as e:
The word Exception is a special Python keyword. It tells Python to catch any kind of error.

The e indicates that Python should save an error in the variable e. You don’t have to name it e— you can name it any variable name—but e is a common variable developers use here because it's short for error. You can print or use the e variable to learn more about what went wrong in the program.

Notice the added except ValueError block. Since you can identify the specific error type, you can create a targeted except block for that specific error type (in this case, ValueError). This allows you to provide an error message that directly addresses the user's mistake.

Try running the program and enter Bella as input. Notice how you now receive a more informative error message that specifically addresses the invalid input, rather than seeing a technical error message or program crash.


SOL.PY
The initial error is that the input() function returns a string (like "3"), but range() requires a number, causing a TypeError in range(num_certificates).

•
To solve this, the following changes were made:

Enclosed the problematic code in a try block

Converted the string input to an integer using int()

Added a specific except ValueError to handle text inputs

Included a general except Exception as e as a catchall safety net

•
This solution transforms the raw string input into usable integer data while gracefully handling potential errors.

Summary

In this lesson, you learned how to use Python's try and except blocks to handle errors and prevent programs from crashing. You first explored how errors like ValueError occur when users provide incorrect input, such as typing a word instead of a number. You learned how to catch all errors using except Exception as e, print helpful details about the error, and identify its type using type(e). Then, you took it a step further by learning to catch specific errors, like ValueError, so you can provide clearer, more helpful messages to users and improve the user experience. You practiced this with real-world examples from AnyCompany Pet Society and built skills to create more reliable and user-friendly Python programs. Nice work!
