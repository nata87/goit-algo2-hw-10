from colorama import Fore, Style, init
init(autoreset=True)

class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []
    used = set() 

    while remaining_subjects:
        best_idx = None
        best_coverage = set()

        for i, teacher in enumerate(teachers):
            if i in used:
                continue
            coverage = teacher.can_teach_subjects & remaining_subjects
            if not coverage:
                continue  
  
            if (len(coverage) > len(best_coverage) or
                (len(coverage) == len(best_coverage) and best_idx is not None and teacher.age < teachers[best_idx].age) or
                (len(coverage) == len(best_coverage) and best_idx is None)):
                best_idx = i
                best_coverage = coverage

        if best_idx is None:
            print(Fore.RED + "Неможливо покрити всі предмети наявними викладачами." + Style.RESET_ALL)
            return None

        t = teachers[best_idx]
        t.assigned_subjects = best_coverage.copy()  
        schedule.append(t)
        used.add(best_idx)
        remaining_subjects -= best_coverage

    return schedule

if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print(Fore.CYAN + "Розклад занять:" + Style.RESET_ALL)
        for t in schedule:
            taught = ", ".join(sorted(t.assigned_subjects)) if t.assigned_subjects else "(нічого)"
            print(Fore.GREEN + f"{t.first_name} {t.last_name}, {t.age} років, email: {t.email}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   Викладає предмети: {taught}\n" + Style.RESET_ALL)
    
