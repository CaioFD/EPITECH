def analyze_grades(grades):
    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))
    print("Average grade:", round(sum(grades) / len(grades), 2))

n = int(input("How many students? "))

grades = []
for i in range(n):
    score = float(input(f"Score of student {i + 1}: "))
    grades.append(score)

analyze_grades(grades)