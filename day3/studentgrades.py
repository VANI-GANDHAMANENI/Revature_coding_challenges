students_names = [("Shiva", 85), ("Krishna", 92), ("Srinivasa", 67)]

grade = {name: ('A' if score >= 90 else 
                 'B' if score >= 80 else 
                 'C' if score >= 70 else 'F') 
          for name, score in students_names}

print(grade)