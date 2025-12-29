from functions.get_files_info import get_files_info

test_cases = [("calculator", "."),("calculator", "pkg"),("calculator", "/bin"),("calculator", "../")]

def test():
    for case in test_cases:
        result = get_files_info(case[0],case[1])
        if case[1] == ".":
            print(f"Result for current directory:")
        else:
            print(f"Result for {case[1]} directory:")
        print(result)

if __name__ == "__main__":
    test()