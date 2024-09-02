

print("St-1")
try:
    print(2/a)
except ZeroDivisionError:
    print("Normal Execution")
except TypeError:
    print("Normal Execution")
except ValueError:
    print("Normal Execution")
except NameError:
    print("Normal Execution")
print("St-2")

print("St-3")
try:
    print(2/a)
except (ZeroDivisionError, TypeError, ValueError, NameError):
    print("Normal Execution")
print("St-4")

print("St-5")
try:
    print(2/a)
except (ZeroDivisionError, TypeError, ValueError):
    print("Normal Execution")
except:
    print("Normal Execution(Default)")
print("St-6")

print("St-7")
try:
    print(2/a)
except (ZeroDivisionError, TypeError, ValueError,NameError):
    print("Normal Execution")
except:
    print("Normal Execution(Default)")
finally:
    print("finally inside the except call")
print("St-8")


